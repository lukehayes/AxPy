
class Entity(object):
    """Entity base class"""
    def __init__(self):
        ''
        self.components = {}

    def add_component(self, key, component):
        """Add a component to the Entity class"""
        self.components[key] = component


    def update(self):

        for k,comp in self.components.items():
            comp.update(12)
        pass


