from classes.expression.operators import Operator


class Expression:
    """An Expression is something that can be evaluated to return a number.
    """

    def evaluate(self) -> float:
        """Evaluate the expression

        Returns:
            float -- The result of the evaluated expression
        """
        raise NotImplementedError()


class BinaryOperandExpression(Expression):
    def __init__(self,
                 operandA: Expression,
                 operator: Operator,
                 operandB: Expression):

        self._operandA: Expression = operandA
        self._operator: Operator = operator
        self._operandB: Expression = operandB

    def evaluate(self) -> float:
        operand_a_result = self._operandA.evaluate()
        operand_b_result = self._operandB.evaluate()
        return self._operator.operation()(operand_a_result, operand_b_result)

    def __str__(self):
        operand_a_str = str(self._operandA)
        operator_str = str(self._operator)
        operand_b_str = str(self._operandB)
        return f"({operand_a_str} {operator_str} {operand_b_str})"


class NumberExpression(Expression):
    def __init__(self, char: str, isNegative: bool):
        self._char: str = char
        self._isNegative: bool = isNegative

    def evaluate(self) -> float:
        number = float(self._char)
        if self._isNegative:
            return -number
        else:
            return number

    def __str__(self):
        return str(self.evaluate())
