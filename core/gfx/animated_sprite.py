from core.gfx.sprite import Sprite
import pygame

class AnimatedSprite(Sprite):

    def __init__(self, file, speed = 0.1):
        super().__init__(file)

        self.current_frame = 0
        self.speed = speed
        self.counter = 0
        self.current_animation = "idle"
        self.tile_meta = {
            'idle' : 1,
            'running' : 2,
        }

    def play(self, animation):
        self.current_animation = animation
        pass

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


        screen.blit(self.image, (self.x, self.y), pygame.Rect(
                                (ts * sf) * int(self.current_frame),
                                (ts * sf) * self.tile_meta[self.current_animation],
                                ts * sf,
                                ts * sf)
                    )

