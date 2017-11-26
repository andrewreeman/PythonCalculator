import expressionstacklogic as logic
import expressionstack as stack
import Parsers
import utils
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

	# t1 = createTest("1+1", 2)

	# t2 = createTest("3+2*4", 11)
	# t3 = createTest("10-10/5+3", 11)
	# t4 = createTest("7-4*8+3-4/2", -24)
	# t5 = createTest("3+(2+5)*4", 31)
	# t6 = createTest("(7-8)*(2-(4+3)*8)", 54)


	print "Running the 7th test :)"
	t7 = createTest("(10+(3*2))-2", 14) # result is 4
	#t7 = createTest("2-(3*2)+10", 6) # result is -14
	#t7 = createTest("3+(2+5)-4", 6)
	#t3 = createTest("10 - 10 / 5 + 3", 5)

	# for t in [t1, t2, t3, t4, t5, t6, t7]:
	for t in [t7]:
		tester.addTest(t)

	tester.perform()
