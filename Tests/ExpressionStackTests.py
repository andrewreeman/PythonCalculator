from ExpressionEvaluator import *
import expressionstack as expstack
import expressionstacklogic as logic
import expressions as exp
import utils
import operators as ops

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
			stack = expstack.ExpressionStack()
			stack.pushOperator(operatorDummy)	
			stack.pushOperator(operatorDummy2)
			stack.pushOperator(operatorDummy3)

			if not stack.operatorStackSize() == 3:
				return "Operator stack size does not equal 3. Instead it equals: %d" % stack.operatorStackSize()
		return utils.Test("Test that correct operator size is reported", f)	

		
	tester.addTest(testCorrectOperatorSizeReported())	


	def testCanExpressionStackLogicPopCorrectRootNode():
		def f():
			stack = expstack.ExpressionStack()
			stack.pushNumber(1)
			stack.pushNumber(2)
			stack.pushOperator("+")
			
			_logic = logic.ExpressionStackLogic()

			rootNode = _logic.popRootNode(stack)

			if not rootNode:
				return "No root node created"
			
			if rootNode.leftOperand() != 1:
				return "Root node left operand does not equal 1. Instead it equals: " + str(rootNode.leftOperand())

			if rootNode.rightOperand() != 2:
				return "Root node right operand does not equal 2. Instead it equals: " + str(rootNode.rightOperand())

			if rootNode.operator() != "+":
				return "Root node operator does not equal '+'. Instead it equals: " + rootNode.operator()
		

			
		return utils.Test("Test that an expression stack logic instance will create a correct root node", f)
	
	tester.addTest( testCanExpressionStackLogicPopCorrectRootNode() )
		

	def make7Minus4Times8Tree(stack):
		_logic = logic.ExpressionStackLogic()
		rootNode = exp.BinaryOperandExpression(4, '*', 8)			
		
		stack.pushNumber(7)
		stack.pushOperator('-')

		return _logic.popJoiningRootNodeToRightOperand(stack, rootNode)
			
	
	def test7Minus4Times8Tree(tree):
		if not tree:
			return "No root node created"
			
		if tree.leftOperand() != 7:
			return "Root node left operand does not equal 7. Instead it equals: " + str(tree.leftOperand())

		if not tree.rightOperand():
			return "Root node has no right operand."

		if tree.rightOperand().leftOperand() != 4:
			return "Root node's right operand node's left operand does not equal 4. Instead it equals: " + str(tree.rightOperand().leftOperand())

		if tree.rightOperand().rightOperand() != 8:
			return "Root node's right operand node's right operand does not equal 8. Instead it equals: " + str(tree.rightOperand().rightOperand())

		if tree.rightOperand().operator() != '*':
			return "Root node's right operand node's operator does not equal '*'. Instead it equals: " + str(tree.rightOperand().operator())

		if tree.operator() != '-':
			return "Root node's operator does not equal '-'. Instead it equals: " + str(tree.operator())
		
	def testCanJoinANodeAsRightOperand():
		def f():	
			stack = expstack.ExpressionStack()		
			newRootNode = make7Minus4Times8Tree(stack)
			return test7Minus4Times8Tree(newRootNode)

		return utils.Test("Test that we can join a node as the right to an expression", f)
	tester.addTest(testCanJoinANodeAsRightOperand())


	def make7Minus4Times8Plus3Tree(stack):
		stack = expstack.ExpressionStack()		
		originalRootNode = make7Minus4Times8Tree(stack)
		fail = test7Minus4Times8Tree(originalRootNode)
			
		if fail:	
			raise ValueError(fail)		

		stack.pushNumber(3)
		stack.pushOperator('+')

		_logic = logic.ExpressionStackLogic()
		return _logic.popJoiningRootNodeToLeftOperand(stack, originalRootNode)
	
	def test3PlusTree(tree):
		if not tree:
			return "No new root created"

		if tree.rightOperand() != 3:
			return "New root node's right operand does not equal 3. Instead it equals: " + str(newRootNode.rightOperand())

		if tree.operator() != '+':
			return "New root node's operator does not equal '+'. Instead it equals: " + str(newRootNode.operator())

		leftOperand = tree.leftOperand()

		return test7Minus4Times8Tree(leftOperand)

	def testCanJoinANodeAsLeftOperand():
		def f():			
			try:
				stack = expstack.ExpressionStack()								
				newRootNode = make7Minus4Times8Plus3Tree(stack)
				return test3PlusTree(newRootNode)				
			except ValueError as err:
				return str(err)
			
		return utils.Test("Test that we can join a node as the left operand to an expression", f)
	tester.addTest(testCanJoinANodeAsLeftOperand())	

	def testCanJoinTwoNodesWithOperator():			
		def f():			
			try:
				stack = expstack.ExpressionStack()								
				newRootNode = make7Minus4Times8Plus3Tree(stack)
				fail = test3PlusTree(newRootNode)				
				
				if fail:
					raise ValueError(fail)
				
				stack.pushNumber(4)
				stack.pushNumber(2)
				stack.pushOperator('/')

				_logic = logic.ExpressionStackLogic()
				
				rightNode = _logic.popRootNode(stack)

				stack.pushOperator('-')
				newTree = _logic.popOperatorAndJoinNodes(stack, newRootNode, rightNode)
				
				if not newTree:
					return "No new tree returned"


				if newTree.operator() != '-':
					return "New tree operator does not equal '-'. Instead it equals: " + str(newTree.operator())

				if newTree.rightOperand().operator() != '/':
					return "New tree right operand operator does not equal '/'. Instead it equals: " + str(newTree.rightOperand().operator())

				if newTree.rightOperand().leftOperand() != 4:
					return "New tree right operand left operand does not equal 4. Instead it equals: " + str(newTree.rightOperand().leftOperand())

				if newTree.rightOperand().rightOperand() != 2:
					return "New tree right operand right operand does not equal 2. Instead it equals: " + str(newTree.rightOperand().rightOperand())  

				leftNode = newTree.leftOperand()
				
				return test3PlusTree(leftNode)



		
			except ValueError as err:
				return str(err)
			
		return utils.Test("Test that we can join two nodes to an expression", f)
	tester.addTest(testCanJoinTwoNodesWithOperator())	


	def testCanCheckPrecedenceOfOperatorsOnStack():
		def f():
			stack = expstack.ExpressionStack()	
			
			addOp = ops.AddOperator()
			subOp = ops.SubtractOperator()
			multOp = ops.MultiplyOperator()
			divOp = ops.DivideOperator()

			stack.pushOperator(multOp)
			stack.pushOperator(divOp)
			stack.pushOperator(subOp)
			stack.pushOperator(addOp)

			_logic = logic.ExpressionStackLogic()
			if not _logic.isTopOperatorStackLowerPrecedence(stack, multOp):
				return "Top operator on stack should be lower precedence than multiply  operator"

			stack.popOperator()
	
			if not _logic.isTopOperatorStackLowerPrecedence(stack, addOp):
				return "Top operator on stack should be higher precedence than add operator"

			stack.popOperator()
	
			if _logic.isTopOperatorStackLowerPrecedence(stack, addOp):
				return "Top operator on stack should be higher precedence than add operator"

			stack.popOperator()
	
			if not _logic.isTopOperatorStackLowerPrecedence(stack, divOp):
				return "Top operator on stack %s should be lower precedence than div operator" % str(stack.peekOperator())

			stack.popOperator()
			if not stack.isOperatorStackEmpty():
				return "Operator stack should be empty"
			

			
										

		return utils.Test("Test that we can check correct precedence of operators on stack", f)
			
	tester.addTest(testCanCheckPrecedenceOfOperatorsOnStack())			
	tester.perform()


	

def main():
	testExpressionStackOperations()


	
