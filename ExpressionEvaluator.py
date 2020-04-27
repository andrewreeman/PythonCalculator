from StringStream import StringStream
from Parsers import *
import expressions

def evaluate(expressionString):
	stream = StringStream(expressionString)
	return consume(stream)

def consume(stream):	
	numberParser = NumberParser()
	operatorParser = OperatorParser()
	binaryOperandConsumer = BinaryOperandConsumer( numberParser, operatorParser )
	expressionConsumer = ExpressionConsumer(binaryOperandConsumer)		
	return expressionConsumer.consume(stream).evaluate() 


class ExpressionConsumer:
	def __init__(self, binaryOperandConsumer): 
		self.__binaryOperandConsumer = binaryOperandConsumer
	
	def consume(self, stream):		
		result = self.__binaryOperandConsumer.consume(stream)	

		while stream.hasChars():		
			nextResult = self.__binaryOperandConsumer.consume(stream)	
			if not nextResult: break
			else: result = nextResult			
		return result
	
class BinaryOperandConsumer:
	def __init__(self, numberConsumer, operatorConsumer):
		self.__numberConsumer = numberConsumer
		self.__operatorConsumer = operatorConsumer
		pass
	
	def consume(self, stream):
		# if next token is an operator then left operand is set to previous expression
		operator = self.__operatorConsumer.parse(stream)
		
		# if not then it must be a number and we have a complete expression such as 2+2 or 3*476
		if not operator:			
			operandA = self.__numberConsumer.parse(stream)
			operator = self.__operatorConsumer.parse(stream)
			
			if operator == False:
				return False		

			operandB = self.__numberConsumer.parse(stream)
				
			if operandB == False:
				return False
		
			self.__previousExpression = expressions.BinaryOperandExpression(operandA, operator, operandB)			
			return self.__previousExpression
		# if next token is an operator then we must chain to a previous expression
		else:				
			operandA = self.__previousExpression	
			if operandA == False:		
				return False
			
			operandB = self.__numberConsumer.parse(stream)
				
			if operandB == False:
				return False
		
			self.__previousExpression = expressions.BinaryOperandExpression(operandA, operator, operandB)			
			return self.__previousExpression


	# def __isSingleDigitNum(self, char):
	# 	return char in string.digits
	
	# def __isNegativeSign(self, char):
	# 	result = char == '-'
	# 	return result



