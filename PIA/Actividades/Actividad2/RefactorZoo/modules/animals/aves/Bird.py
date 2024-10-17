from .. import Animal
from ..others import Flying

class Bird(Animal, Flying):
    def __init__(self, name: str, age: int) -> None:
        """Constructor of the Bird class, calls the superclass constructor.

        Args:
            name (str): Name of the bird.
            age (int): Age of the bird.
        """
        super().__init__(name, age)
    
    def make_noise(self) -> str:
        """Returns a characteristic noise of a bird.

        Returns:
            str: The noise that the bird makes.
        """
        return 'I\'m a bird'
    
    def move(self) -> str:
        """Describes how the bird moves.

        Returns:
            str: A phrase describing the movement of a bird.
        """
        return 'I\'m a bird and I\'m moving'

