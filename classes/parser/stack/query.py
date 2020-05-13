import classes.expression.expressions as expressions
import pdb

from classes.string_stream import StringStream as strStr
from classes.expression.operators import AddOperator
from classes.expression.expressions import NumberExpression

from classes.parser.number import NumberParser
from classes.parser.operator import OperatorParser
from classes.parser.stack.stack import ParserStack

class ParserStackQuery:
	def __init__(self):
		self.__isPoppingStack = False

	def setIsPoppingStack(self, isPoppingStack):
		self.__isPoppingStack = isPoppingStack

	def isPoppingStack(self):
		return self.__isPoppingStack	

	def isTopOperatorStackLowerPrecedence(self, stack, operator):
		topOperator = stack.peekOperator()
		if topOperator:
			return topOperator.isLowerPrecedenceThan(operator)
		else:
			return False

	def isTopOperatorStackSamePrecedence(self, expressionStack, operator):
		topOperator = expressionStack.peekOperator()
		if topOperator:
			return topOperator.isSamePrecedenceAs(operator)
		else:
			return False

	def isNumberStackCountGreaterThanOperatorStackCount(self, expressionStack):
		return expressionStack.numberStackSize() > expressionStack.operatorStackSize()

	def areBothStacksEmpty(self, stack):		
		return stack.isOperatorStackEmpty() and stack.isNumberStackEmpty()

	def areBothStacksEqualSize(self, expressionStack):
		return expressionStack.numberStackSize() == expressionStack.operatorStackSize()

	def areBothStacksSizeOfOneAndCurrentlyPoppingStack(self, expressionStack):
		return self.__isPoppingStack and self.areBothStacksSizeOfOne(expressionStack)

	def areBothStacksSizeOfOneAndCurrentlyNotPoppingStack(self, expressionStack):
		return not self.__isPoppingStack and self.areBothStacksSizeOfOne(expressionStack)

	def areBothStacksSizeOfOne(self, expressionStack):
		return expressionStack.numberStackSize() == 1 and expressionStack.operatorStackSize() == 1
