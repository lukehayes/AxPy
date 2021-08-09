from core.gfx.sprite import Sprite
import pygame

class AnimatedSprite(Sprite):

    def __init__(self, file, x = 0,y = 0, speed = 0.1):
        super().__init__(file, x, y)

        self.current_frame = 0
        self.speed = speed
        self.counter = 0

    def update(self, dt, screen):
        ts = self.tile_size
        sf = self.scale_factor
        max_frame = 5

        self.counter += dt

        if self.counter > self.speed:
            self.current_frame += 1
            self.counter = 0

            if self.current_frame > max_frame:
                self.current_frame = 0


        screen.blit(self.image, (200,200), pygame.Rect(
                                (ts * sf) * int(self.current_frame),
                                (ts * sf) * 4,
                                ts * sf,
                                ts * sf)
                    )

