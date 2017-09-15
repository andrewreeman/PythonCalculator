from StringStream import StringStream
import string

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
		print result

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
		print "Checking operator"	
		operator = self.__operatorConsumer.consume(stream)
		if not operator:
			print "Is not operator. Checking is number"
			operandA = self.__numberConsumer.consume(stream)		
		else:
			print "Is operator"			
			operandA = self.__previousExpression
		
		if operandA == False:
			print "Is not number"
			return False
		if not operator:
			operator = self.__operatorConsumer.consume(stream)
		if operator == False:
			return False
		
		operandB = self.__numberConsumer.consume(stream)
		
		if operandB == False:
			return False
		
		self.__previousExpression = BinaryOperandExpression(operandA, operator, operandB)	
		print "Consumed"
		return self.__previousExpression

	def __isSingleDigitNum(self, char):
		return char in string.digits
	
	def __isNegativeSign(self, char):
		result = char == '-'
		return result

class OperatorConsumer:
	def __init__(self):
		pass
	
	def consume(self, stream):
		if not self.__canConsume(stream):
			return False
		token = stream.next()

		if token == '+':
			return AddOperand()
		elif token == '-':
			return SubtractOperand()
		elif token == '*':
			return MultiplyOperand()
		elif token == '/':
			return DivideOperand()
		

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

		print isNegative
		numberToken = self.__consumeNumber(stream)		
		return NumberExpression(numberToken, isNegative)
	

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

class BinaryOperandExpression:
	def __init__(self, operandA, operator, operandB):
		self.__operandA = operandA
		self.__operator = operator
		self.__operandB = operandB

	def setLeftOperand(self, evaluatable):
		self.__operandA = evaluatable

	def evaluate(self):
		return self.__operator.evaluate()(self.__operandA.evaluate(),self.__operandB.evaluate())

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

class AddOperand:
	def __init__(self): pass
	
	def evaluate(self):
		return lambda a, b: a + b 	


class SubtractOperand:
	def evaluate(self):
		return lambda a, b: a - b

class MultiplyOperand:
	def evaluate(self):
		return lambda a,b: a * b
class DivideOperand:
	def evaluate(self):
		return lambda a,b: 0 if b == 0 else a/b


evaluate("1+1*2/2-1")
	




