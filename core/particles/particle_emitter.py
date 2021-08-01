from core.particles.emitter  import Emitter
from core.particles.particle import Particle


class ParticleEmitter(Emitter):
    """ParticleEmitter"""
    def __init__(self, x, y ):
        super().__init__(x,y)
        self.particles = []

        size = 100
        for x in range(size):
            p = Particle(self.x, self.y)
            self.particles.append(p)

    def load_particles(self):
        pass
        size = 10
        for x in range(size):
            p = Particle(self.x, self.y)
            self.particles.append(p)


    def update(self, dt, screen):
        for particle in self.particles:
            if not particle.alive:
                self.particles.remove(particle)
                pass

            particle.update(dt,screen)


