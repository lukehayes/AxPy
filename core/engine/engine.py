import pygame

class Engine():
    """The brain of the application"""
    def __init__(self, width, height, title = "AxPy"):
        self.width = width
        self.height = height
        self.title = title
        self.bg_color = (0,0,0)
        self.fps = 30
        self.clock = pygame.time.Clock()
        self.running = True

    """ PROPERTIES  """
    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
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

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value

    """ METHODS  """

    def update(self):

        deltaTime = 0

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            print(deltaTime)

            deltaTime = self.clock.tick(self.fps)/1000.0
            pygame.display.flip()




