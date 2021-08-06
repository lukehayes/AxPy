import pygame

class BasicSprite(object):
    """
    BasicSprite serves as an inbetween for the Sprite and Animated Sprite Classes

    """
    def __init__(self,  x = 0, y = 0):
        self.x = x
        self.y = y
        self.current_frame = 0
        self.frames = [
            pygame.image.load("res/sprites/props_itens/" + "torch_anim_f0.png").convert(),
            pygame.image.load("res/sprites/props_itens/" + "torch_anim_f1.png").convert(),
            pygame.image.load("res/sprites/props_itens/" + "torch_anim_f2.png").convert(),
            pygame.image.load("res/sprites/props_itens/" + "torch_anim_f3.png").convert(),
            pygame.image.load("res/sprites/props_itens/" + "torch_anim_f4.png").convert(),
            pygame.image.load("res/sprites/props_itens/" + "torch_anim_f5.png").convert()
        ]
        self.max_frames = 6


    def draw(self, screen):
        self.current_frame  += 1

        if self.current_frame >= self.max_frames:
            self.current_frame = 0

        screen.blit(self.frames[self.current_frame], (self.x, self.y))


