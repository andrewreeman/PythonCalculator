from typing import Optional

import expressions
#import pdb
#import StringStream as strStr
from StringStream import StringStream

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
            if numberToken is not None:
                continue

            operatorToken = self._parse_operator(stream)

            if operatorToken:
                if self._stack.isOperatorStackEmpty() or self._logic.isTopOperatorStackLowerPrecedence(self._stack, operatorToken):
                    self._stack.pushOperator(operatorToken)                                                                                   
                elif self._stack.numberStackSize() >= 2 and self._stack.operatorStackSize() >= 1 and self._logic.isTopOperatorStackSamePrecedence(self._stack, operatorToken):

                    # should this be replaceable with single call to createNodeFromStack?
                    operandB = self._stack.popNumber()
                    operandA = self._stack.popNumber()
                    operator = self._stack.popOperator()
                    evaluatable_expression = expressions.BinaryOperandExpression(operandA, operator, operandB)
                    self._stack.pushNumber(evaluatable_expression)
                    self._stack.pushOperator(operatorToken)
                else:                    
                    while not self._stack.isOperatorStackEmpty():
                        tree = self._createNodeFromStack(0, tree)
                    self._stack.pushOperator(operatorToken)
            
            if stream.peek() == '(':
                stream.next()                
                self._evaluate_bracket_expression(stream)                                

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
        # can comment out open bracket test?
        return stream.peek() is None or stream.peek().isspace() or (not self._numberParser.canConsume(stream) and not self._operatorParser.canConsume(stream) and not stream.peek() == '(')

    def _parse_number(self, stream: StringStream) -> Optional[NumberExpression]:
        # if awaiting operator and it is a negative sign then this is an operator and not a number
        if self._stack.numberStackSize() >= self._stack.operatorStackSize() and stream.peek() == '-':
            return None

        numberToken: Optional[NumberExpression] = self._numberParser.parse(stream)

        if numberToken:
            self._stack.pushNumber(numberToken)

        return numberToken

    def _parse_operator(self, stream: StringStream):
        return self._operatorParser.parse(stream)     

    def _evaluate_bracket_expression(self, stream):        
        bracket_expression_parser = ExpressionParser(ExpressionStack(), self._logic, self._numberParser, self._operatorParser)        
        self._stack.pushNumber(bracket_expression_parser.parse(stream))
        
        if stream.peek() == ')':
            stream.next()
           
