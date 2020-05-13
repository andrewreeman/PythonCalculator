from classes.string_stream import StringStream
from classes.parser.number import NumberParser
from classes.parser.expression import ExpressionParser
from classes.parser.operator import OperatorParser
import classes.expression.expressions as expressions

import expressionstacklogic as logic
from classes.expressionstack import ExpressionStack


def evaluate(expressionString):
	stream = StringStream(expressionString)	
	return consume(stream)

def consume(stream):		
	_logic = logic.ExpressionStackLogic()
	_stack = ExpressionStack()
	_numberParser = NumberParser()
	_operatorParser = OperatorParser()

	return ExpressionParser(_stack, _logic, _numberParser, _operatorParser).parse(stream).evaluate()