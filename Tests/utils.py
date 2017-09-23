from termcolor import colored

def Result(success):
	if success:
		print colored('Pass', 'green')
	else:
		print colored('Fail', 'red')

class Tester:
	def __init__(self, name):
		self.__name = name
		self.__tests = list()

	def addTest(self, test):
		self.__tests.append( test )

	
	def perform(self):
		for test in self.__tests:
			 Result( test.perform() )





# a testable will return a description string on fail and None on pass

class Test:
	def __init__(self, expectedBehaviourDescription, testable): 
		self.__description = expectedBehaviourDescription
		self.__testable = testable
	
	
	def perform(self): 
		print "\nTesting: %s" % self.__description

		result = self.__testable()
		if not result:
			return True
		else:
			print  "%s" % result
			return False


