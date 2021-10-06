import pygame
import math
import random
from core.engine import Engine
from core.component import ComponentManager

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

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pygame.quit()

    dt = clock.tick(engine.fps)/1000.0
    pygame.display.flip()

