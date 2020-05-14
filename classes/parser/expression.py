from typing import Optional

from classes.string_stream import StringStream
from classes.expression.expressions import Expression, NumberExpression
from classes.expression.operators import Operator
from classes.parser.number import NumberParser
from classes.parser.operator import OperatorParser

from .stack.stack import ParserStack
from .stack.interactor import ParserStackInteractor
from classes.expression_tree_creator import ExpressionTreeCreator


class ExpressionParser:
    """ Will parse an expression from a provided StringStream
    """
    def __init__(
      self,
      stack_interactor: ParserStackInteractor,
      number_parser: NumberParser,
      operator_parser: OperatorParser
    ):
        self._number_parser: NumberParser = number_parser
        self._operator_parser: OperatorParser = operator_parser
        self._stack_interactor: ParserStackInteractor = stack_interactor
        self._tree: ExpressionTreeCreator = ExpressionTreeCreator(stack_interactor)

    def parse(self, stream: StringStream) -> Optional[Expression]:
        while stream.hasChars() and not stream.peek() == ')':

            if not self._can_consume(stream):
                stream.next()
                continue

            if self._consume_number(stream):
                continue

            self._consume_operator(stream)

            if stream.peek() == '(':
                stream.next()
                self._evaluate_bracket_expression(stream)

        return self._tree.create_expression()

    def _evaluate_bracket_expression(self, stream):
        new_interactor = ParserStackInteractor(ParserStack())
        bracket_expression_parser = ExpressionParser(new_interactor, self._number_parser, self._operator_parser)
        self._stack_interactor.push_expression(bracket_expression_parser.parse(stream))

        if stream.peek() == ')':
            stream.next()

    def _can_consume(self, stream: StringStream) -> bool:
        return self._is_open_bracket(stream) or self._can_child_parser_consume(stream)

    def _consume_number(self, stream: StringStream) -> bool:
        number_token: Optional[NumberExpression] = self._parse_number(stream)
        if number_token:
            self._stack_interactor.push_expression(number_token)
            return True
        return False

    def _consume_operator(self, stream: StringStream):
        operator_token: Optional[Operator] = self._parse_operator(stream)
        if self._stack_interactor.should_create_expression_before_pushing(operator_token):
            self._tree.create_expression()
        self._stack_interactor.push_operator(operator_token)

    def _parse_number(self, stream: StringStream) -> Optional[NumberExpression]:
        if self._is_subtract_character(stream):
            return None

        numberToken: Optional[NumberExpression] = self._number_parser.parse(stream)
        return numberToken

    def _parse_operator(self, stream: StringStream):
        return self._operator_parser.parse(stream)

    def _is_open_bracket(self, stream: StringStream) -> bool:
        return stream.peek() == '('

    def _can_child_parser_consume(self, stream: StringStream) -> bool:
        return self._number_parser.can_consume(stream) or self._operator_parser.can_consume(stream)

    def _is_subtract_character(self, stream: StringStream) -> bool:
        return self._stack_interactor.query.is_awaiting_operator() and stream.peek() == '-'
