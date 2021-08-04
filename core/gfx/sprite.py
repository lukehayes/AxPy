import pygame

class Sprite(object):
    """docstring for Sprite"""
    def __init__(self, file, x = 0,y = 0):
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

