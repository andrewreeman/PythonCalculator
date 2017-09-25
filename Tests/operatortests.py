import utils
import operators

def testOperatorPrecedence():
	tester = utils.Tester("Operator precedence tests")

	add = operators.AddOperator()
	subtract = operators.SubtractOperator()
	multiply = operators.MultiplyOperator()
	divide = operators.DivideOperator()
	
	def testThatSubtractHasLowestPrecedence():
		def f():		
			if add.isLowerPrecedenceThan(subtract):
				return "Add has lower precedence than subtract" 
	
			if multiply.isLowerPrecedenceThan(subtract):
				return "Multiply has lower precedence than subtract"

			if divide.isLowerPrecedenceThan(subtract):
				return "Divide has lower precedence than subtract"

		return utils.Test("Test that subtract has the lowest precedence", f)
		
	tester.addTest(testThatSubtractHasLowestPrecedence())	

		
	tester.perform()


	

def main():
	testOperatorPrecedence()


	
