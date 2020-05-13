import classes.expression.expressions as expressions
import pdb

from classes.string_stream import StringStream as strStr
from classes.expression.operators import AddOperator
from classes.expression.expressions import NumberExpression

from classes.parser.number import NumberParser
from classes.parser.operator import OperatorParser
from classes.parser.stack.stack import ParserStack

class ParserStackQuery:
	def __init__(self, stack: ParserStack):
		self.__isPoppingStack = False
		self._stack: ParserStack = stack

	def setIsPoppingStack(self, isPoppingStack):
		self.__isPoppingStack = isPoppingStack

	def isPoppingStack(self):
		return self.__isPoppingStack

	def isOperatorStackEmpty(self):
		return self._stack.isOperatorStackEmpty()

	def isAwaitingOperator(self):
		return self._stack.numberStackSize() >= self._stack.operatorStackSize() 

	def isTopOperatorStackLowerPrecedence(self, operator):
		topOperator = self._stack.peekOperator()
		if topOperator:
			return topOperator.isLowerPrecedenceThan(operator)
		else:
			return False

	def isTopOperatorStackSamePrecedence(self, operator):
		topOperator = self._stack.peekOperator()
		if topOperator:
			return topOperator.isSamePrecedenceAs(operator)
		else:
			return False

	def isNumberStackCountGreaterThanOperatorStackCount(self):
		return self._stack.numberStackSize() > self._stack.operatorStackSize()

	def areBothStacksEmpty(self):		
		return self._stack.isOperatorStackEmpty() and self._stack.isNumberStackEmpty()

	def areBothStacksEqualSize(self):
		return self._stack.numberStackSize() == self._stack.operatorStackSize()

	def areBothStacksSizeOfOneAndCurrentlyPoppingStack(self):
		return self.__isPoppingStack and self.areBothStacksSizeOfOne()

	def areBothStacksSizeOfOneAndCurrentlyNotPoppingStack(self):
		return not self.__isPoppingStack and self.areBothStacksSizeOfOne()

	def areBothStacksSizeOfOne(self):
		return self._stack.numberStackSize() == 1 and self._stack.operatorStackSize() == 1
