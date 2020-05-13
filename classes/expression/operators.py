class AddOperator:
	def evaluate(self):				
		return lambda a, b: a + b

	def precedence(self):
		return 0

	def isLowerPrecedenceThan(self, operator):
		return isOperatorLowerPrecedenceThanOtherOperator(self, operator)

	def isSamePrecedenceAs(self, operator):
		return isSamePrecedenceAs(self, operator)

	def __str__(self):
		return "+"


class SubtractOperator:
	def evaluate(self):
		return lambda a, b: a - b

	def precedence(self):
		return 0

	def isLowerPrecedenceThan(self, operator):
		return isOperatorLowerPrecedenceThanOtherOperator(self, operator)
	
	def isSamePrecedenceAs(self, operator):
		return isSamePrecedenceAs(self, operator)
	
	def __str__(self):
		return "-"

class MultiplyOperator:
	def evaluate(self):
		return lambda a,b: a * b

	def precedence(self):
		return 1

	def isLowerPrecedenceThan(self, operator):
		return isOperatorLowerPrecedenceThanOtherOperator(self, operator)
	
	def isSamePrecedenceAs(self, operator):
		return isSamePrecedenceAs(self, operator)
	
	def __str__(self):
		return "*"

class DivideOperator:
	def evaluate(self):
		return lambda a,b: 0 if b == 0 else a/b	

	def precedence(self):
		return 1

	def isLowerPrecedenceThan(self, operator):
		return isOperatorLowerPrecedenceThanOtherOperator(self, operator)
	
	def isSamePrecedenceAs(self, operator):
		return isSamePrecedenceAs(self, operator)
	
	def __str__(self):
		return "/"

def isSamePrecedenceAs(operatorA, operatorB):
	return operatorA.precedence() == operatorB.precedence()

def isOperatorLowerPrecedenceThanOtherOperator(operatorA, operatorB):
	result = operatorA.precedence() < operatorB.precedence()
	return result
