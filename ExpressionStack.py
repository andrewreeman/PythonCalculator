import Expressions


class ExpressionStackLogic:
	def __init__(self):
		self.__isPoppingStack = False

	def setIsPoppingStack(self, isPoppingStack):
		self.__isPoppingStack = isPoppingStack


	def popRootNode(self, expressionStack):
		rightOperand = expressionStack.popNumber()
		leftOperand = expressionStack.popNumber()
		return self.popOperatorAndJoinNodes(expressionStack, leftOperand, rightOperandNode)

	def popJoiningRootNodeToRightOperand(self, expressionStack, oldRootNode):
		leftOperand = expressionStack.popNumber()
		return self.popOperatorAndJoinNodes(expressionStack, leftOperand, oldRootNode)

	def popJoiningRootNodeToLeftOperand(self, expressionStack, oldRootNode):
		rightOperandNode = expressionStack.popNumber()
		return self.popOperatorAndJoinNodes(expressionStack, oldRootNode, rightOperandNode)

	def popOperatorAndJoinNodes(self, expressionStack, leftNode, rightNode):
		operator = expressionStack.popOperator()

		if operator and leftNode and rightNode:
			return BinaryOperandExpression(leftNode, operator, rightNode)

	def isNumberStackCountGreaterThanOperatorStackCount(self, expressionStack):
		return expressionStack.numberStackSize() > expressionStack.operatorStackSize()

	def areBothStacksEqualSize(self, expressionStack):
		return expressionStack.numberStackSize() == expressionStack.operatorStackSize()
	
	def areBothStacksSizeOfOneAndCurrentlyPoppingStack(self, expressionStack):
		return self.__isPoppingStack and self.areBothStacksSizeOfOne(expressionStack)
	
	def areBothStacksSizeOfOneAndCurrentlyNotPoppingStack(self, expressionStack):
		return not self.__isPoppingStack and self.areBothStacksSizeOfOne()

	def areBothStacksSizeOfOne(self, expressionStack):
		return expressionStack.numberStackSize() == 1 and expressionStack.operatorStackSize() == 1
	
	
			
		

class ExpressionStack:
	def __init__(self): 
		self.__operatorStack = list()
		self.__numberStack = list()

	def pushOperator(self, operator):
		self.__operatorStack.append( operator )

	def pushNumber(self, number):	
		self.__numberStack.append( number )

	def popOperator(self):
		if self.__operatorStack:
			return self.__operatorStack.pop()

	def popNumber(self, number):
		if self.__numberStack:
			return self.python __numberStack.pop()

	def numberStackSize(self):
		return len(self.__numberStack)

	def operatorStackSize(self):
		return len(self.__operatorStack)

	


	


