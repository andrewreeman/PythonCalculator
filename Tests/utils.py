from typing import List

from termcolor import colored

def Result(success):
	if success:
		print(colored('Pass', 'green'))
	else:
		print(colored('Fail', 'red'))


class Tester:
	def __init__(self, name):
		self.__name = name
		self.__tests = list()
		self.__singleTest = None

	@property
	def just_test_this(self) -> bool:
		return self.__singleTest is not None

	def addTest(self, test):
		self.__tests.append( test )
	
	def justTest(self, test):
		self.__singleTest = test
	
	def perform(self):
		print("\n=== " + self.__name + " ===\n")
		if self.__singleTest:
			self.__tests.clear()
			self.__tests.append(self.__singleTest)

		passCount = 0

		for test in self.__tests:
			success = test.perform()
			Result(success)
			
			if success:
				passCount += 1
			else:
				raise AssertionError("Test failed")

		print("%d/%d passed" % (passCount, len(self.__tests)))

class MultiTester:
	def __init__(self):
		self._testers: List[Tester] = list()

	def new_test_package(self, name) -> Tester:
		tester = Tester(name)
		self._testers.append(tester)
		return tester

	def perform(self):		
		for tester in self._testers:
			if tester.just_test_this:
				tester.perform()
				return
		
		for tester in self._testers:
			tester.perform()	


# a testable will return a description string on fail and None on pass

class Test:
	def __init__(self, expectedBehaviourDescription, testable): 
		self.__description = expectedBehaviourDescription
		self.__testable = testable
	
	
	def perform(self): 
		print("\nTesting: %s" % self.__description)

		result = self.__testable()
		if not result:
			return True
		else:
			print("%s" % result)
			return False


