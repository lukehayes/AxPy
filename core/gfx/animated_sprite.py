from core.gfx.base_sprite import BaseSprite
import pygame

class AnimatedSprite(BaseSprite):

    def __init__(self, file, screen, x = 1,y = 1, xTuple = (0,0), yTuple = (0,0)):
        """
        Constructor

        Args:
            file  (str): The name of the image file
            x  (int): The x position of the sprite
            y  (int): The y position of the sprite
        """
        super().__init__(file, screen, x,y)
        self.xFrameStart, self.xFrameEnd = xTuple
        self.yFrameStart, self.yFrameEnd = yTuple
        self.speed = 8
        self.animating = True

        self.cX = 4
        self.cY = 5

    def update(self, dt):

        if self.animating:
            self.cX += self.speed * dt
            # self.cY += self.speed * dt

            if self.cX >= self.xFrameEnd:
                self.cX = self.xFrameStart

            # if self.cY >= self.yFrameEnd:
                # self.cY = self.yFrameStart

            self.xFrame = int(self.cX)
            self.yFrame = int(self.cY)

    def draw(self, x = None, y = None):
        BaseSprite.draw(self)

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
