import expressions
import pdb
import StringStream as strStr
import expressionstack as expStack

class ExpressionParser:
	def __init__(self, expressionStack, expressionStackLogic, numberParser, operatorParser):
		self.__numberParser = numberParser
		self.__operatorParser = operatorParser
		self.__stack = expressionStack
		self.__logic = expressionStackLogic


	def parse(self, stream):		
		tree = None		

	 	#pdb.set_trace()
		while stream.hasChars() and not stream.peek() == ')':	
			print "I am looping baby"		
			if not self.__numberParser.canConsume(stream) and not self.__operatorParser.canConsume(stream) and not stream.peek() == '(':
				stream.next()
				continue
						
			numberToken = self.__numberParser.parse(stream)

			if numberToken:				
				self.__stack.pushNumber(numberToken)		

			operatorToken = self.__operatorParser.parse(stream)

			if operatorToken:				
				if self.__stack.isOperatorStackEmpty():
					self.__stack.pushOperator(operatorToken)
				else:
					if self.__logic.isTopOperatorStackLowerPrecedence(self.__stack, operatorToken):
						self.__stack.pushOperator(operatorToken)
					else:
						while not self.__stack.isOperatorStackEmpty():							
							tree = self.__createNodeFromStack(0, tree)							
						self.__stack.pushOperator(operatorToken)

			#todo: this is ugly code. we should be abstracting this all into a bracket parser!
			if stream.peek() == '(':
				stream.next()
				newStack = expStack.ExpressionStack()
				bracketTree = ExpressionParser(newStack, self.__logic, self.__numberParser, self.__operatorParser).parse(stream)
				
				numberResult = bracketTree.evaluate()
				tempStream = strStr.StringStream("%d" % numberResult)
				numberToken = self.__numberParser.parse(tempStream)				
				self.__stack.pushNumber(numberToken)		
				if stream.peek() == ')':
					stream.next()
		

		return self.__createNodeFromStack(0, tree)

	def __createNodeFromStack(self, depth, tree = None, orphan = None):
		#print "\nCreate node from stack called with tree: %s" % tree		
		print "__createNodeFromStack is called with"
		print tree
		logic = self.__logic		
		stack = self.__stack
		#print stack

		if depth == 0:
			logic.setIsPoppingStack(False) #todo: if popping stack state just depends on an existence of a tree then just use that instead

		#print "Is currently popping stack: %s" % str(logic.isPoppingStack())
		#print "Depth is: %s" % str(depth)

		if stack.isOperatorStackEmpty():
		#	print "Operator stack is empty"
			return tree

		elif orphan:
		#	print "We have an orphan"
			
			rootNode = logic.popOperatorAndJoinNodes(stack, tree, orphan)
			return self.__createNodeFromStack(depth + 1, rootNode)

		elif logic.isNumberStackCountGreaterThanOperatorStackCount(stack):
		#	print "Number stack larger than operator stack"

			logic.setIsPoppingStack(True)
			rootNode = logic.popRootNode(stack)
			return self.__createNodeFromStack(depth + 1, rootNode)

		elif logic.areBothStacksSizeOfOneAndCurrentlyPoppingStack(stack):
		#	print "Both stacks have one and currently popping stack"

			rootNode = logic.popJoiningRootNodeToRightOperand(stack, tree)
			return self.__createNodeFromStack(depth + 1, rootNode)

		elif logic.areBothStacksSizeOfOneAndCurrentlyNotPoppingStack(stack):
		#	print "Both stacks have one and currently not popping stack"

			rootNode = logic.popJoiningRootNodeToLeftOperand(stack, tree)
			return self.__createNodeFromStack(depth + 1, rootNode)

		elif logic.areBothStacksEqualSize(stack):
		#	print "Both stacks are equal size"

			orphan = logic.popRootNode(stack)
			return self.__createNodeFromStack(depth + 1, tree, orphan)

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
		return not self.__isPoppingStack and self.areBothStacksSizeOfOne(expressionStack)

	def areBothStacksSizeOfOne(self, expressionStack):
		return expressionStack.numberStackSize() == 1 and expressionStack.operatorStackSize() == 1
