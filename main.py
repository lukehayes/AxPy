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

p = AnimatedSprite("spritesheet.png", screen, x = 100, y = 100, xTuple = (0,5), yTuple = (0,0))
p2 = AnimatedSprite("spritesheet.png", screen, x = 100, y = 100, xTuple = (0,5), yTuple = (1,0))

c = 0
speed = 1000

while running:

    c += speed * dt

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pygame.quit()

            if event.key == pygame.K_a:
                p.x -= speed * dt
            if event.key == pygame.K_d:
                p.x += speed * dt
            if event.key == pygame.K_w:
                p.y += speed * dt
            if event.key == pygame.K_s:
                p.y -= speed * dt

    screen.fill(engine.bg_color)

    p.update(dt)
    p.draw()

    dt = clock.tick(engine.fps)/1000.0
    pygame.display.flip()

