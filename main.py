import pygame
import math
from core.block import Block
from core.gfx import draw

SPACE = 6
GRID_X = 50
GRID_Y = 50
background_colour = (0,0,0)
(width, height) = (800, 600)

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Physics')
screen.fill(background_colour)
pygame.display.flip()
running = True

c = 0

b = Block()

while running:
    c = c + 0.01
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(background_colour)
    pygame.draw.rect(screen, pygame.Color(b.r, b.g, b.b), pygame.Rect(10,10, b.width, b.height))
    draw(screen,100,100,23,200)
    draw(screen,200,130,230,100)

    pygame.display.flip()
