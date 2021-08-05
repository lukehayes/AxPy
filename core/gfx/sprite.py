import pygame

class Sprite(object):
    """docstring for Sprite"""
    def __init__(self, file, x = 0,y = 0, sx = 1, sy = 1):
        """
        Constructor

        Args:
            file  (str): The name of the image file
            x  (int): The x position of the sprite
            y  (int): The y position of the sprite
            sx (int): The scale factor on x axis
            sy (int): The scale factor on y axis
        """
        super().__init__()
        self.image = pygame.image.load("res/sprites/" + file).convert()

        # Scale our image by a scale factor
        self.image = pygame.transform.scale(
                        self.image,(
                            self.image.get_width() * sx,
                            self.image.get_height() * sy
                        )
                    )

        self.x = x
        self.y = y
        self.scale_x = sx
        self.scale_y = sy

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
