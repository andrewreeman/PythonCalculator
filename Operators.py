class AddOperator:
	def evaluate(self):
		return lambda a, b: a + b 

	def precedence(self):
		return 1


class SubtractOperator:
	def evaluate(self):
		return lambda a, b: a - b

	def precedence(self):
		return 0

class MultiplyOperator:
	def evaluate(self):
		return lambda a,b: a * b

	def precedence(self):
		return 2

class DivideOperator:
	def evaluate(self):
		return lambda a,b: 0 if b == 0 else a/b	

	def precedence(self):
		return 3
