from .operators import SubtractOperator

class BinaryOperandExpression:
	def __init__(self, operandA, operator, operandB):
		self._operandA = operandA
		self._operator = operator
		self._operandB = operandB	
	
	def evaluate(self):
		return self._operator.evaluate()(self._operandA.evaluate(),self._operandB.evaluate())	

	def __str__(self):
		return f"({str(self._operandA)} {str(self._operator)} {str(self._operandB)})"		

class NumberExpression:	
	def __init__(self, char, isNegative):
		self._char = char
		self._isNegative = isNegative		

	def evaluate(self):
		number = float(self._char)
		if self._isNegative:
			return -number
		else:
			return number

	def __str__(self):
		return str(self.evaluate())
