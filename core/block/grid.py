from core.block import Block


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

    def create(self):
        """Create an X by Y size grid"""
        """
        Parameters
        ----------
        x : int
            The X size of the grid.
        y : int
            The Y size of the grid.

        Returns
        ----------
        Dict
            A grid of pre built block types.
        """
        grid = dict()

        for x in range(self.width):
            d = dict()
            for y in range(self.height):
                block = Block(x * 11, y * 11)
                d.append(b)

            grid.append(d)

        return grid


    def draw(self):
        pass
