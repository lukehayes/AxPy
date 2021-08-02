from core.block import Block
from core.gfx import drawBlock


class Grid():

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = []

    def update(self):
        """docstring for update"""
        print("Updating Grid")

    def render(self):
        """docstring for update"""
        print("Rendering Grid")

    def create(self):
        """Build the grid"""
        for x in range(self.width):
            row = []
            for y in range(self.height):
                block = Block(x * 11, y * 11)
                row.append(block)

            self.grid.append(row)

        return self.grid

    def draw(self, screen):
        """Draw the grid"""
        for row in self.grid:
            for block in row:
                drawBlock(screen, block)
