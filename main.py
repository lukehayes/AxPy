import pygame
import math

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

while running:
    c = c + 0.01
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(background_colour)

    for x in range(GRID_X):
        for y in range(GRID_Y):
            if x == 0 and y == 0:
                pygame.draw.rect(screen, pygame.Color(0,200,0), pygame.Rect(10 + x * SPACE, 10 + y * SPACE, 5,5))
            else:
                pygame.draw.rect(screen, pygame.Color(100,0,100), pygame.Rect(10 + x * SPACE, 10 + y * SPACE, 5,5))

            if x == GRID_X - 1 and y == GRID_Y - 1:
                pygame.draw.rect(screen, pygame.Color(200,0,0), pygame.Rect(10 + x * SPACE, 10 + y * SPACE, 5,5))
            else:
                pygame.draw.rect(screen, pygame.Color(100,0,100), pygame.Rect(10 + x * SPACE, 10 + y * SPACE, 5,5))

    pygame.display.flip()
