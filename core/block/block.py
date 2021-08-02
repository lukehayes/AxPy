
class Block:
    """Base class for a block."""
    def __init__(self, x, y, r = 255, g = 0, b = 255, width = 10, height = 10 ):
        self.speed = 5
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.r = r
        self.g = g
        self.b = b
        self.alive = True

