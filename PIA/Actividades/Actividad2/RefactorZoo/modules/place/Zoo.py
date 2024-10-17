from . import Habitat

from modules.animals.others import Mammal, Reptile
from modules.animals.aves import Bird, Duck

class Zoo:
    def __init__(self) -> None:
        """Constructor of the Zoo class, initializes the list of habitats."""
        self.habitats = []
    
    def add_habitat(self, name: str, max_capacity: int) -> None:
        """Adds a new habitat to the zoo.

        Args:
            name (str): Name of the habitat.
            max_capacity (int): Maximum capacity of the habitat.
        """
        nuevo = Habitat(name=name, max_capacity=max_capacity)
        self.habitats.append(nuevo)
    
    def add_animal_to_habitat(self, animal_type: str, name: str, age: int, habitat: int) -> None:
        """Adds a new animal to the specified habitat.

        Args:
            animal_type (str): Type of the animal (mammal, bird, reptile, duck).
            name (str): Name of the animal.
            age (int): Age of the animal.
            habitat (int): The habitat number to place the animal in.
        """
        if  animal_type.lower() == 'mammal':
            animal = Mammal(name=name, age=age)
        elif animal_type.lower() == 'bird':
            animal = Bird(name=name, age=age)
        elif animal_type.lower() == 'reptile':
            animal = Reptile(name=name, age=age)
        elif animal_type.lower() == 'duck':
            animal = Duck(name=name, age=age)
        else:
            print("That type doesn't exist")
            return

        self.habitats[habitat-1].add_animal(animal)
    
    def show_all_habitats(self) -> None:
        """Displays all the habitats and their animals."""
        print("################ Zoo Animals ################")
        for habitat in self.habitats:
            habitat.show_animals()
        print("")
    
    def show_habitats(self) -> None:
        """Displays all habitats in the zoo."""
        print("################ Zoo Habitats ################")
        for i, habitat in enumerate(self.habitats):
            print(f'{i+1}. {habitat}')
        print("")
    
    def count_all_animals(self) -> int:
        """Counts all animals in the zoo across all habitats.

        Returns:
            int: The total number of animals in the zoo.
        """
        res = 0
        for habitat in self.habitats:
            res += habitat.count_animals()
        return res
    
    def move_animals_between_habitats(self, h1: int, h2: int) -> None:
        """Moves animals between two habitats.

        Args:
            h1 (int): Source habitat number.
            h2 (int): Destination habitat number.
        """
        self.habitats[h1-1].move_animals(self.habitats[h2-1])
    
    def delete_all_animals(self) -> None:
        """Deletes all animals from the zoo's habitats."""
        for habitat in self.habitats:
            habitat.delete_all_animals()