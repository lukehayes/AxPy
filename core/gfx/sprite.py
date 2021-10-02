import pygame

class Sprite(object):

    def __init__(self, file, x = 1,y = 1, xFrame = 0, yFrame = 0):
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

        # Scale our image by a scale factor
        self.image = pygame.transform.scale(
            self.image,(
                self.image.get_width() * self.scale_factor,
                self.image.get_height() * self.scale_factor
            )
        )

    def draw(self,screen):
        calc = 16 * 6
        screen.blit(self.image, (self.x, self.y), (calc * self.xFrame, calc * self.yFrame, calc, calc))

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
