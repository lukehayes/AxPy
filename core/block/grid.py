from core.block import Block


class Grid():
    """docstring for Grid"""

    def __init__(self, width, height):
        """Constructor"""
        """
        Parameters
        ----------
        width : int
            The WIDTH size of the grid.
        height : int
            The HEIGHT size of the grid.
        """
        self.width = width
        self.height = height

    def update(self):
        """docstring for update"""
        print("Updating Grid")

    def render(self):
        """docstring for update"""
        print("Rendering Grid")

    def create(self):
        """Build the grid"""
        """
        Returns
        ----------
        List
            A grid of pre built block types.
        """
        grid = []

        for x in range(self.width):
            row = []
            for y in range(self.height):
                block = Block(x * 11, y * 11)
                row.append(block)

            grid.append(row)

        return grid


    def draw(self):
        pass
