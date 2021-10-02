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

pygame.init()
monitor_size = pygame.display.Info()
engine = Engine(int(monitor_size.current_w / 2), int(monitor_size.current_h / 2))

screen = pygame.display.set_mode((engine.width, engine.height), pygame.RESIZABLE)
pygame.display.set_caption('Physics')
screen.fill(engine.bg_color)
pygame.display.flip()
running = True


dt = 0
clock  = pygame.time.Clock()

# s = AnimatedSprite("spritesheet.png")
s = Sprite("spritesheet.png", x = 400, y = 600, xFrame = 6, yFrame = 3)
# s.animating = False

c = 0
speed = 1

while running:

    c += speed * dt


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pygame.quit()

    screen.fill(engine.bg_color)

    s.x = 200 + math.cos(c) * 100
    s.y = 200 + math.sin(c) * 100

    s.update(dt)
    s.draw(screen)

    # screen.blit(s.image, (0,0))

    # screen.blit(s.image, (0,400), (calc * 9,0, calc, calc))
    # s.update(dt, screen)

    dt = clock.tick(engine.fps)/1000.0
    pygame.display.flip()

