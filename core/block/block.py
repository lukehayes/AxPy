
class Block:
    """Base class for a block."""
    def __init__(self, x, y):
        self.speed = 5
        self.x = x
        self.y = y
        self.width = 10
        self.height = 10
        self.r = 255
        self.g = 0
        self.b = 255
        self.alive = True

