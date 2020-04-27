from StringStream import StringStream
import Parsers
import expressions

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
	_operatorParser = Parsers.OperatorParser()

	return expression_parser.ExpressionParser(_stack, _logic, _numberParser, _operatorParser).parse(stream).evaluate()