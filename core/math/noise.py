from opensimplex import OpenSimplex

class Noise(object):

    @classmethod
    def noise(cls, x,y):
        os = OpenSimplex()
        return os.noise2d(x,y)

