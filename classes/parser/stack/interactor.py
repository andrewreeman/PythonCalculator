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

    def popRootNode(self, expressionStack):
        rightOperand = expressionStack.popNumber()
        leftOperand = expressionStack.popNumber()
        return self.popOperatorAndJoinNodes(expressionStack, leftOperand, rightOperand)

    def popSingleNumberAddition(self, expressionStack, oldRootNode):
        number = expressionStack.popNumber()
        _oldRootNode = oldRootNode or NumberExpression('0', False)
        return expressions.BinaryOperandExpression(_oldRootNode, AddOperator(), number)        

    def popJoiningRootNodeToRightOperand(self, expressionStack, oldRootNode):
        leftOperand = expressionStack.popNumber()
        return self.popOperatorAndJoinNodes(expressionStack, leftOperand, oldRootNode)

    def popJoiningRootNodeToLeftOperand(self, expressionStack, oldRootNode):
        rightOperandNode = expressionStack.popNumber()
        return self.popOperatorAndJoinNodes(expressionStack, oldRootNode, rightOperandNode)

    def popOperatorAndJoinNodes(self, expressionStack, leftNode, rightNode):
        operator = expressionStack.popOperator()
        if leftNode == None:
            leftNode = NumberExpression('0', False)
        if operator and leftNode and rightNode:
            return expressions.BinaryOperandExpression(leftNode, operator, rightNode)

    def pushOperatorToken(self, operatorToken, expression_creator):
        if not operatorToken:
            return
        
        if self.stack.isOperatorStackEmpty() or self.query.isTopOperatorStackLowerPrecedence(operatorToken):
            self.stack.pushOperator(operatorToken)                                                                                               
        elif self.stack.numberStackSize() >= 2 and self.stack.operatorStackSize() >= 1 and self.query.isTopOperatorStackSamePrecedence(operatorToken):

            # should this be replaceable with single call to createNodeFromStack?
            operandB = self.stack.popNumber()
            operandA = self.stack.popNumber()
            operator = self.stack.popOperator()
            evaluatable_expression = expressions.BinaryOperandExpression(operandA, operator, operandB)
            self.stack.pushNumber(evaluatable_expression)
            self.stack.pushOperator(operatorToken)            
        else:          
            expression_creator()
            self.stack.pushOperator(operatorToken)                         
                

    @property
    def query(self) -> ParserStackQuery:
        return self._query

    @property
    def stack(self) -> ParserStack:
        return self._stack