from typing import Optional

from classes.parser.number import NumberParser
from classes.parser.operator import OperatorParser
from classes.parser.expression import ExpressionParser
from classes.parser.stack.stack import ParserStack
from classes.parser.stack.query import ParserStackQuery
from classes.parser.stack.interactor import ParserStackInteractor

import Tests.utils as utils

from classes.string_stream import StringStream


def createTest(expression, expectedResult):

    testName = "Evaluating expression %s. Expecting result to be %d " % (
        expression, expectedResult)

    def f():

        stream = StringStream(expression)

        _stack = ParserStack()
        _logic = ParserStackInteractor(_stack)
        _numberParser = NumberParser()
        _operatorParser = OperatorParser()

        _expressionParser = ExpressionParser(
            _logic, _numberParser, _operatorParser)
        result = _expressionParser.parse(stream)
        if not result.evaluate() == expectedResult:
            return "Result is: %s. \n object is: %s" % (str(result.evaluate()), str(result))

    return utils.Test(testName, f)


def main(_tester: Optional[utils.Tester] = None):
    tester = _tester or utils.Tester("Expression parsing tests")

    def addTest(test, expected):
        tester.addTest(createTest(test, expected))

    def justTest(test, expected):
        tester.justTest(createTest(test, expected))

    addTest("1+1", 2)
    addTest("3+2*4", 11)
    addTest("10-10/5+3", 11)

    addTest("7-4*8+3-4/2", -24)
    addTest("7-4*8+3-4", -26)

    addTest("7-4*8-4", -29)
    addTest("7-4*8+3", -22)

    addTest("3+(2+5)*4", 31)
    addTest("(7-8)*(2-(4+3)*8)", 54)
    addTest("1-8", -7)
    addTest("1-1", 0)
    addTest("(10+0)-2", 8)

    addTest("(10+0)", 10)

    addTest("10+0", 10)
    addTest("10", 10)
    addTest("(10)", 10)
    addTest("2-(3*2)+10", 6)
    addTest("3+(2+5)-4", 6)
    addTest("(10+(3*2))", 16)
    addTest("(10+(3*2))-2", 14)
    addTest("10-10/5+3", 11)
    addTest("10-10", 0)
    addTest("10 - 10", 0)
    addTest("10-10/5+3", 11)
    addTest("10 - 10 / 5 + 3", 11)
    addTest("-1", -1)
    addTest("-0", -0)
    addTest("(-0)", -0)
    addTest("2-(6)+10", 6)
    addTest("-4+10", 6)
    addTest("2-6+0", -4)
    addTest("2-6+10", 6)
    addTest("1*2/2", 1)
    addTest("1*8/4", 2)
    addTest("1+2/2", 2)
    addTest("1+1*2/2-1", 1)
    addTest("1+1*2/2", 2)
    addTest("1+2/2", 2)  # '(1 + (2 / 2))' is correct grouping
    addTest("3+12/3*5", 23)
    addTest("2^6", 64)
    addTest("2^(6+2)", 256)
    addTest("2^6+2", 256)
    addTest("2^8+2-2", 256)
    # addTest("2^(8+2)-2", 256)

    if _tester is None:
        tester.perform()
