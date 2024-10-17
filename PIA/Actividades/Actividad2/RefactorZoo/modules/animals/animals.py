from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name: str, age: int) -> None:
        """Constructor of the Animal class, initializes the name and age of the animal.

        Args:
            name (str): The name of the animal.
            age (int): The age of the animal.

        Raises:
            ValueError: If the name is incorrect or empty.
        """
        if self.check_name(name=name):
            self.name = name 
            self.age = age
        else:
            raise ValueError(f"The name is incorrect or empty")

    @abstractmethod
    def make_noise(self):
        """Abstract method that makes a noise characteristic of each animal."""
        pass

    @abstractmethod
    def move(self):
        """Abstract method that defines the movement of each animal."""
        pass

    def __str__(self) -> str:
        """Returns a string representation of the animal object.

        Returns:
            str: The name and age of the animal.
        """
        return f'Name: {self.name}, Age: {self.age}'
    
    def check_name(self, name: str) -> bool:
        """Validates the name of the animal.

        Args:
            name (str): The name to check.

        Returns:
            bool: True if the name is valid, False otherwise.
        """
        return len(name) != 0 and type(name) == str