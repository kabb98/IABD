from modules.animals import Animal
from ..others import Flying, Aquatic

class Duck(Animal, Flying, Aquatic):
    def __init__(self, name: str, age: int) -> None:
        """Constructor of the Duck class, calls the superclass constructor.

        Args:
            name (str): Name of the duck.
            age (int): Age of the duck.
        """
        super().__init__(name, age)

    def move(self) -> str:
        """Describes how the duck moves.

        Returns:
            str: A phrase describing the duck's movement.
        """
        return "I'm a duck and I'm walking"

    def fly(self) -> str:
        """Describes how the duck flies.

        Returns:
            str: A phrase describing the duck's flight.
        """
        return "I'm a duck and I'm flying"
    
    def make_noise(self) -> str:
        """Returns a characteristic noise of a duck.

        Returns:
            str: The noise that the duck makes.
        """
        return "Cuack Cuack"
