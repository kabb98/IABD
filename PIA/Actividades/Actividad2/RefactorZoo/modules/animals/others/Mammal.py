from modules.animals.animals import Animal

class Mammal(Animal):
    def __init__(self, name: str, age: int) -> None:
        """Constructor of the Mammal class, calls the superclass constructor.

        Args:
            name (str): Name of the mammal.
            age (int): Age of the mammal.
        """
        super().__init__(name, age)
    
    def make_noise(self) -> str:
        """Returns a characteristic noise of a mammal.

        Returns:
            str: The noise that the mammal makes.
        """
        return 'I\'m a mammal'
    
    def move(self) -> str:
        """Describes how the mammal moves.

        Returns:
            str: A phrase describing the movement of a mammal.
        """
        return 'I\'m walking'