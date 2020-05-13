from typing import Optional

import expressionstacklogic as logic
import expressionstack as stack
import classes.parser.Parsers as Parsers
from classes.parser.operator import OperatorParser
import Tests.utils as utils

from classes.string_stream import StringStream


import expression_parser

def createTest(expression, expectedResult):

	testName = "Evaluating expression %s. Expecting result to be %d " % (expression, expectedResult)
	
	def f():      
		
		stream = StringStream(expression)


		_logic = logic.ExpressionStackLogic()
		_stack = stack.ExpressionStack()
		_numberParser = Parsers.NumberParser()
		_operatorParser = OperatorParser()

		_expressionParser = expression_parser.ExpressionParser(_stack, _logic, _numberParser, _operatorParser)
		
		result = _expressionParser.parse(stream)
		if not result.evaluate() == expectedResult:
			return "Result is: %s. \n object is: %s" % (str(result.evaluate()), str(result))


	return utils.Test(testName, f)


def main(_tester: Optional[utils.Tester] = None):
	tester = _tester or utils.Tester("Expression parsing tests")
	
	def addTest(test, expected):
		tester.addTest(createTest(test, expected))		
	
	def justTest(test, expected):
		tester.justTest(createTest(test, expected))

	addTest("1+1", 2)
	addTest("3+2*4", 11)
	addTest("10-10/5+3", 11)

	addTest("7-4*8+3-4/2", -24)
	addTest("7-4*8+3-4", -26)

	addTest("7-4*8-4", -29)
	addTest("7-4*8+3", -22)

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
	addTest("10-10", 0)
	addTest("10 - 10", 0)
	addTest("10-10/5+3", 11)
	addTest("10 - 10 / 5 + 3", 11)
	addTest("-1", -1)
	addTest("-0", -0)
	addTest("(-0)", -0)		
	addTest("2-(6)+10", 6)		
	addTest("-4+10", 6)
	addTest("2-6+0", -4)		
	addTest("2-6+10", 6)
	addTest("1*2/2", 1)	
	addTest("1*8/4", 2)			
	addTest("1+2/2", 2)			
	addTest("1+1*2/2-1", 1)			
	addTest("1+1*2/2", 2)					
	addTest("1+2/2", 2)	# '(1 + (2 / 2))' is correct grouping	
	addTest("3+12/3*5", 23)	

	if _tester is None:
		tester.perform()
