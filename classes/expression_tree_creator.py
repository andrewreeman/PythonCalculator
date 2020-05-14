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

        new_root_node = old_root_node

        if query.is_operator_stack_empty():
            new_root_node = stack.popSingleNumber()
        elif query.is_expression_stack_higher_than_operator_stack():
            self._start_popping_stack()
            new_root_node = stack.popRootNode()
        elif query.can_create_left_operand():
            leftOperand = stack.popSingleNumber()
            new_root_node = stack.popOperatorAndJoinNodes(leftOperand, old_root_node)
        elif query.can_create_right_operand():
            rightOperandNode = stack.popSingleNumber()
            new_root_node = stack.popOperatorAndJoinNodes(old_root_node, rightOperandNode)
        else:
            rightOperand = stack.popRootNode()
            new_root_node = stack.popOperatorAndJoinNodes(old_root_node, rightOperand)

        return self._create_expression_tree(new_root_node)

    def _start_popping_stack(self):
        self._stack_interactor.query.set_is_popping_stack(True)

    def _stop_popping_stack(self):
        self._stack_interactor.query.set_is_popping_stack(False)

    def _has_finished_popping_stacks(self) -> bool:
        return self._stack_interactor.query.are_both_stacks_empty()
