from .. import Animal

class Reptile(Animal):
    def __init__(self, name: str, age: int) -> None:
        """Constructor of the Reptile class, calls the superclass constructor.

        Args:
            name (str): Name of the reptile.
            age (int): Age of the reptile.
        """
        super().__init__(name, age)
    
    def make_noise(self) -> str:
        """Returns a characteristic noise of a reptile.

        Returns:
            str: The noise that the reptile makes.
        """
        return 'I\'m a reptile'
    
    def move(self) -> str:
        """Describes how the reptile moves.

        Returns:
            str: A phrase describing the movement of a reptile.
        """
        return 'I\'m crawling'