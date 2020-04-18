import io 
	
# www.jython.org/javadoc/org/python/modules/cStringIO.StringIO.html
class StringStream:
	def __init__(self, string):		
		self._stream = io.BytesIO()
		self._stream.write(bytes(string, "utf-8"))
		self._stream.seek(0)	

	def next(self):				
		nextChar = self._stream.read(1)				
		return nextChar.decode("utf-8")
	
	def peek(self):
		char = self.next()
		
		if not char == "":
			self._stepBack()
		
		return char
	
	def hasChars(self):
		char = self.peek()			
		return not char == ""
	
	def _stepBack(self):
		self._stream.seek(-1, io.SEEK_CUR)
	
