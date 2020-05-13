from typing import Optional

import classes.expression.expressions as expressions

from classes.string_stream import StringStream as strStr
from classes.expression.operators import AddOperator
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
        rightOperand = self._stack.popNumber()
        leftOperand = self._stack.popNumber()
        return self.popOperatorAndJoinNodes(leftOperand, rightOperand)

    def popSingleNumber(self):
        return self._stack.popNumber()    

    def popOperatorAndJoinNodes(self, leftNode, rightNode):
        operator = self._stack.popOperator()
        if leftNode == None:
            leftNode = NumberExpression('0', False)
        if operator and leftNode and rightNode:
            return expressions.BinaryOperandExpression(leftNode, operator, rightNode)

    def pushNumberToken(self, numberToken):        
        self._stack.pushNumber(numberToken)

    def pushOperatorToken(self, operatorToken, expression_creator):
        if not operatorToken:
            return
        
        if self.query.isOperatorStackEmpty() or self.query.isTopOperatorStackLowerPrecedence(operatorToken):
            self._stack.pushOperator(operatorToken)                                                                                               
        elif self._stack.numberStackSize() >= 2 and self._stack.operatorStackSize() >= 1 and self.query.isTopOperatorStackSamePrecedence(operatorToken):

            # should this be replaceable with single call to createNodeFromStack?
            operandB = self._stack.popNumber()
            operandA = self._stack.popNumber()
            operator = self._stack.popOperator()
            evaluatable_expression = expressions.BinaryOperandExpression(operandA, operator, operandB)
            self._stack.pushNumber(evaluatable_expression)
            self._stack.pushOperator(operatorToken)            
        else:          
            expression_creator()
            self._stack.pushOperator(operatorToken)                                         

    @property
    def query(self) -> ParserStackQuery:
        return self._query
    