from opensimplex import OpenSimplex
import random

class Noise(object):

    @classmethod
    def noise2D(cls, x,y, seed = 0):
        """
        Create 2D noise.

        Args:
            cls  (object): The initial value
            x    (int)   : The starting value
            y    (int)   : The ending value
            seed (int)   : The seed optional seed value for OpenSimplex

        Returns:
            Float: Simplex noise value for x and y.
        """
        os = OpenSimplex(seed)
        return os.noise2d(x,y)

