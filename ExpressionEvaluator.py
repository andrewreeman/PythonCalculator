from StringStream import StringStream
import string

def evaluate(expressionString):
	print "Evaluating expression %s " % expressionString
	
	stream = StringStream(expressionString)
	consume(stream)

def consume(stream):
	numberConsumer = NumberConsumer()
	operandConsumer = OperandConsumer()
	binaryOperandConsumer = BinaryOperandConsumer( numberConsumer, operandConsumer )

	if binaryOperandConsumer.canConsume(stream):
		binaryOperandConsumer.consume(stream)


class BinaryOperandConsumer:
	def __init__(self, numberConsumer, operandConsumer):
		self.__numberConsumer = numberConsumer
		self.__operandConsumer = operandConsumer
		pass

	def canConsume(self, stream):
		return self.__numberConsumer.canConsume(stream)
	
	def consume(self, stream):
		operandA = self.__numberConsumer.consume(stream)
		
		
		pass

	def __isSingleDigitNum(self, char):
		return char in string.digits
	
	def __isNegativeSign(self, char):
		result = char == '-'
		print(char)
		print(result)
		return result

class OperandConsumer:
	def __init__(self):
		pass
	
	def canConsumer(self, stream):
		token = stream.peek()
		return self.__isOperator(token)
	
	def __isOperator(self, token):
		return token == '+' or token == '-' or token == '*' or token == '/' or token == '^' or token == '%'
	

class NumberConsumer:
	def __init__(self):
		pass

	def canConsume(self, stream):
		token = stream.peek()	
		return self.__isSingleDigitNum(token) or self.__isNegativeSign(token)
	
	def consume(self, stream):
		token = stream.next()	
		isNegative = self.__isNegativeSign(token)		
		
		if not isNegative:
			return NumberExpression(token, False)
		else:
			token = stream.next()
			return NumberExpression(token, True)
		


	def __isSingleDigitNum(self, char):
		return char in string.digits
	
	def __isNegativeSign(self, char):
		result = char == '-'
		print(char)
		print(result)
		return result

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
	
	



evaluate("-2+1")
	




