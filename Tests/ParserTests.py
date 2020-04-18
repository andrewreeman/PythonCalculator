import Parsers
import Tests.utils
import StringStream as strStr


def createTest(expression):

	testName = "Parsing " + expression
	
	def f():      
		stream = strStr.StringStream(expression)
		_numberParser = Parsers.NumberParser()
		_operatorParser = Parsers.OperatorParser()


		number = _numberParser.parse(stream)		
		operator = _operatorParser.parse(stream)		
		number = _numberParser.parse(stream)		

		if stream.hasChars():
			return "Stream should now be empty"

	return utils.Test(testName, f)

def testStream():
		stream = strStr.StringStream("1+1")
		
		def f():
			stream.peek()
			stream.next()
			stream.peek()
			stream.next()
			stream.peek()
			stream.peek()
			stream.peek()
			stream.next()
			stream.peek()
			stream.peek()

			if stream.hasChars():
				return "Stream should be empty"

		return utils.Test("Test that stream operators work", f)


def main():
	tester = utils.Tester("Parsing tests")

	test1 = createTest("1+1")


	for t in [test1, testStream()]:
		tester.addTest(t)

	tester.perform()
