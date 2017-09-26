import expressionstacklogic as logic
import expressionstack as stack
import Parsers
import utils
import StringStream as strStr

def createTest(expression, expectedResult):

	testName = "Evaluating expression %s. Expecting result to be %d " % (expression, expectedResult)
	
	def f():      
		return "This test fails"
		# stream = strStr.StringStream(expression)


		# _logic = logic.ExpressionStackLogic()
		# _stack = stack.ExpressionStack()
		# _numberParser = Parsers.NumberParser()
		# _operatorParser = Parsers.OperatorParser()

		# _expressionParser = logic.ExpressionParser(_stack, _logic, _numberParser, _operatorParser)

		# result = _expressionParser.parse(stream)
		# if not result == expectedResult:
		# 	return "Result is: %s" % str(result)

	return utils.Test(testName, f)


def main():
	tester = utils.Tester("Expression tests")

	test1 = createTest("1+1", 2)


	for t in [test1]:
		tester.addTest(t)

	tester.perform()
