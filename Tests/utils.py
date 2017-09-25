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
		print "\n=== " + self.__name + " ===\n"
		
		passCount = 0

		for test in self.__tests:
			success = test.perform()
		 	Result(success)
			
			if success:
				passCount += 1

		print "%d/%d passed" % (passCount, len(self.__tests))





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


