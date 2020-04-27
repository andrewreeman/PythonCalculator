from StringStream import StringStream
import Parsers
import expressions

import expressionstacklogic as logic
import expressionstack as stack

def evaluate(expressionString):
	stream = StringStream(expressionString)	
	return consume(stream)

def consume(stream):		
	_logic = logic.ExpressionStackLogic()
	_stack = stack.ExpressionStack()
	_numberParser = Parsers.NumberParser()
	_operatorParser = Parsers.OperatorParser()

	return logic.ExpressionParser(_stack, _logic, _numberParser, _operatorParser).parse(stream).evaluate()