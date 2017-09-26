class BinaryOperandExpression:
	def __init__(self, operandA, operator, operandB):
		self.__operandA = operandA
		self.__operator = operator
		self.__operandB = operandB

	def setLeftOperand(self, evaluatable):
		self.__operandA = evaluatable

	def leftOperand(self):
		return self.__operandA 

	def rightOperand(self):
		return self.__operandB

	def operator(self):
		return self.__operator

	def evaluate(self):
		return self.__operator.evaluate()(self.__operandA.evaluate(),self.__operandB.evaluate())

	def isOtherLowerPrecedence(self, other):
		return other.__operator.precedence < self.__operator.precedence

	def __str__(self):
		description = "Operand A: " + str(self.leftOperand())
		description += "\nOperand B: " + str(self.rightOperand())
		description += "\nOperator: " + str(self.operator())
		return description

class NumberExpression:
	def __init__(self, char, isNegative):
		self.__char = char
		self.__isNegative = isNegative

	def evaluate(self):
		number = int(self.__char)
		if self.__isNegative:
			return -number
		else:
			return number
