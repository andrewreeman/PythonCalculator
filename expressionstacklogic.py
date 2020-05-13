import classes.expressions as expressions
import pdb

from classes.string_stream import StringStream as strStr



from operators import AddOperator
from expressionstack import ExpressionStack
from classes.expressions import NumberExpression
from Parsers import NumberParser
from Parsers import OperatorParser

class ExpressionStackLogic:
	def __init__(self):
		self.__isPoppingStack = False

	def setIsPoppingStack(self, isPoppingStack):
		self.__isPoppingStack = isPoppingStack

	def isPoppingStack(self):
		return self.__isPoppingStack

	def popRootNode(self, expressionStack):
		rightOperand = expressionStack.popNumber()
		leftOperand = expressionStack.popNumber()
		return self.popOperatorAndJoinNodes(expressionStack, leftOperand, rightOperand)
	
	def popSingleNumberAddition(self, expressionStack, oldRootNode):
		number = expressionStack.popNumber()
		_oldRootNode = oldRootNode or NumberExpression('0', False)
		return expressions.BinaryOperandExpression(_oldRootNode, AddOperator(), number)
		

	def popJoiningRootNodeToRightOperand(self, expressionStack, oldRootNode):
		leftOperand = expressionStack.popNumber()
		return self.popOperatorAndJoinNodes(expressionStack, leftOperand, oldRootNode)

	def popJoiningRootNodeToLeftOperand(self, expressionStack, oldRootNode):
		rightOperandNode = expressionStack.popNumber()
		return self.popOperatorAndJoinNodes(expressionStack, oldRootNode, rightOperandNode)

	def popOperatorAndJoinNodes(self, expressionStack, leftNode, rightNode):
		operator = expressionStack.popOperator()
		if leftNode == None:
			leftNode = NumberExpression('0', False)
		if operator and leftNode and rightNode:
			return expressions.BinaryOperandExpression(leftNode, operator, rightNode)
	
	def isTopOperatorStackLowerPrecedence(self, expressionStack: ExpressionStack, operator):		
		topOperator = expressionStack.peekOperator()
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

	def areBothStacksEqualSize(self, expressionStack):
		return expressionStack.numberStackSize() == expressionStack.operatorStackSize()

	def areBothStacksSizeOfOneAndCurrentlyPoppingStack(self, expressionStack):
		return self.__isPoppingStack and self.areBothStacksSizeOfOne(expressionStack)

	def areBothStacksSizeOfOneAndCurrentlyNotPoppingStack(self, expressionStack):
		return not self.__isPoppingStack and self.areBothStacksSizeOfOne(expressionStack)

	def areBothStacksSizeOfOne(self, expressionStack):
		return expressionStack.numberStackSize() == 1 and expressionStack.operatorStackSize() == 1
