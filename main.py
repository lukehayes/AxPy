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
engine = Engine(1024, 768)

screen = pygame.display.set_mode((engine.width, engine.height), pygame.RESIZABLE)
pygame.display.set_caption('Physics')
screen.fill(engine.bg_color)
pygame.display.flip()
running = True


c = 0

dt = 0
clock  = pygame.time.Clock()


blocks = []

anim = AnimatedSprite("python.png")

for x in range(50):
    row = []
    for y in range(50):
        b = Block(x * SPACE,y * SPACE)
        b.r = 100
        row.append(b)

    blocks.append(row)


def iterate(x,y):
    block = blocks[x][y]
    block.alive = True

    if block.alive:
        block.r = 255

    return block



s = Sprite("python.png", 100,100)
r = pygame.Rect(30,0,100,100)
ss = s.image.subsurface(r)


print(ss)

while running:
    c = c + 0.01
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(engine.bg_color)

    anim.play(10, c)

    # screen.blit(ss, r)
    # screen.blit(anim.image, anim.rect)

    # drawSprite(screen, s)
    # drawSprite(screen, ss)


    dt = clock.tick(engine.fps)/1000.0
    pygame.display.flip()

