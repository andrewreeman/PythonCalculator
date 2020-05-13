from classes.expression.operators import Operator

class Expression:
	def evaluate(self) -> float:
		raise NotImplementedError()	

class BinaryOperandExpression(Expression):
	def __init__(self, operandA: Expression, operator: Operator, operandB: Expression):
		self._operandA: Expression = operandA
		self._operator: Operator = operator
		self._operandB: Expression = operandB	
	
	def evaluate(self) -> float:
		return self._operator.operation()(self._operandA.evaluate(),self._operandB.evaluate())	

	def __str__(self):
		return f"({str(self._operandA)} {str(self._operator)} {str(self._operandB)})"		

class NumberExpression(Expression):	
	def __init__(self, char: str, isNegative: bool):
		self._char: str = char
		self._isNegative: bool = isNegative		

	def evaluate(self) -> float:
		number = float(self._char)
		if self._isNegative:
			return -number
		else:
			return number

	def __str__(self):
		return str(self.evaluate())
