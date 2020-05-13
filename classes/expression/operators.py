class AddOperator:
	def evaluate(self):				
		return lambda a, b: a + b

	def precedence(self):
		return 0

	def is_lower_precedence_than(self, operator):
		return is_operator_lower_precedence_than_other_operator(self, operator)

	def is_same_precedence_as(self, operator):
		return is_same_precedence_as(self, operator)

	def __str__(self):
		return "+"


class SubtractOperator:
	def evaluate(self):
		return lambda a, b: a - b

	def precedence(self):
		return 0

	def is_lower_precedence_than(self, operator):
		return is_operator_lower_precedence_than_other_operator(self, operator)
	
	def is_same_precedence_as(self, operator):
		return is_same_precedence_as(self, operator)
	
	def __str__(self):
		return "-"

class MultiplyOperator:
	def evaluate(self):
		return lambda a,b: a * b

	def precedence(self):
		return 1

	def is_lower_precedence_than(self, operator):
		return is_operator_lower_precedence_than_other_operator(self, operator)
	
	def is_same_precedence_as(self, operator):
		return is_same_precedence_as(self, operator)
	
	def __str__(self):
		return "*"

class DivideOperator:
	def evaluate(self):
		return lambda a,b: 0 if b == 0 else a/b	

	def precedence(self):
		return 1

	def is_lower_precedence_than(self, operator):
		return is_operator_lower_precedence_than_other_operator(self, operator)
	
	def is_same_precedence_as(self, operator):
		return is_same_precedence_as(self, operator)
	
	def __str__(self):
		return "/"

def is_same_precedence_as(operatorA, operatorB):
	return operatorA.precedence() == operatorB.precedence()

def is_operator_lower_precedence_than_other_operator(operatorA, operatorB):
	result = operatorA.precedence() < operatorB.precedence()
	return result
