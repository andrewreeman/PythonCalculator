class ParserStack:
    """This is a stack used by the the ExpressionParser via
    the ParserStackInteractor.
    This stack maintains the parsing state via
    a stack for expressions and a stack for operators
    """

    def __init__(self):
        self._operator_stack = list()
        self._expression_stack = list()

    def push_operator(self, operator):
        self._operator_stack.append(operator)

    def push_expression(self, number):
        self._expression_stack.append(number)

    def pop_operator(self):
        if self._operator_stack:
            return self._operator_stack.pop()
    
    def pop_expression(self):
        if self._expression_stack:
            return self._expression_stack.pop()
        
    def peek_operator(self):
        if self._operator_stack:
            return self._operator_stack[-1]
        else:
            return None

    def expression_stack_size(self):
        return len(self._expression_stack)

    def operator_stack_size(self):
        return len(self._operator_stack)

    def __str__(self):
        description = "Stack contents\n\Expression stack: \n"

        for n in reversed(self._expression_stack):
            description += "\t%s\n" % str(n)

        description += "\n\tOperator stack: \n"

        for o in reversed(self._operator_stack):
            description += "\t%s\n" % str(o)

        return description
