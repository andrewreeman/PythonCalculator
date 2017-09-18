from ExpressionEvaluator import *
from termcolor import colored

def PrintTestResult(success):
	if success:
		print colored('Pass', 'green')
	else:
		print colored('Fail', 'red')

def Test(expression, expectedResult):
	print "\nEvaluating expression %s. Expecting result to be %d " % (expression, expectedResult)

	result = evaluate(expression)
	print "Result is %d" % result
	
	PrintTestResult( result == expectedResult )


Test("1+1*2/2-1", 1)
Test("3+2*4", 11)
Test("3+12/3*5", 23)
Test("7-4*8+3-4/2", -24)



	
