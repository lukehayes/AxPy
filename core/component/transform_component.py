from core.component.component import Component

class TransformComponent(Component):
    """
    Transform component

    Class only supports x and y position for now.

    """
    def __init__(self, x = 0, y = 0):
        super().__init__()

    def update(self, detla):
        print("Updating Transform")
        pass
