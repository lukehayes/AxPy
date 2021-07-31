class Engine():
    """The brain of the application"""
    def __init__(self):
        self.width = 800
        self.height = 600

    @property
    def width(self):
        print("Getting Property")
        return self._width

    @width.setter
    def width(self, value):
        print("Setting Property")
        self._width = value


    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

