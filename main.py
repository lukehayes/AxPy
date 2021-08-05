import pygame
import math
from core.block import Block
from core.block import Grid
from core.gfx import draw,drawBlock, drawSprite
from core.gfx.sprite import Sprite
from core.gfx.animated_sprite import AnimatedSprite
from core.engine import Engine
from core.particles import ParticleEmitter
from core.particles import Particle
import random

SPACE = 11

pygame.init()
monitor_size = pygame.display.Info()
engine = Engine(int(monitor_size.current_w / 2), int(monitor_size.current_h / 2))

screen = pygame.display.set_mode((engine.width, engine.height), pygame.RESIZABLE)
pygame.display.set_caption('Physics')
screen.fill(engine.bg_color)
pygame.display.flip()
running = True


c = 0
dt = 0
clock  = pygame.time.Clock()

scale_factor = 5


s = AnimatedSprite("spritesheet.png", x = 10, y = 10, sx = scale_factor, sy = scale_factor)
s.x = 100

frame = 0


while running:
    c += 1

    frame += 1

    if c >  (8 * 6):
        c = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(engine.bg_color)


    s.play(screen, 10)

    # screen.blit(s.image, (50,50))

    # screen.blit(s.image, (0,0))
    # s.play(screen, 5, c)
    # screen.blit(s.image, (0,0), pygame.Rect((16 * scale_factor) * 6 + (frame * scale_factor), (16 * scale_factor) * 3, 16 * scale_factor, 16 * scale_factor) )


    dt = clock.tick(engine.fps)/1000.0
    pygame.display.flip()

