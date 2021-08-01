import pygame
import math
from core.block import Block
from core.block import Grid
from core.gfx import draw,drawBlock
from core.engine import Engine
from core.particles import ParticleEmitter
from core.particles import Particle
import random

SPACE = 6
engine = Engine(1024, 768)

screen = pygame.display.set_mode((engine.width, engine.height), pygame.RESIZABLE)
pygame.display.set_caption('Physics')
screen.fill(engine.bg_color)
pygame.display.flip()
running = True


c = 0

b = Block(10,10)
dt = 0
clock  = pygame.time.Clock()

emitters = []
particles = ParticleEmitter(150,650)

for x in range(1,10):
    e = ParticleEmitter(
        random.randint(10,1000),
        random.randint(10,700)
    )

emitters.append(e)

while running:
    c = c + 0.01
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(engine.bg_color)

    particles.update(dt,screen)

    dt = clock.tick(engine.fps)/1000.0
    pygame.display.flip()

