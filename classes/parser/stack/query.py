from typing import Tuple

from classes.parser.stack.stack import ParserStack
from classes.expression.operators import Operator


class ParserStackQuery:
    """This class is used for querying the state of a ParserStack
    """

    def __init__(self, stack: ParserStack):
        self.__is_popping_stack: bool = False
        self._stack: ParserStack = stack

    def can_create_left_operand(self) -> bool:
        return self.are_both_stacks_size_of_one() and self.is_popping_stack()

    def can_create_right_operand(self) -> bool:
        return self.are_both_stacks_size_of_one() and not self.is_popping_stack()

    def can_create_expression_with_same_precedence(self, operator: Operator) -> bool:
        are_stacks_ready = self._stack.expression_stack_size() >= 2 and self._stack.operator_stack_size() >= 1
        return are_stacks_ready and self.is_top_operator_same_precedence(operator)

    def can_create_expression_with_lower_precedence(self, operator: Operator) -> bool:
        return not self.is_top_operator_lower_precedence(operator)

    def set_is_popping_stack(self, is_popping_stack: bool):
        self.__is_popping_stack = is_popping_stack

    def is_popping_stack(self) -> bool:
        return self.__is_popping_stack

    def is_operator_stack_empty(self) -> bool:
        return self._stack.operator_stack_size() == 0

    def is_expression_stack_empty(self) -> bool:
        return self._stack.expression_stack_size() == 0

    def is_top_operator_lower_precedence(self, operator: Operator) -> bool:                
        topOperator = self._stack.peek_operator()
        if topOperator:
            return topOperator.is_lower_precedence_than(operator)
        else:
            print("Top operator is none")
            return False

    def is_top_operator_same_precedence(self, operator: Operator) -> bool:
        topOperator = self._stack.peek_operator()
        if topOperator:
            return topOperator.is_same_precedence_as(operator)
        else:
            return False

    def is_awaiting_operator(self) -> bool:
        stack_sizes = self._stack_sizes()
        return stack_sizes[0] >= stack_sizes[1]

    def is_expression_stack_higher_than_operator_stack(self) -> bool:
        stack_sizes = self._stack_sizes()
        return stack_sizes[0] > stack_sizes[1]

    def are_both_stacks_empty(self) -> bool:
        stack_sizes = self._stack_sizes()
        return stack_sizes[0] == 0 and stack_sizes[1] == 0

    def are_both_stacks_equal_size(self) -> bool:
        stack_sizes = self._stack_sizes()
        return stack_sizes[0] == stack_sizes[1]

    def are_both_stacks_size_of_one(self) -> bool:
        stack_sizes = self._stack_sizes()
        return stack_sizes[0] == 1 and stack_sizes[1] == 1

    def top_operator_is_right_associative(self) -> bool:
        operator = self._stack.peek_operator()
        
        if operator is None:
            return False        
        return not operator.is_left_to_right_associative()

    def _stack_sizes(self) -> Tuple[int, int]:
        stack = self._stack
        return (stack.expression_stack_size(), stack.operator_stack_size())
