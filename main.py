import pygame
import math
from core.block import Block
from core.block import Grid
from core.gfx import draw,drawBlock
from core.engine import Engine

SPACE = 6
engine = Engine(800,600)

screen = pygame.display.set_mode((engine.width, engine.height))
pygame.display.set_caption('Physics')
screen.fill(engine.bg_color)
pygame.display.flip()
running = True

c = 0

b = Block(10,10)
gridObject= Grid(10,10)
grid = gridObject.create()

dt = 0
clock  = pygame.time.Clock()

while running:
    c = c + 0.01
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    print(dt)
    screen.fill(engine.bg_color)

    for x in range(len(grid)):
        row = grid[x]
        for y in range(len(row)):
            drawBlock(screen, grid[x][y])


    dt = clock.tick(engine.fps)/1000.0
    pygame.display.flip()
