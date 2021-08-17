from core.component.component import Component

class Health(Component):
    """
    Health component

    """
    def __init__(self, start_value = 100):
        super().__init__()
        self.start_value = start_value

    def update(self, delta):
        print("Updating Health")
        pass
