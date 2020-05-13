from classes.parser.stack.stack import ParserStack


class ParserStackQuery:
    """This class is used for querying the state of a ParserStack
    """
    
    def __init__(self, stack: ParserStack):
        self.__isPoppingStack = False
        self._stack: ParserStack = stack

    def setIsPoppingStack(self, isPoppingStack):
        self.__isPoppingStack = isPoppingStack

    def isPoppingStack(self):
        return self.__isPoppingStack

    def isOperatorStackEmpty(self):
        return self._stack.operator_stack_size() == 0
    
    def is_number_stack_empty(self) -> bool:
        return self._stack.expression_stack_size() == 0

    def isAwaitingOperator(self):
        return self._stack.expression_stack_size() >= self._stack.operator_stack_size()

    def isTopOperatorStackLowerPrecedence(self, operator):
        topOperator = self._stack.peek_operator()
        if topOperator:
            return topOperator.is_lower_precedence_than(operator)
        else:
            return False

    def isTopOperatorStackSamePrecedence(self, operator):
        topOperator = self._stack.peek_operator()
        if topOperator:
            return topOperator.is_same_precedence_as(operator)
        else:
            return False

    def isNumberStackCountGreaterThanOperatorStackCount(self):
        return self._stack.expression_stack_size() > self._stack.operator_stack_size()

    def areBothStacksEmpty(self):
        return self.isOperatorStackEmpty() and self.is_number_stack_empty()

    def areBothStacksEqualSize(self):
        return self._stack.expression_stack_size() == self._stack.operator_stack_size()

    def areBothStacksSizeOfOneAndCurrentlyPoppingStack(self):
        return self.__isPoppingStack and self.areBothStacksSizeOfOne()

    def areBothStacksSizeOfOneAndCurrentlyNotPoppingStack(self):
        return not self.__isPoppingStack and self.areBothStacksSizeOfOne()

    def areBothStacksSizeOfOne(self):
        return self._stack.expression_stack_size() == 1 and self._stack.operator_stack_size() == 1
