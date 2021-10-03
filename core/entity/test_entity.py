import pygame
import random as r

class TestEntity(object):

    def __init__(self):
        self.x = r.randint(10,800)
        self.y = r.randint(10,600)
        self.dx = 1
        self.dy = 1
        self.speed = r.randint(3,20)
        self.r = r.randint(20,255)
        self.g = r.randint(20,255)
        self.b = r.randint(20,255)

        print("Here " + str(self.x))


    def update(self, dt):

        self.x += self.dx * self.speed * dt
        self.y += self.dy * self.speed * dt

        if self.x > 800 or self.x < 0:
            self.dx = -self.dx

        if self.y > 600 or self.y < 0:
            self.dy = -self.dy

    def draw(self, screen):
        pygame.draw.rect(screen, (self.r, self.g, self.b), (self.x, self.y, 10,10))

