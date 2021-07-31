import random,pygame

class Particle():
    """Particle base class"""
    def __init__(self, x,y):
        self.x = x
        self.y = y
        self.vx = random.randint(0,20) / 10 - 1
        self.vy = random.randint(0,20) / 10 - 1
        self.lifetime = 5
        self.alive = True

    def update(self,dt, screen):
        self.x += self.vx
        self.y += self.vy
        self.lifetime -= 0.1

        pygame.draw.circle(screen, (200,200,200), (self.x,self.y), self.lifetime)
