from abc import ABC, abstractmethod

class Component(ABC):
    """Base class for all components."""

    def __init__(self):
        pass

    @abstractmethod
    def update(self, delta):
        """
        Update the component

        Abstract Method

        Args:
            delta (Float): Delta time.

        Returns:
            None
        """
        pass
