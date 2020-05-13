from ..expression.operators import *

class OperatorParser:
	def __init__(self):
		pass
	
	def parse(self, stream):
		if not self.__canConsume(stream):
			return False
		
		token: str = stream.next()

		if token == '+':
			return AddOperator()
		elif token == '-':
			return SubtractOperator()
		elif token == '*':
			return MultiplyOperator()
		elif token == '/':
			return DivideOperator()
		elif token.isspace():
			return parse(self, stream)
		

	def canConsume(self, stream):
		return self.__canConsume(stream)		

	def __canConsume(self, stream):
		token = stream.peek()
		return self.__isOperator(token)
	
	def __isOperator(self, token):
		return token == '+' or token == '-' or token == '*' or token == '/' or token == '^' or token == '%'
	
