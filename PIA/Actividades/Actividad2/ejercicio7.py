from abc import ABC, abstractmethod

class Animal(ABC):

    def __init__(self, name: str, age: int) -> None:
        """Constructor of the Animal class

        Args:
            name (str): The name of the animal
            age (int): The age of the animal
        """
        self.name = name
        self.age = age

    @abstractmethod
    def make_noise(self):
        """Abstract function that make a noise of each animal
        """
        pass

    @abstractmethod
    def move(self):
        """Abstract function that make a move of each animal
        """
        pass


class Mammal(Animal):

    def __init__(self, name: str, age: int) -> None:
        super().__init__(name, age)
    
    def make_noise(self) -> str:
        return 'I\'m a mammal'
    
    def move(self) -> str:
        return 'I\'m walking'

class Bird(Animal):
    def __init__(self, name: str, age: int) -> None:
        super().__init__(name, age)
    
    def make_noise(self) -> str:
        return 'I\'m a bird'
    
    def move(self) -> str:
        return 'I\'m flying'
    


class Reptile(Animal):
    def __init__(self, name: str, age: int) -> None:
        super().__init__(name, age)
    
    def make_noise(self) -> str:
        return 'I\'m a reptile'
    
    def move(self) -> str:
        return 'I\'m crawling'

class Zoo:
    def __init__(self) -> None:
        self.animals = []
    
    def add_animal(self, animal: Animal) -> None:
        self.animals.append(animal)
