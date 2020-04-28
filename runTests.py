import Tests.Expressions as ExpressionTests
import Tests.ExpressionStackTests as StackTests
import Tests.operatortests as OperatorTests
import Tests.ExpressionParserTests as ExpressionParserTests
import Tests.ParserTests as ParserTests
from Tests.utils import MultiTester

tester = MultiTester()
ExpressionParserTests.main(tester.new_test_package("Expression parsing tests"))
# ExpressionTests.main()
# StackTests.main()
# OperatorTests.main()
# ParserTests.main()

tester.perform()