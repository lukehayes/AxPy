import pygame
import math

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

    for x in range(10):
        for y in range(10):
            pygame.draw.line(screen, pygame.Color(100,0,100), (x * 100, math.cos(c) * 100), (200 + y * 100, 100), 1)
    pygame.display.flip()
