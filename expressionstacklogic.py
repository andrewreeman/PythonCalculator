import expressions

class ExpressionParser:
	def __init__(self, expressionStack, expressionStackLogic, numberParser, operatorParser):
		self.__numberParser = numberParser
		self.__operatorParser = operatorParser
		self.__stack = expressionStack
		self.__logic = expressionStackLogic

	
	def parse(self, stream):

		while stream.hasItems():
			numberToken = self.__numberParser.parse(stream)

			if numberToken:	
				self.__stack.pushNumber(numberToken)

			operatorToken = self.__operatorParser.parse(stream)

			if operatorToken:
				if self.__stack.isOperatorStackEmpty():
					self.__stack.pushOperator(operatorToken)
				else:
					if self.__logic.isTopOperatorStackLowerPrecedence(self.__stack, operator):
						self.__stack.pushOperator(operator)

					while not self.__stack.isOperatorStackEmpty:	
						self.__createNodeFromStack()

		self.__createNodeFromStack()

	def __createNodeFromStack(self, tree = None, orphan = None):
		logic = self.__logic
		stack = self.__stack

		if not tree:
			logic.setIsPoppingStack(False) #todo: if popping stack state just depends on an existence of a tree then just use that instead
		
		if stack.isOperatorStackEmpty():
			return tree

		elif orphan:
			rootNode = logic.popOperatorAndJoinNodes(tree, orphan
			return self.__createNodeFromStack(rootNode, None)

		elif logic.isNumberStackCountGreaterThanOperatorStackCount(stack):
			logic.setIsPoppingStack(True)
			rootNode = logic.popRootNode(stack)
			return self.__createNodeFromStack(rootNode, None)

		elif logic.areBothStacksSizeOfOneAndCurrentlyPoppingStack(stack):
			rootNode = logic.popJoiningRootNodeToRightOperand(stack, tree)
			return self.__createNodeFromStack(rootNode, None)

		elif logic.areBothStacksSizeOfOneAndCurrentlyNotPoppingStack(stack):
			rootNode = logic.popJoiningRootNodeToLeftOperand(stack, tree)
			return self.__createNodeFromStack(rootNode, None)

		elif logic.areBothStacksEqualSize(stack):
			orphan = logic.popRootNode(stack)
			return self.__createNodeFromStack(rootNode, orphan)
		
											
		
class ExpressionStackLogic:
	def __init__(self):
		self.__isPoppingStack = False

	def setIsPoppingStack(self, isPoppingStack):
		self.__isPoppingStack = isPoppingStack


	def popRootNode(self, expressionStack):
		rightOperand = expressionStack.popNumber()
		leftOperand = expressionStack.popNumber()
		return self.popOperatorAndJoinNodes(expressionStack, leftOperand, rightOperand)

	def popJoiningRootNodeToRightOperand(self, expressionStack, oldRootNode):
		leftOperand = expressionStack.popNumber()
		return self.popOperatorAndJoinNodes(expressionStack, leftOperand, oldRootNode)

	def popJoiningRootNodeToLeftOperand(self, expressionStack, oldRootNode):
		rightOperandNode = expressionStack.popNumber()
		return self.popOperatorAndJoinNodes(expressionStack, oldRootNode, rightOperandNode)

	def popOperatorAndJoinNodes(self, expressionStack, leftNode, rightNode):
		operator = expressionStack.popOperator()
		if operator and leftNode and rightNode:
			return expressions.BinaryOperandExpression(leftNode, operator, rightNode)
	
	def isTopOperatorStackLowerPrecedence(self, expressionStack, operator):
		topOperator = expressionStack.peekOperator()
		if topOperator:
			return topOperator.isLowerPrecedenceThan(operator)
		else:
			return False

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


	


	


