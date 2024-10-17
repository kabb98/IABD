
from modules.animals import Animal

class Habitat:
    def __init__(self, name: str, max_capacity: int) -> None:
        """Constructor of the Habitat class, initializes the habitat's name and capacity.

        Args:
            name (str): The name of the habitat.
            max_capacity (int): The maximum number of animals the habitat can hold.
        """
        self.name = name
        self.max_capacity = max_capacity
        self.animals = []

    def add_animal(self, animal: Animal) -> None:
        """Adds an animal to the habitat if capacity is not exceeded.

        Args:
            animal (Animal): The animal to add.
        """
        if len(self.animals) < self.max_capacity:
            self.animals.append(animal)
        else:
            print("The capacity of the habitat is completed")
    
    def show_animals(self) -> None:
        """Displays all the animals in the habitat."""
        print(f"######## Animals of the habitat {self.name} ########")
        for animal in self.animals:
            print(animal)
        print("")
    
    def count_animals(self) -> int:
        """Counts the number of animals in the habitat.

        Returns:
            int: The number of animals.
        """
        return len(self.animals)
    
    def count_combined_animals(self, o_habitat) -> int:
        """Counts the total number of animals from two habitats.

        Args:
            o_habitat (Habitat): Another habitat to combine with.

        Returns:
            int: The combined total number of animals.
        """
        return self.count_animals() + o_habitat.count_animals()
    
    def __str__(self) -> str:
        """String representation of the habitat.

        Returns:
            str: The habitat name and its maximum capacity.
        """
        return f'Habitat: {self.name}, Max Capacity: {self.max_capacity}'
    
    def move_animals(self, o_habitat):
        """Moves all animals from the current habitat to another habitat.

        Args:
            o_habitat (Habitat): The destination habitat.
        """
        for animal in self.animals[:]:
            o_habitat.add_animal(animal)
            self.animals.remove(animal)

    def delete_all_animals(self):
        """Deletes all animals from the habitat."""
        self.animals.clear()