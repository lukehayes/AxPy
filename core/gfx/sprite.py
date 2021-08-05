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
        self.image = pygame.transform.scale(self.image, (int(1042/sx), int(768/sy) ))
        self.x = x
        self.y = y

