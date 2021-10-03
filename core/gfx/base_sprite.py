import pygame

class BaseSprite(object):

    def __init__(self, file, screen, x = 10, y = 10):
        self.x = x
        self.y = y
        self.image = pygame.image.load("res/sprites/" + file).convert()
        self.tile_size = 16
        self.scale_factor = 6
        self.screen = screen

        # Scale our image by a scale factor
        self.image = pygame.transform.scale(
            self.image,(
                self.image.get_width() * self.scale_factor,
                self.image.get_height() * self.scale_factor
            )
        )

    def draw(self, x = None, y = None):
        # Check x and/or y are None here, use self version if so.
        if x == None:
            x = self.x

        if y == None:
            y = self.y

        calc = self.tile_size * self.scale_factor
        self.screen.blit(self.image, (x,y), (calc * self.xFrame, calc * self.yFrame, calc, calc))

