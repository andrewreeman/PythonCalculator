import expressionstacklogic as logic
import expressionstack as stack
import Parsers
import Tests.utils as utils
import StringStream as strStr

def createTest(expression, expectedResult):

	testName = "Evaluating expression %s. Expecting result to be %d " % (expression, expectedResult)
	
	def f():      
		
		stream = strStr.StringStream(expression)


		_logic = logic.ExpressionStackLogic()
		_stack = stack.ExpressionStack()
		_numberParser = Parsers.NumberParser()
		_operatorParser = Parsers.OperatorParser()

		_expressionParser = logic.ExpressionParser(_stack, _logic, _numberParser, _operatorParser)
		
		result = _expressionParser.parse(stream)
		if not result.evaluate() == expectedResult:
			return "Result is: %s. \n object is: %s" % (str(result.evaluate()), str(result))


	return utils.Test(testName, f)


def main():
	tester = utils.Tester("Expression tests")

	tests = list()
	def addTest(test, expected):
		tests.append(createTest(test, expected))	

	addTest("1+1", 2)
	addTest("3+2*4", 11)
	addTest("10-10/5+3", 11)
	addTest("7-4*8+3-4/2", -24)
	addTest("3+(2+5)*4", 31)
	addTest("(7-8)*(2-(4+3)*8)", 54)
	addTest("1-8", -7)
	addTest("1-1", 0)		
	addTest("(10+0)-2", 8)
	addTest("(10+0)", 10)
	addTest("10+0", 10)		
	addTest("10", 10)
	addTest("(10)", 10)		
	addTest("2-(3*2)+10", 6)
	addTest("3+(2+5)-4", 6)
	addTest("(10+(3*2))", 16) 	
	addTest("(10+(3*2))-2", 14) 		
	addTest("10-10/5+3", 11)	
	addTest("10 - 10", 0)
	addTest("10 - 10 / 5 + 3", 11)
	addTest("-1", -1)
	addTest("-0", -0)
	addTest("(-0)", -0)

	for t in tests:
		tester.addTest(t)

	tester.perform()
