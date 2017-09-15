import cStringIO 
	
# www.jython.org/javadoc/org/python/modules/cStringIO.StringIO.html
class StringStream:
	def __init__(self, string):
		self.__stream = cStringIO.StringIO()
		self.__stream.write(string)
		self.__stream.reset()	

	def next(self):		
		nextChar = self.__stream.read(1)
		print "Next char " + nextChar
		return nextChar
	
	def peek(self):
		char = self.next()
		self.__stepBack()
		return char
	
	def hasChars(self):
		print "Has chars"
		char = self.peek()
		return not char == ""
	
	def __stepBack(self):
		self.__stream.seek(-1, 1)
	
