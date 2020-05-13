from classes.string_stream import StringStream
from classes.parser.number import NumberParser
from classes.parser.expression import ExpressionParser
from classes.parser.operator import OperatorParser
from classes.parser.stack.stack import ParserStack

import classes.expression.expressions as expressions
from classes.parser.stack.query import ParserStackQuery
from classes.parser.stack.interactor import ParserStackInteractor

from sys import argv

def evaluate(expressionString):
	stream = StringStream(expressionString)	
	return parse(stream).evaluate()

def parse(stream):		
	_logic = ParserStackInteractor(ParserStack(), ParserStackQuery())	
	_numberParser = NumberParser()
	_operatorParser = OperatorParser()

	return ExpressionParser(_logic, _numberParser, _operatorParser).parse(stream)

if __name__ == "__main__":	
	print(evaluate(argv[1]))	