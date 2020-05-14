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
from classes.expression_tree_creator import ExpressionTreeCreator

class ExpressionParser:
    def __init__(self, stack_interactor: ParserStackInteractor, numberParser: NumberParser, operatorParser: OperatorParser):
        self._numberParser: NumberParser = numberParser
        self._operatorParser: OperatorParser = operatorParser
        self._stack_interactor: ParserStackInteractor = stack_interactor  
        self._tree = ExpressionTreeCreator(stack_interactor)  

    def parse(self, stream):                
        while stream.hasChars() and not stream.peek() == ')':

            if not self.canConsume(stream):
                stream.next()
                continue

            numberToken: Optional[NumberExpression] = self._parse_number(stream)
            if numberToken is not None:
                continue

            operatorToken = self._parse_operator(stream)
            
            self._stack_interactor.push_operator(operatorToken, self._tree.create_expression)
            
            if stream.peek() == '(':
                stream.next()                
                self._evaluate_bracket_expression(stream)                                

        return self._tree.create_expression()
    
    def canConsume(self, stream: StringStream) -> bool:                                
        return  stream.peek() == '(' or self._numberParser.canConsume(stream) or self._operatorParser.canConsume(stream)

    def _parse_number(self, stream: StringStream) -> Optional[NumberExpression]:
        # if awaiting operator and it is a negative sign then this is an operator and not a number
        if self._stack_interactor.query.is_awaiting_operator() and stream.peek() == '-':
            return None

        numberToken: Optional[NumberExpression] = self._numberParser.parse(stream)

        if numberToken:
            self._stack_interactor.push_expression(numberToken)            

        return numberToken

    def _parse_operator(self, stream: StringStream):
        return self._operatorParser.parse(stream)     

    def _evaluate_bracket_expression(self, stream):
        new_interactor = ParserStackInteractor(ParserStack())
        bracket_expression_parser = ExpressionParser(new_interactor, self._numberParser, self._operatorParser)
        self._stack_interactor.push_expression(bracket_expression_parser.parse(stream))
        
        if stream.peek() == ')':
            stream.next()    


