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
speed = 100
movement = 1

vel = pygame.math.Vector2(0.1,0.1)

while running:

    c += speed * dt

    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pygame.quit()

    if keys[pygame.K_a]:
        vel.x -= movement
    if keys[pygame.K_d]:
        vel.x += movement
    if keys[pygame.K_w]:
        vel.y -= movement
    if keys[pygame.K_s]:
        vel.y += movement

    print(vel)
    vel = pygame.math.Vector2.normalize(vel)
    print(vel)

    p.x += vel.x * speed * dt
    p.y += vel.y * speed * dt

    screen.fill(engine.bg_color)

    p.update(dt)
    p.draw()

    dt = clock.tick(engine.fps)/1000.0
    pygame.display.flip()

