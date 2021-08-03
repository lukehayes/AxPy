from opensimplex import OpenSimplex
import random

class Noise(object):

    @classmethod
    def noise2D(cls, x,y):
        """
        Create 2D noise.

        Args:
            cls (object): The initial value
            x   (int)   : The starting value
            y   (int)   : The ending value

        Returns:
            Float: Simplex noise value for x and y.
        """
        os = OpenSimplex()
        return os.noise2d(x,y)

