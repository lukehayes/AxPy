from core.gfx.sprite import Sprite
import pygame

class AnimatedSprite(Sprite):

    def __init__(self, file, x = 0,y = 0, speed = 0.5):
        super().__init__(file, x, y)

        self.tile_size = 16
        self.scale_factor = 6
        self.current_frame = 0
        self.speed = speed
        self.counter = 0

        self.image = pygame.transform.scale(
                        self.image,(
                            self.image.get_width() * self.scale_factor,
                            self.image.get_height() * self.scale_factor
                        )
                    )

    def update(self, dt, screen):
        ts = self.tile_size
        sf = self.scale_factor
        speed = 0.5
        max_frame = 4

        self.counter += dt

        if self.counter > self.speed:
            self.current_frame += 1

        print(int(self.counter))

        screen.blit(self.image, (200,200), pygame.Rect((ts * sf) * int(self.counter), (ts * sf) * 3,ts * sf,ts * sf))

