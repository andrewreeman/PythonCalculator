from typing import Optional

from classes.expression.expressions import BinaryOperandExpression, NumberExpression, Expression
from classes.expression.operators import Operator

from classes.parser.stack.stack import ParserStack
from classes.parser.stack.query import ParserStackQuery


class ParserStackInteractor:
    def __init__(self, stack: ParserStack):
        self._stack: ParserStack = stack
        self._query: ParserStackQuery = ParserStackQuery(self._stack)

    @property
    def query(self) -> ParserStackQuery:
        return self._query

    def pop_binary_expression(self) -> BinaryOperandExpression:
        right_operand = self._stack.pop_expression()
        left_operand = self._stack.pop_expression()
        return self.pop_operator_and_create_binary_expression(left_operand, right_operand)

    def pop_single_expression(self) -> Expression:
        return self._stack.pop_expression()

    def pop_operator_and_create_binary_expression(
      self,
      left_operand: Expression,
      right_operand: Expression
    ) -> BinaryOperandExpression:

        operator = self._stack.pop_operator()
        if left_operand is None:
            left_operand = NumberExpression('0', False)
        if operator and left_operand and right_operand:
            return BinaryOperandExpression(left_operand, operator, right_operand)

    def push_expression(self, expression: Expression):
        self._stack.push_expression(expression)

    def push_operator(self, operator: Optional[Operator]):
        if not operator:
            return

        if self.query.can_create_expression_with_same_precedence(operator):
            operandB = self._stack.pop_expression()
            operandA = self._stack.pop_expression()
            operator_from_stack = self._stack.pop_operator()
            evaluatable_expression = BinaryOperandExpression(operandA, operator_from_stack, operandB)
            self._stack.push_expression(evaluatable_expression)

        self._stack.push_operator(operator)

    def should_create_expression_before_pushing(self, operator: Operator) -> bool:
        if self.query.can_create_expression_with_same_precedence(operator):
            return False

        return self.query.can_create_expression_with_lower_precedence(operator)
