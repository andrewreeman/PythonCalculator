from typing import Optional

import expressions
#import pdb
#import StringStream as strStr
from StringStream import StringStream

import expressionstack as expStack
from expressionstack import ExpressionStack

from operators import AddOperator
from expressions import NumberExpression
from Parsers import NumberParser
from Parsers import OperatorParser
from expressionstacklogic import ExpressionStackLogic


class ExpressionParser:
    def __init__(self, expressionStack: ExpressionStack, expressionStackLogic: ExpressionStackLogic, numberParser: NumberParser, operatorParser: OperatorParser):
        self._numberParser: NumberParser = numberParser
        self._operatorParser: OperatorParser = operatorParser
        self._stack: ExpressionStack = expressionStack
        self._logic: ExpressionStackLogic = expressionStackLogic

    def parse(self, stream):
        tree = None

        while stream.hasChars() and not stream.peek() == ')':

            if self._is_not_consumable(stream):
                stream.next()
                continue

            numberToken: Optional[NumberExpression] = self._parse_number(stream)
            operatorToken = self._parse_operator(stream)

            if operatorToken:
                if self._stack.isOperatorStackEmpty():
                    self._stack.pushOperator(operatorToken)
                else:
                    if self._logic.isTopOperatorStackLowerPrecedence(self._stack, operatorToken):
                        self._stack.pushOperator(operatorToken)
                    elif self._stack.numberStackSize() >= 2 and self._stack.operatorStackSize() >= 1 and self._logic.isTopOperatorStackSamePrecedence(self._stack, operatorToken):
                        operandB = self._stack.popNumber()
                        operandA = self._stack.popNumber()
                        operator = self._stack.popOperator()
                        new_top_number = expressions.BinaryOperandExpression(
                            operandA, operator, operandB).evaluate()
                        self._stack.pushNumber(
                            NumberExpression.fromNumber(new_top_number))
                        self._stack.pushOperator(operatorToken)
                    else:
                        while not self._stack.isOperatorStackEmpty():
                            tree = self._createNodeFromStack(0, tree)
                        self._stack.pushOperator(operatorToken)

            # todo: this is ugly code. we should be abstracting this all into a bracket parser!
            if stream.peek() == '(':
                stream.next()
                newStack = expStack.ExpressionStack()
                bracketTree = ExpressionParser(
                    newStack, self._logic, self._numberParser, self._operatorParser).parse(stream)

                numberResult = bracketTree.evaluate()
                tempStream = StringStream("%d" % numberResult)
                numberToken = self._numberParser.parse(tempStream)
                self._stack.pushNumber(numberToken)
                if stream.peek() == ')':
                    stream.next()

        return self._createNodeFromStack(0, tree)

    def _createNodeFromStack(self, depth, tree=None, orphan=None):
        # print "\nCreate node from stack called with tree: %s" % tree
        logic = self._logic
        stack = self._stack
        # print stack

        if depth == 0:
            # todo: if popping stack state just depends on an existence of a tree then just use that instead
            logic.setIsPoppingStack(False)

        # print "Is currently popping stack: %s" % str(logic.isPoppingStack())
        # print "Depth is: %s" % str(depth)

        if stack.isOperatorStackEmpty():
            if stack.isNumberStackEmpty():
                return tree
            else:
                rootNode = logic.popSingleNumberAddition(stack, tree)
                return self._createNodeFromStack(depth + 1, rootNode)
        #	print "Operator stack is empty"
        elif orphan:
            #	print "We have an orphan"

            rootNode = logic.popOperatorAndJoinNodes(stack, tree, orphan)
            return self._createNodeFromStack(depth + 1, rootNode)

        elif logic.isNumberStackCountGreaterThanOperatorStackCount(stack):
            #	print "Number stack larger than operator stack"

            logic.setIsPoppingStack(True)
            rootNode = logic.popRootNode(stack)
            return self._createNodeFromStack(depth + 1, rootNode)

        elif logic.areBothStacksSizeOfOneAndCurrentlyPoppingStack(stack):
            #	print "Both stacks have one and currently popping stack"

            rootNode = logic.popJoiningRootNodeToRightOperand(stack, tree)
            return self._createNodeFromStack(depth + 1, rootNode)

        elif logic.areBothStacksSizeOfOneAndCurrentlyNotPoppingStack(stack):
            #	print "Both stacks have one and currently not popping stack"

            rootNode = logic.popJoiningRootNodeToLeftOperand(stack, tree)
            return self._createNodeFromStack(depth + 1, rootNode)

        elif logic.areBothStacksEqualSize(stack):
            #	print "Both stacks are equal size"

            orphan = logic.popRootNode(stack)
            return self._createNodeFromStack(depth + 1, tree, orphan)

    def _is_not_consumable(self, stream: StringStream) -> bool:
        return not self._numberParser.canConsume(stream) and not self._operatorParser.canConsume(stream) and not stream.peek() == '('

    def _parse_number(self, stream: StringStream) -> Optional[NumberExpression]:
        numberToken: Optional[NumberExpression] = self._numberParser.parse(
            stream)
        if numberToken:
            self._stack.pushNumber(numberToken)

        return numberToken

    def _parse_operator(self, stream: StringStream):
        operator_token = self._operatorParser.parse(stream)

        if not operator_token and not self._stack.isNumberStackEmpty():
            numberToken: Optional[NumberExpression] = self._stack.popNumber()
            operator_token = numberToken.convert_to_subtract_operator()
            if not operator_token:
                self._stack.pushNumber(numberToken)
        return operator_token