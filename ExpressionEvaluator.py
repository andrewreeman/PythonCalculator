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

	def chain(self, other):
			
	
	def isOtherLowerPrecedence(self, other):
		return other.__operator.precedence < self.__operator.precedence

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

class AddOperator:
	def __init__(self): pass
	
	def evaluate(self):
		return lambda a, b: a + b 

	def precedence:
		return 1


class SubtractOperator:
	def evaluate(self):
		return lambda a, b: a - b

	def precedence:
		return 0

class MultiplyOperator:
	def evaluate(self):
		return lambda a,b: a * b

	def precedence:
		return 2

class DivideOperator:
	def evaluate(self):
		return lambda a,b: 0 if b == 0 else a/b	

	def precedence:
		return 3


evaluate("1+1*2/2-1")
evaluate("3+2*4")
evaluate("3+12/3*5") #23

3+12
12/3
this should be l:3+r:(12/3)
# 3+12 has a lower precedence than 12/3 so we make the right operand of 3+12 be 12/3 making: 3+(12/3)


3*5
this should be: l:3 + r:(5*(12/3))
# 12/3 has a higher precendece than 3*5 so we swap the operands of ... no this is bullshit

what we should do is simply work out which operand to evaluate first when evaluating depending on precedence...obviously?
and should start evaluatiom from right most expression
	




