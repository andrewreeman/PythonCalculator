import string
from typing import Optional

from classes.expression.expressions import NumberExpression
from classes.string_stream import StringStream


class NumberParser:
    def parse(self, stream: StringStream) -> Optional[NumberExpression]:
        if not self.can_consume(stream):
            return None

        token: str = stream.peek()
        if token.isspace():
            stream.next()
            return self.parse(stream)

        isNegative = self._isNegativeSign(token)

        if isNegative:
            stream.next()

        numberToken = self._consumeNumber(stream)
        return NumberExpression(numberToken, isNegative)

    def can_consume(self, stream: StringStream) -> bool:
        token = stream.peek()
        return self._isSingleDigitNum(token) or self._isNegativeSign(token)

    def _consumeNumber(self, stream: StringStream) -> Optional[NumberExpression]:
        if not self._can_consumeDigit(stream):
            return None

        token = stream.next()
        while self._can_consumeDigit(stream):
            token += stream.next()
        return token

    def _can_consumeDigit(self, stream: StringStream) -> bool:
        token = stream.peek()
        return self._isSingleDigitNum(token)

    def _isSingleDigitNum(self, char: str) -> bool:
        if len(char) == 0:
            return False

        return char in string.digits

    def _isNegativeSign(self, char: str) -> bool:
        result = char == '-'
        return result
