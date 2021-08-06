from core.gfx.sprite import Sprite
import pygame

class AnimatedSprite(Sprite):
    def __init__(self, file, x = 0,y = 0, sx = 1, sy = 1, frame_size = 16):
        super().__init__(file, x, y, sx, sy)
        self.frame_size = frame_size
        self.current_frame = 0
        self.rect = pygame.Rect(0,0,self.frame_size, self.frame_size)

    def play(self, screen, speed):
        animation = self.image.subsurface(self.rect)

        # screen.blit(self.image, (self.x, self.y), pygame.Rect(0,8 * x, 8 * 5,8 * 5))

        self.current_frame += (1 * self.scale_x)

        if self.current_frame > (1 * self.scale_x ):
            self.current_frame = 0


        screen.blit(self.image, (0,0), pygame.Rect(
            (self.frame_size * self.scale_x) * 6 + (self.current_frame * self.scale_x),
            (self.frame_size * self.scale_y) * 3,
            self.frame_size * self.scale_x,
            self.frame_size * self.scale_y)
        )


