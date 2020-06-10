from typing import Optional
from typing import List

from classes.expression.operators import Operator
from classes.expression.expressions import Expression


class ParserStack:
    """This is a stack used by the the ExpressionParser via
    the ParserStackInteractor.
    This stack maintains the parsing state via
    a stack for expressions and a stack for operators
    """

    def __init__(self):
        self._operator_stack: List[Operator] = list()
        self._expression_stack: List[Expression] = list()
        self._operator_stack.append(4)
        self._operator_stack.clear()

    def push_operator(self, operator: Operator):
        self._operator_stack.append(operator)

    def push_expression(self, expression: Expression):
        self._expression_stack.append(expression)

    def pop_operator(self) -> Optional[Operator]:
        if self.operator_stack_size() > 0:
            return self._operator_stack.pop()

    def pop_expression(self) -> Optional[Expression]:
        if self.expression_stack_size() > 0:
            return self._expression_stack.pop()

    def peek_operator(self) -> Optional[Operator]:
        if self._operator_stack:
            return self._operator_stack[-1]
        else:
            return None

    def expression_stack_size(self) -> int:
        return len(self._expression_stack)

    def operator_stack_size(self) -> int:
        return len(self._operator_stack)

    def __str__(self):
        description = "Stack contents\n Expression stack: \n"
        
        if(len(self._expression_stack) == 0):
            description += "empty!"

        for n in reversed(self._expression_stack):
            description += "\t%s\n" % str(n)

        description += "\n\tOperator stack: \n"
        if(len(self._operator_stack) == 0):
            description += "empty!"

        for o in reversed(self._operator_stack):
            description += "\t%s\n" % str(o)

        return description
