
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
	
	def peekOperator(self):
		if self.__operatorStack:
			return self.__operatorStack[-1]
		else:
			return None

	def popNumber(self):
		if self.__numberStack:
			return self.__numberStack.pop()

	def isOperatorStackEmpty(self):
		return self.operatorStackSize() == 0
	
	def isNumberStackEmpty(self):
		return self.numberStackSize() == 0

	def numberStackSize(self):
		return len(self.__numberStack)

	def operatorStackSize(self):
		return len(self.__operatorStack)

	def __str__(self):
		description = "Stack contents\n\tNumber stack: \n"

		for n in reversed(self.__numberStack):
			description += "\t%s\n" % str(n)

		description += "\n\tOperator stack: \n"

		for o in reversed(self.__operatorStack):
			description += "\t%s\n" % str(o)



		return description


