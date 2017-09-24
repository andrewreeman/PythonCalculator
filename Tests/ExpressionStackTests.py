from ExpressionEvaluator import *
import ExpressionStack
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
			stack = ExpressionStack.ExpressionStackThing()
			stack.pushOperator(operatorDummy)	
			stack.pushOperator(operatorDummy2)
			stack.pushOperator(operatorDummy3)

			if not stack.operatorStackSize() == 3:
				return "Operator stack size does not equal 3. Instead it equals: %d" % stack.operatorStackSize()
		return utils.Test("Test that correct operator size is reported", f)	

	tester.addTest(testCorrectOperatorSizeReported())	
	tester.perform()
	



def main():
	testExpressionStackOperations()


	
