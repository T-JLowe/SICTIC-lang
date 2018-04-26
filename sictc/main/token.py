class Token():

    def __init__(self, kind, value):
        self._kind = kind
        self._value = value

    def tostr(self):
        print("TOKEN KIND: " + self._kind + ", TOKEN VALUE: " + self._value)
        