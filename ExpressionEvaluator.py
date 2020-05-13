from classes.string_stream import StringStream
import classes.parser.Parsers as Parsers
from classes.parser.operator import OperatorParser
import classes.expression.expressions as expressions

import expressionstacklogic as logic
import expressionstack as stack
import expression_parser

def evaluate(expressionString):
	stream = StringStream(expressionString)	
	return consume(stream)

def consume(stream):		
	_logic = logic.ExpressionStackLogic()
	_stack = stack.ExpressionStack()
	_numberParser = Parsers.NumberParser()
	_operatorParser = OperatorParser()

	return expression_parser.ExpressionParser(_stack, _logic, _numberParser, _operatorParser).parse(stream).evaluate()