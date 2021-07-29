
class Grid():
    """docstring for Grid"""

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def update(self):
        """docstring for update"""
        print("Updating Grid")

    def render(self):
        """docstring for update"""
        print("Rendering Grid")

    def create(self, x, y):
        grid = dict()

        for xx in range(x):
            d = dict()
            for yy in range(y):
                block = Block(xx * 11, yy * 11)
                d.append(b)

            grid.append(d)



