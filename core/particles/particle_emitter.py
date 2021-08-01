from core.particles.emitter  import Emitter
from core.particles.particle import Particle


class ParticleEmitter(Emitter):
    """ParticleEmitter"""
    def __init__(self, x, y ):
        super().__init__(x,y)
        self.particles = []

        size = 100
        for x in range(size):
            p = Particle(250,250)
            self.particles.append(p)

    def load_particles(self):
        pass
        size = 10
        for x in range(size):
            p = Particle(250,250)
            self.particles.append(p)




