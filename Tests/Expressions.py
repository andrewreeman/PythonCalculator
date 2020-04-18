from ExpressionEvaluator import *
import Tests.utils


def createTest(expression, expectedResult):

	testName = "Evaluating expression %s. Expecting result to be %d " % (expression, expectedResult)

	def f():
		result = evaluate(expression)
		if not result == expectedResult:
			return "Result is: %s" % str(result)

	return utils.Test(testName, f)


def main():
	tester = utils.Tester("Expression tests")

	test1 = createTest("1+1*2/2-1", 1)
	test2 = createTest("3+2*4", 11)
	test3 = createTest("3+12/3*5", 23)
	test4 = createTest("7-4*8+3-4/2", -24)


	for t in [test1, test2, test3, test4]:
		tester.addTest(t)

	tester.perform()
