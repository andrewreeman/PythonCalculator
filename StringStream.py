import cStringIO 
	
class StringStream:
	def __init__(self, string):
		self.__stream = cStringIO.StringIO()
		self.__stream.write(string)
		self.__stream.reset()	

	def next(self):		
		return self.__stream.read(1)
	
	def peek(self):
		char = self.next()
		self.__stepBack()
		return char
	
	def __stepBack(self):
		self.__stream.seek(-1, 1)
