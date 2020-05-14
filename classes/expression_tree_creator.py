from typing import Optional

from classes.parser.stack.interactor import ParserStackInteractor
from classes.expression.expressions import Expression
from classes.parser.stack.query import ParserStackQuery


class ExpressionTreeCreator:
    """Creates an expression tree and returns the root expression
    """
    def __init__(self, interactor: ParserStackInteractor):
        self._tree: Optional[Expression] = None
        self._stack_interactor: ParserStackInteractor = interactor

    def create_expression(self) -> Optional[Expression]:
        self._tree = self._create_expression_tree(self._tree)
        return self._tree

    def _create_expression_tree(self, old_root_node: Optional[Expression]) -> Optional[Expression]:
        if self._has_finished_popping_stacks():
            self._stop_popping_stack()
            return old_root_node

        stack: ParserStackInteractor = self._stack_interactor
        query: ParserStackQuery = self._stack_interactor.query

        root_node = old_root_node

        if query.is_operator_stack_empty():
            root_node = stack.pop_single_expression()
        elif query.is_expression_stack_higher_than_operator_stack():
            self._start_popping_stack()
            root_node = stack.pop_binary_expression()
        elif query.can_create_left_operand():
            left_operand = stack.pop_single_expression()
            root_node = stack.pop_operator_and_create_binary_expression(left_operand, old_root_node)
        elif query.can_create_right_operand():
            right_operand = stack.pop_single_expression()
            root_node = stack.pop_operator_and_create_binary_expression(old_root_node, right_operand)
        else:
            rightOperand = stack.pop_binary_expression()
            root_node = stack.pop_operator_and_create_binary_expression(old_root_node, rightOperand)

        return self._create_expression_tree(root_node)

    def _start_popping_stack(self):
        self._stack_interactor.query.set_is_popping_stack(True)

    def _stop_popping_stack(self):
        self._stack_interactor.query.set_is_popping_stack(False)

    def _has_finished_popping_stacks(self) -> bool:
        return self._stack_interactor.query.are_both_stacks_empty()
