from StringStream import StringStream
from Parsers import *

def evaluate(expressionString):
	print "Evaluating expression %s " % expressionString
	
	stream = StringStream(expressionString)
	consume(stream)

def consume(stream):
	numberConsumer = NumberConsumer()
	operatorConsumer = OperatorConsumer()
	binaryOperandConsumer = BinaryOperandConsumer( numberConsumer, operatorConsumer )
	expressionConsumer = ExpressionConsumer(binaryOperandConsumer)	
	
	print( expressionConsumer.consume(stream).evaluate() )


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
		# is next token is an operator then left operand is set to previous expression
		operator = self.__operatorConsumer.consume(stream)
		
		# if not then it must be a number and we have a complete expression such as 2+2 or 3*476
		if not operator:			
			operandA = self.__numberConsumer.consume(stream)
			operator = self.__operatorConsumer.consume(stream)
			
			if operator == False:
				return False		

			operandB = self.__numberConsumer.consume(stream)
				
			if operandB == False:
				return False
		
			self.__previousExpression = BinaryOperandExpression(operandA, operator, operandB)			
			return self.__previousExpression
		# if next token is an operator then we must chain to a previous expression
		else:				
			operandA = self.__previousExpression	
			if operandA == False:		
				return False
			
			operandB = self.__numberConsumer.consume(stream)
				
			if operandB == False:
				return False
		
			self.__previousExpression = BinaryOperandExpression(operandA, operator, operandB)			
			return self.__previousExpression


	def __isSingleDigitNum(self, char):
		return char in string.digits
	
	def __isNegativeSign(self, char):
		result = char == '-'
		return result



