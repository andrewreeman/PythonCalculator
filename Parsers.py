import string

from Operators import *
import expressions

class OperatorConsumer:
	def __init__(self):
		pass
	
	def consume(self, stream):
		if not self.__canConsume(stream):
			return False
		token = stream.next()

		if token == '+':
			return AddOperator()
		elif token == '-':
			return SubtractOperator()
		elif token == '*':
			return MultiplyOperator()
		elif token == '/':
			return DivideOperator()
		

	def __canConsume(self, stream):
		token = stream.peek()
		return self.__isOperator(token)
	
	def __isOperator(self, token):
		return token == '+' or token == '-' or token == '*' or token == '/' or token == '^' or token == '%'
	

class NumberConsumer:
	def __init__(self):
		pass

	def consume(self, stream):
		if not self.__canConsume(stream):
			return False

		token = stream.peek()	
		isNegative = self.__isNegativeSign(token)		
		
		if isNegative:
			stream.next()
		
		numberToken = self.__consumeNumber(stream)		
		return expressions.NumberExpression(numberToken, isNegative)
	

	def __consumeNumber(self, stream):

		if not self.__canConsumeDigit(stream):
			return False
		token = stream.next()
		while self.__canConsumeDigit(stream):
			token += stream.next()
		return token
		
				
	def __canConsume(self, stream):
		token = stream.peek()	
		return self.__isSingleDigitNum(token) or self.__isNegativeSign(token)
	def __canConsumeDigit(self, stream):
		token = stream.peek()
		return self.__isSingleDigitNum(token)
		
	def __isSingleDigitNum(self, char):
		if char == "": return False
		return char in string.digits
	
	def __isNegativeSign(self, char):
		result = char == '-'
		return result


