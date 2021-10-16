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

# Pygame Setup
pygame.init()
monitor_size = pygame.display.Info()
engine = Engine(int(monitor_size.current_w / 2), int(monitor_size.current_h / 2))
screen = pygame.display.set_mode((engine.width, engine.height), pygame.RESIZABLE)
pygame.display.set_caption('Physics')
screen.fill(engine.bg_color)
pygame.display.flip()
running = True

# Delta Time
dt = 0
clock  = pygame.time.Clock()

# Sprites
p = AnimatedSprite("spritesheet.png", screen, x = 100, y = 100, xTuple = (0,5), yTuple = (0,0))
p2 = AnimatedSprite("spritesheet.png", screen, x = 100, y = 100, xTuple = (0,5), yTuple = (1,0))

# Speed, Movement, Velocity
c = 0
speed = 1
movement = 1
vel = pygame.math.Vector2(0.1,0.1)
maxVelocity = 20
minVelocity = 0
current_speed_x = 0
current_speed_y = 0
xDir = 1
yDir = 1

# KeyDown Checks
leftPressed = False;
rightPressed = False;
upPressed = False;
downPressed = False;

while running:

    c += speed * dt

    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

        # Key Down Checks
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pygame.quit()

            if event.key == pygame.K_a:
                leftPressed = True
            if event.key == pygame.K_d:
                rightPressed = True
            if event.key == pygame.K_w:
                upPressed = True
            if event.key == pygame.K_s:
                downPressed = True

        # Key Up Checks
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_q:
                pygame.quit()
            if event.key == pygame.K_a:
                leftPressed = False
            if event.key == pygame.K_d:
                rightPressed = False
            if event.key == pygame.K_w:
                upPressed = False
            if event.key == pygame.K_s:
                downPressed = False

    # Starting Speed of 0
    # When key is pressed down, increment by a value until max is reached
    # Keep speed at max whilst key held down
    # When key released, decrement the speed until reached 0

    if leftPressed:
        vel.x += 1 * speed
        if vel.x > maxVelocity:
            vel.x = maxVelocity
    else:
        vel.x -= 1 * speed
        if vel.x < 0:
            vel.x = 0

    if rightPressed:
        vel.x -= 1 * speed
        if vel.x < -maxVelocity:
            vel.x = -maxVelocity
    else:
        vel.x += 1 * speed
        if vel.x < 0:
            vel.x = 0

    # if rightPressed:
        # current_speed_x -= xDir * speed * dt
    # else:
        # current_speed_x += xDir * speed * dt


    if upPressed:
        print("Up Down")
    if downPressed:
        print("Down Down")

    p.x += vel.x
    p.y += vel.y

    screen.fill(engine.bg_color)

    p.update(dt)
    p.draw()

    dt = clock.tick(engine.fps)/1000.0
    pygame.display.flip()

