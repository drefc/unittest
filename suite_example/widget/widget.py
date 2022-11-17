class Widget:

    def __init__(self, name):
        self.name = name
        self._x = 50
        self._y = 50

    def size(self):
        return (self._x,self._y)

    def resize(self, x, y):
        self._x = x
        self._y = y
    
    def dispose(self):
        pass