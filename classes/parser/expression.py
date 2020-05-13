from typing import Optional

import classes.expression.expressions as expressions
from classes.string_stream import StringStream

from classes.expression.operators import AddOperator

from classes.expression.expressions import NumberExpression
from classes.parser.number import NumberParser
from classes.parser.operator import OperatorParser

from .stack.stack import ParserStack
from .stack.query import ParserStackQuery
from .stack.interactor import ParserStackInteractor

class ExpressionParser:
    def __init__(self, stack_interactor: ParserStackInteractor, numberParser: NumberParser, operatorParser: OperatorParser):
        self._numberParser: NumberParser = numberParser
        self._operatorParser: OperatorParser = operatorParser
        self._stack_interactor: ParserStackInteractor = stack_interactor        

    def parse(self, stream):
        tree = None

        def onStackCanCreateExpression():            
            while not self._stack_interactor.stack.isOperatorStackEmpty():
                nonlocal tree
                tree = self._createNodeFromStack(0, tree)

        while stream.hasChars() and not stream.peek() == ')':

            if self._is_not_consumable(stream):
                stream.next()
                continue

            numberToken: Optional[NumberExpression] = self._parse_number(stream)
            if numberToken is not None:
                continue

            operatorToken = self._parse_operator(stream)
            
            self._stack_interactor.pushOperatorToken(operatorToken, onStackCanCreateExpression)
            
            if stream.peek() == '(':
                stream.next()                
                self._evaluate_bracket_expression(stream)                                

        return self._createNodeFromStack(0, tree)
    
    def _createNodeFromStack(self, depth, tree=None, orphan=None):
        # print "\nCreate node from stack called with tree: %s" % tree        
        logic = self._stack_interactor
        stack = self._stack_interactor.stack
        # print stack

        if depth == 0:
            # todo: if popping stack state just depends on an existence of a tree then just use that instead
            logic.query.setIsPoppingStack(False)

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

        elif logic.query.isNumberStackCountGreaterThanOperatorStackCount(stack):
            #	print "Number stack larger than operator stack"

            logic.query.setIsPoppingStack(True)
            rootNode = logic.popRootNode(stack)
            return self._createNodeFromStack(depth + 1, rootNode)

        elif logic.query.areBothStacksSizeOfOneAndCurrentlyPoppingStack(stack):
            #	print "Both stacks have one and currently popping stack"

            rootNode = logic.popJoiningRootNodeToRightOperand(stack, tree)
            return self._createNodeFromStack(depth + 1, rootNode)

        elif logic.query.areBothStacksSizeOfOneAndCurrentlyNotPoppingStack(stack):
            #	print "Both stacks have one and currently not popping stack"

            rootNode = logic.popJoiningRootNodeToLeftOperand(stack, tree)
            return self._createNodeFromStack(depth + 1, rootNode)

        elif logic.query.areBothStacksEqualSize(stack):
            #	print "Both stacks are equal size"

            orphan = logic.popRootNode(stack)
            return self._createNodeFromStack(depth + 1, tree, orphan)

    def _is_not_consumable(self, stream: StringStream) -> bool:        
        # can comment out open bracket test?
        return stream.peek() is None or stream.peek().isspace() or (not self._numberParser.canConsume(stream) and not self._operatorParser.canConsume(stream) and not stream.peek() == '(')

    def _parse_number(self, stream: StringStream) -> Optional[NumberExpression]:
        # if awaiting operator and it is a negative sign then this is an operator and not a number
        if self._stack_interactor.stack.numberStackSize() >= self._stack_interactor.stack.operatorStackSize() and stream.peek() == '-':
            return None

        numberToken: Optional[NumberExpression] = self._numberParser.parse(stream)

        if numberToken:
            self._stack_interactor.stack.pushNumber(numberToken)

        return numberToken

    def _parse_operator(self, stream: StringStream):
        return self._operatorParser.parse(stream)     

    def _evaluate_bracket_expression(self, stream):               
        new_interactor = ParserStackInteractor(ParserStack(), ParserStackQuery())
        bracket_expression_parser = ExpressionParser(new_interactor, self._numberParser, self._operatorParser)
        self._stack_interactor.stack.pushNumber(bracket_expression_parser.parse(stream))
        
        if stream.peek() == ')':
            stream.next()    


