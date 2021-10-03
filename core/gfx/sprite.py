import pygame

class Sprite(object):

    def __init__(self, file, screen, x = 1,y = 1, xFrame = 0, yFrame = 0):
        """
        Constructor

        Args:
            file  (str): The name of the image file
            x  (int): The x position of the sprite
            y  (int): The y position of the sprite
        """
        super().__init__()
        self.image = pygame.image.load("res/sprites/" + file).convert()
        self.x = x
        self.y = y
        self.xFrame = xFrame
        self.yFrame = yFrame
        self.tile_size = 16
        self.scale_factor = 6
        self.speed = 8
        self.animating = True
        self.screen = screen

        self.cX = 4
        self.cY = 5

        # Scale our image by a scale factor
        self.image = pygame.transform.scale(
            self.image,(
                self.image.get_width() * self.scale_factor,
                self.image.get_height() * self.scale_factor
            )
        )

    def update(self, dt):

        if self.animating:
            self.cX += self.speed * dt

            if self.cX >= 12:
                self.cX = 6

            self.xFrame = int(self.cX)
            self.yFrame = int(self.cY)

    def draw(self, x = None, y = None):

        # Check x and/or y are None here, use self version if so.
        if x == None:
            x = self.x

        if y == None:
            y = self.y

        calc = self.tile_size * self.scale_factor
        self.screen.blit(self.image, (x,y), (calc * self.xFrame, calc * self.yFrame, calc, calc))

    @property
    def sx(self):
        return self.sx

    @sx.setter
    def sx(self, value):
        self.sx = value

    @property
    def sy(self):
        return self.sy

    @sy.setter
    def sy(self, value):
        self.sy = value
