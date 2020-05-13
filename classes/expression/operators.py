from typing import Callable

OperatorEvaluator = Callable[[float, float], float]

class Operator:
	def operation(self) -> OperatorEvaluator:
		raise NotImplementedError()

	def precedence(self) -> int:
		raise NotImplementedError()
	
	def is_lower_precedence_than(self, operator):
		return self.precedence() < operator.precedence()	
	
	def is_same_precedence_as(self, operator):
		return self.precedence() == operator.precedence()	

class AddOperator(Operator):	
	def operation(self) -> OperatorEvaluator:				
		return lambda a, b: a + b

	def precedence(self) -> int:
		return 0		

	def __str__(self):
		return "+"


class SubtractOperator(Operator):
	def operation(self) -> OperatorEvaluator:
		return lambda a, b: a - b

	def precedence(self) -> int:
		return 0			
	
	def __str__(self):
		return "-"

class MultiplyOperator(Operator):
	def operation(self) -> OperatorEvaluator:
		return lambda a,b: a * b

	def precedence(self) -> int:
		return 1			
	
	def __str__(self):
		return "*"

class DivideOperator(Operator):
	def operation(self) -> OperatorEvaluator:
		return lambda a,b: 0 if b == 0 else a/b	

	def precedence(self) -> int:
		return 1		
	
	def __str__(self):
		return "/"
