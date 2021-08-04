from core.gfx.sprite import Sprite
import pygame

class AnimatedSprite(Sprite):
    def __init__(self, file,
                 frame_size = 8):
        super().__init__(file)
        self.frame_size = frame_size
        self.rect = pygame.Rect(0,0,self.frame_size, self.frame_size)

    def play(self, speed,x):
        animation = self.image.subsurface(self.rect)
        ss = self.image.subsurface(self.rect)


