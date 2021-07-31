class Engine():
    """The brain of the application"""
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.bg_color = (0,0,0)
        self.fps = 30

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

    @property
    def bg_color(self):
        return self._bg_color

    @bg_color.setter
    def bg_color(self, value):
        self._bg_color = value
