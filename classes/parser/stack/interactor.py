import classes.expression.expressions as expressions
from classes.expression.expressions import NumberExpression

from classes.parser.number import NumberParser
from classes.parser.operator import OperatorParser
from classes.parser.stack.stack import ParserStack
from classes.parser.stack.query import ParserStackQuery


class ParserStackInteractor:
    def __init__(self, stack: ParserStack):
        self._stack: ParserStack = stack        
        self._query: ParserStackQuery = ParserStackQuery(self._stack)

    def popRootNode(self):
        rightOperand = self._stack.pop_expression()
        leftOperand = self._stack.pop_expression()
        return self.popOperatorAndJoinNodes(leftOperand, rightOperand)

    def popSingleNumber(self):
        return self._stack.pop_expression()    

    def popOperatorAndJoinNodes(self, leftNode, rightNode):
        operator = self._stack.pop_operator()
        if leftNode == None:
            leftNode = NumberExpression('0', False)
        if operator and leftNode and rightNode:
            return expressions.BinaryOperandExpression(leftNode, operator, rightNode)

    def pushNumberToken(self, numberToken):        
        self._stack.push_expression(numberToken)

    def pushOperatorToken(self, operatorToken, expression_creator):
        if not operatorToken:
            return
        
        if self.query.is_operator_stack_empty() or self.query.is_top_operator_lower_precedence(operatorToken):
            self._stack.push_operator(operatorToken)                                                                                               
        elif self._stack.expression_stack_size() >= 2 and self._stack.operator_stack_size() >= 1 and self.query.is_top_operator_same_precedence(operatorToken):

            # this should be replaceable with single call to expression_creator() but this does not work
            operandB = self._stack.pop_expression()
            operandA = self._stack.pop_expression()
            operator = self._stack.pop_operator()
            evaluatable_expression = expressions.BinaryOperandExpression(operandA, operator, operandB)
            self._stack.push_expression(evaluatable_expression)
            self._stack.push_operator(operatorToken)            
        else:          
            expression_creator()
            self._stack.push_operator(operatorToken)                                         

    @property
    def query(self) -> ParserStackQuery:
        return self._query
    