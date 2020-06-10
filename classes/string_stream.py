import io


class StringStream:
    def __init__(self, string: str):
        self._stream = io.BytesIO()        
        self._stream.write(bytes(string, "utf-8"))
        self._stream.seek(0)

    def next(self):
        nextChar = self._stream.read(1)

        if(nextChar.isspace()):
            return self.next()
        else:
            return nextChar.decode("utf-8")

    def peek(self):
        char = self.next()

        if not len(char) == 0:
            self._step_back()

        return char

    def has_chars(self):
        char = self.peek()
        return not char == ""

    def _step_back(self):
        self._stream.seek(-1, io.SEEK_CUR)
