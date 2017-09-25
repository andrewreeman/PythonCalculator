from ExpressionEvaluator import *
import expressionstack as espstack
import expressionstacklogic as logic
import utils

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
			stack = espstack.ExpressionStack()
			stack.pushOperator(operatorDummy)	
			stack.pushOperator(operatorDummy2)
			stack.pushOperator(operatorDummy3)

			if not stack.operatorStackSize() == 3:
				return "Operator stack size does not equal 3. Instead it equals: %d" % stack.operatorStackSize()
		return utils.Test("Test that correct operator size is reported", f)	

		
	tester.addTest(testCorrectOperatorSizeReported())	


	def testCanExpressionStackLogicPopCorrectRootNode():
		def f():
			stack = espstack.ExpressionStack()
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
	tester.perform()

	_logic = logic.ExpressionStackLogic()
	

def main():
	testExpressionStackOperations()


	
