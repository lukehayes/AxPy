import pygame
from core.gfx.base_sprite import BaseSprite

class Sprite(BaseSprite):

    def __init__(self, file, screen, x = 1,y = 1, xFrame = 0, yFrame = 0):
        """
        Constructor

        Args:
            file  (str): The name of the image file
            x  (int): The x position of the sprite
            y  (int): The y position of the sprite
        """
        super().__init__(file, screen, x,y)
        self.xFrame = xFrame
        self.yFrame = yFrame

        self.cX = 4
        self.cY = 5

    def update(self, dt):
        pass

    def draw(self, x = None, y = None):
        BaseSprite.draw(self)

