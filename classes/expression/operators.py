# used so Operator class can reference Operator type
from __future__ import annotations
from typing import Callable

OperatorEvaluator = Callable[[float, float], float]


class Operator:
    """An operator will provide an operation for operating on two numbers.
    """

    def operation(self) -> OperatorEvaluator:
        """Provide a function for operating on two numbers

        Returns:
            OperatorEvaluator -- A function that can operate on two floats
        """
        raise NotImplementedError()

    def precedence(self) -> int:
        """The higher precedence operators should be performed
        before the lower precedence operators.

        Returns:
            int -- The precedence of this operator
        """
        raise NotImplementedError()

    def is_lower_precedence_than(self, operator: Operator):    
        return self.precedence() < operator.precedence()

    def is_same_precedence_as(self, operator: Operator):
        return self.precedence() == operator.precedence()

    def is_left_to_right_associative(self) -> bool:
        return True


class AddOperator(Operator):
    def operation(self) -> OperatorEvaluator:
        return lambda a, b: a + b

    def precedence(self) -> int:
        return 0

    def __str__(self):
        return "+"


class SubtractOperator(Operator):
    def operation(self) -> OperatorEvaluator:
        return lambda a, b: a - b

    def precedence(self) -> int:
        return 0

    def __str__(self):
        return "-"


class MultiplyOperator(Operator):
    def operation(self) -> OperatorEvaluator:
        return lambda a, b: a * b

    def precedence(self) -> int:
        return 1

    def __str__(self):
        return "*"


class DivideOperator(Operator):
    def operation(self) -> OperatorEvaluator:
        return lambda a, b: 0 if b == 0 else a/b

    def precedence(self) -> int:
        return 1

    def __str__(self):
        return "/"


class PowerOperator(Operator):
    def operation(self) -> OperatorEvaluator:
        return lambda a, b: a ** b

    def is_left_to_right_associative(self) -> bool:
        print("Power operator queried for associativity")
        return False

    def precedence(self):
        return 2

    def __str__(self):
        return "^"
