from ExpressionEvaluator import *
from classes.parser.stack.stack import ParserStack
import classes.expression.expressions as exp
import Tests.utils as utils

def testExpressionStackOperations():
	tester = utils.Tester("Expression stack operation tests")
	
	operatorDummy = 0
	operatorDummy2 = 1
	operatorDummy3 = 2

	numberDummy = -1
	numberDummy2 = -2
	numberDummy3 = -3
	
	evaluate("1+1")
	
	def testCorrectOperatorSizeReported():
		def f():
			stack = ParserStack()
			stack.pushOperator(operatorDummy)	
			stack.pushOperator(operatorDummy2)
			stack.pushOperator(operatorDummy3)

			if not stack.operatorStackSize() == 3:
				return "Operator stack size does not equal 3. Instead it equals: %d" % stack.operatorStackSize()
		return utils.Test("Test that correct operator size is reported", f)	
		
	tester.addTest(testCorrectOperatorSizeReported())	

	def testCanParserStackQueryPopCorrectRootNode():
		def f():
			stack = ParserStack()
			stack.pushNumber(1)
			stack.pushNumber(2)
			stack.pushOperator("+")
			
			_logic = ParserStackInteractor(stack)
			rootNode = _logic.popRootNode()

			if not rootNode:
				return "No root node created"
			
			if rootNode._operandA != 1:
				return "Root node left operand does not equal 1. Instead it equals: " + str(rootNode._operandA)

			if rootNode._operandB != 2:
				return "Root node right operand does not equal 2. Instead it equals: " + str(rootNode._operandB)

			if rootNode._operator != "+":
				return "Root node operator does not equal '+'. Instead it equals: " + rootNode._operator		
			
		return utils.Test("Test that an expression stack logic instance will create a correct root node", f)
	
	tester.addTest( testCanParserStackQueryPopCorrectRootNode() )		

	def make7Minus4Times8Tree(stack):		
		rootNode = exp.BinaryOperandExpression(4, '*', 8)			
		
		stack.pushNumber(7)
		stack.pushOperator('-')
		_logic = ParserStackInteractor(stack)

		leftOperand = _logic.popSingleNumber()
		return _logic.popOperatorAndJoinNodes(leftOperand, rootNode)
				
	def test7Minus4Times8Tree(tree):
		if not tree:
			return "No root node created"
			
		if tree._operandA != 7:
			return "Root node left operand does not equal 7. Instead it equals: " + str(tree._operandA)

		if not tree._operandB:
			return "Root node has no right operand."

		if tree._operandB._operandA != 4:
			return "Root node's right operand node's left operand does not equal 4. Instead it equals: " + str(tree._operandB._operandA)

		if tree._operandB._operandB != 8:
			return "Root node's right operand node's right operand does not equal 8. Instead it equals: " + str(tree._operandB._operandB)

		if tree._operandB._operator != '*':
			return "Root node's right operand node's operator does not equal '*'. Instead it equals: " + str(tree._operandB._operator)

		if tree._operator != '-':
			return "Root node's operator does not equal '-'. Instead it equals: " + str(tree._operator)
		
	def testCanJoinANodeAsRightOperand():
		def f():	
			stack = ParserStack()		
			newRootNode = make7Minus4Times8Tree(stack)
			return test7Minus4Times8Tree(newRootNode)

		return utils.Test("Test that we can join a node as the right to an expression", f)
	tester.addTest(testCanJoinANodeAsRightOperand())


	def make7Minus4Times8Plus3Tree(stack):
		stack = ParserStack()		
		originalRootNode = make7Minus4Times8Tree(stack)
		fail = test7Minus4Times8Tree(originalRootNode)
			
		if fail:	
			raise ValueError(fail)		

		stack.pushNumber(3)
		stack.pushOperator('+')

		_logic = ParserStackInteractor(stack)
		rightOperand = _logic.popSingleNumber()
		return _logic.popOperatorAndJoinNodes(originalRootNode, rightOperand)		
	
	def test3PlusTree(tree):
		if not tree:
			return "No new root created"

		if tree._operandB != 3:
			return "New root node's right operand does not equal 3. Instead it equals: " + str(tree._operandB)

		if tree._operator != '+':
			return "New root node's operator does not equal '+'. Instead it equals: " + str(tree._operator)

		leftOperand = tree._operandA

		return test7Minus4Times8Tree(leftOperand)

	def testCanJoinANodeAsLeftOperand():
		def f():			
			try:
				stack = ParserStack()								
				newRootNode = make7Minus4Times8Plus3Tree(stack)
				return test3PlusTree(newRootNode)				
			except ValueError as err:
				return str(err)
			
		return utils.Test("Test that we can join a node as the left operand to an expression", f)
	tester.addTest(testCanJoinANodeAsLeftOperand())	

	def testCanJoinTwoNodesWithOperator():			
		def f():			
			try:
				stack = ParserStack()								
				newRootNode = make7Minus4Times8Plus3Tree(stack)
				fail = test3PlusTree(newRootNode)				
				
				if fail:
					raise ValueError(fail)
				
				stack.pushNumber(4)
				stack.pushNumber(2)
				stack.pushOperator('/')

				_logic = ParserStackInteractor(stack)				
				rightNode = _logic.popRootNode()
				stack.pushOperator('-')
				newTree = _logic.popOperatorAndJoinNodes(newRootNode, rightNode)
				
				if not newTree:
					return "No new tree returned"

				if newTree._operator != '-':
					return "New tree operator does not equal '-'. Instead it equals: " + str(newTree._operator)

				if newTree._operandB._operator != '/':
					return "New tree right operand operator does not equal '/'. Instead it equals: " + str(newTree._operandB._operator)

				if newTree._operandB._operandA != 4:
					return "New tree right operand left operand does not equal 4. Instead it equals: " +str(newTree._operandB._operandA)

				if newTree._operandB._operandB != 2:
					return "New tree right operand right operand does not equal 2. Instead it equals: " +str(newTree._operandB._operandB)  

				leftNode = newTree._operandA
				
				return test3PlusTree(leftNode)



		
			except ValueError as err:
				return str(err)
			
		return utils.Test("Test that we can join two nodes to an expression", f)
	tester.addTest(testCanJoinTwoNodesWithOperator())			
	tester.perform()


	

def main():
	testExpressionStackOperations()


	
