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


class Flying:
    def fly(self) -> str:
        """Describes how an animal flies.

        Returns:
            str: A string describing the animal flying.
        """
        return 'I\'m flying'


class Aquatic:
    def swin(self) -> str:
        """Describes how an aquatic animal swims.

        Returns:
            str: A string describing the animal swimming.
        """
        return "I'm swimming"


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

def add_new_habitat(zoo: Zoo):
    
    name = input("Type the name of the habitat: ")
    try:
        max_capacity = int(input("Type the maximum capacity: "))
        zoo.add_habitat(name=name, max_capacity=max_capacity)
    except ValueError:
        print("There must be an integer")


def add_animal_to_habitat(zoo: Zoo) -> None:
    """Prompts the user to add an animal to a specific habitat in the zoo.

    Args:
        zoo (Zoo): The zoo instance where the animal will be added.
    """
    zoo.show_habitats()
    habitat = int(input("Select one habitat: "))
    error = True
    while error:
        type = input("Select the type of the animal (mammal/bird/reptile/duck): ")
        if type in ["mammal", "bird", "reptile", "duck"]:
            error = False
    name = input("Type the animal's name: ")
    try:
        age = int(input("Type the animal's age: "))
        zoo.add_animal_to_habitat(animal_type=type, name=name, age=age, habitat=habitat)
    except ValueError:
        print("The age of the animal must be an integer!")


def move_animals_between_habitats(zoo: Zoo) -> None:
    """Allows moving animals between two habitats.

    Args:
        zoo (Zoo): The zoo instance.
    """
    if len(zoo.habitats) < 2:
        print("You must have at least 2 habitats")
    else:
        zoo.show_habitats()
        hab_1 = int(input("Select the habitat from which you want to move animals: "))
        hab_2 = int(input("Select the destination habitat: "))
        zoo.move_animals_between_habitats(hab_1, hab_2)

def delete_all_animals(zoo: Zoo) -> None:
    """Deletes all animals in all habitats.

    Args:
        zoo (Zoo): The zoo instance.
    """
    if len(zoo.habitats) == 0:
        print("You must have at least 1 habitat")
    else:
        zoo.delete_all_animals()


def do_habitats_operations(zoo: Zoo) -> None:
    """Provides a menu for habitat-related operations like moving animals or deleting all animals.

    Args:
        zoo (Zoo): The zoo instance.
    """
    while True:
        print("######## Habitats Operations ########")
        print("1. Move animals to another habitat")
        print("2. Delete all animals")
        print("3. Exit")
        option = int(input("Select which operation you want to do: "))

        match option:
            case 1:
                move_animals_between_habitats(zoo)
            case 2:
                delete_all_animals(zoo)
            case 3:
                print("See you!")
                break
            case others:
                print("Wrong choice!")


def menu(zoo: Zoo) -> None:
    """Main menu function, allows the user to interact with the zoo system.

    Args:
        zoo (Zoo): The zoo instance.
    """
    while True:
        print("1. Add habitat")
        print("2. Add animal to a habitat")
        print("3. Show all habitats")
        print("4. Count all animals in the zoo")
        print("5. Perform habitat operations")
        print("6. Exit")
        
        try:
            option = int(input("Choose one option: "))
            match option:
                case 1:
                    add_new_habitat(zoo=zoo)
                case 2:
                    add_animal_to_habitat(zoo=zoo)
                case 3:
                    zoo.show_all_habitats()
                case 4:
                    print(zoo.count_all_animals())
                case 5:
                    do_habitats_operations(zoo)
                case 6:
                    print('Goodbye!')
                    break
                case other:
                    print('That option does not exist')
        except ValueError:
            print("The option must be an integer")


def main() -> None:
    """Main function to start the zoo program."""
    zoo = Zoo()
    menu(zoo=zoo)


if __name__ == "__main__":
    main()