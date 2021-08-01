import random,pygame

class Particle():
    """Particle base class"""
    def __init__(self, x,y):
        self.x = x
        self.y = y
        self.vx = random.randint(0,20) / 10 - 1
        self.vy = random.randint(0,20) / 10 - 1
        self.r = random.randint(1,255)
        self.g = random.randint(1,255)
        self.b = random.randint(1,255)
        self.lifetime = 5
        self.alive = True

    def update(self,dt, screen):
        self.x += self.vx
        self.y += self.vy
        self.lifetime -= 0.1

        if self.lifetime <= 0:
            self.alive = False

        pygame.draw.circle(screen, (self.r, self.g,self.b), (self.x,self.y), self.lifetime)
