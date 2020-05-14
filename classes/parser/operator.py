from typing import Optional

from classes.expression.operators import AddOperator, SubtractOperator, MultiplyOperator, DivideOperator, Operator
from classes.string_stream import StringStream


class OperatorParser:
    def parse(self, stream: StringStream) -> Optional[Operator]:
        if not self.can_consume(stream):
            return None

        token: str = stream.next()

        if token == '+':
            return AddOperator()
        elif token == '-':
            return SubtractOperator()
        elif token == '*':
            return MultiplyOperator()
        elif token == '/':
            return DivideOperator()
        elif token.isspace():
            return self.parse(stream)

    def can_consume(self, stream: StringStream) -> bool:
        token = stream.peek()
        return self._isOperator(token)

    def _isOperator(self, token: str) -> bool:
        return token == '+' or token == '-' or token == '*' or token == '/' or token == '^' or token == '%'
