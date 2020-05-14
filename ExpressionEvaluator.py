from sys import argv

from classes.string_stream import StringStream
from classes.parser.number import NumberParser
from classes.parser.expression import ExpressionParser
from classes.parser.operator import OperatorParser
from classes.parser.stack.stack import ParserStack
from classes.parser.stack.interactor import ParserStackInteractor


def evaluate(expressionString):
    stream = StringStream(expressionString)
    return parse(stream).evaluate()


def parse(stream):
    _logic = ParserStackInteractor(ParserStack())
    _numberParser = NumberParser()
    _operatorParser = OperatorParser()

    return ExpressionParser(_logic, _numberParser, _operatorParser).parse(stream)


if __name__ == "__main__":
    print(evaluate(argv[1]))
