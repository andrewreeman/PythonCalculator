import Tests.utils as utils
from classes.expression.operators import *

def testOperatorPrecedence():
	tester = utils.Tester("Operator precedence tests")

	add = AddOperator()
	subtract = SubtractOperator()
	multiply = MultiplyOperator()
	divide = DivideOperator()
	
	def testThatSubtractHasLowestPrecedence():
		def f():		
			if add.is_lower_precedence_than(subtract):
				return "Add has lower precedence than subtract" 
	
			if multiply.is_lower_precedence_than(subtract):
				return "Multiply has lower precedence than subtract"

			if divide.is_lower_precedence_than(subtract):
				return "Divide has lower precedence than subtract"

		return utils.Test("Test that subtract has the lowest precedence", f)
		
	tester.addTest(testThatSubtractHasLowestPrecedence())	

		
	tester.perform()


	

def main():
	testOperatorPrecedence()


	
