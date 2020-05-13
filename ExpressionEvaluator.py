from classes.string_stream import StringStream
from classes.parser.number import NumberParser
from classes.parser.expression import ExpressionParser
from classes.parser.operator import OperatorParser
import classes.expression.expressions as expressions

from classes.expressionstacklogic import ExpressionStackLogic
from classes.expressionstack import ExpressionStack
from sys import argv


def evaluate(expressionString):
	stream = StringStream(expressionString)	
	return parse(stream).evaluate()

def parse(stream):		
	_logic = ExpressionStackLogic()
	_stack = ExpressionStack()
	_numberParser = NumberParser()
	_operatorParser = OperatorParser()

	return ExpressionParser(_stack, _logic, _numberParser, _operatorParser).parse(stream)

if __name__ == "__main__":	
	print(evaluate(argv[1]))	