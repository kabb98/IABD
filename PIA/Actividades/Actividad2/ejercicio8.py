from abc import ABC, abstractmethod

class Animal(ABC):

    def __init__(self, name: str, age: int) -> None:
        """Constructor of the Animal class

        Args:
            name (str): The name of the animal
            age (int): The age of the animal
        """
        if self.check_name(name=name):
            self.name = name 
            self.age = age
        else:
            print(f"The name is incorrect or empty")

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

    def __str__(self) -> str:
        """Return the str of the animal object

        Returns:
            str: The str with the name and age
        """
        return f'Name: {self.name}, Age: {self.age}'
    
    def check_name(self, name: str) -> bool:
        return len(name) != 0 and type(name) == str


class Flying:
    def fly(self) -> str:
        """Describes how the a animal flies.

        Returns:
            str: The fly phrase for an animal.
        """
        return 'I\'m flying'

        

class Aquatic:
    def swin(self):
        return "I'm swimming"


class Habitat:

    def __init__(self, name: str, max_capacity: int) -> None:
        self.name = name
        self.max_capacity = max_capacity
        self.animals = []

    def add_animal(self, animal: Animal) -> None:
        if len(self.animals) < self.max_capacity:
            self.animals.append(animal)
        else:
            print("There capacity of the habitat is completed")
    
    def show_animals(self) -> None:
        """Shows all the animals of the habitat (nam and age)
        """
        print(f"################ Animals of the habitat: {self.name} ################")
        for animal in self.animals:
                print(animal)

        print("")
    
    def count_animals(self) -> int:
        return len(self.animals)
    
    # Operaciones combinadas
    def count_combined_animals(self, o_habitat) -> int:
        return self.count_animals() + o_habitat.count_animals()





class Mammal(Animal):

    def __init__(self, name: str, age: int) -> None:
        """Constructor of the mammal class, this function invokes the superclass constructor.

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
            str: The movement phrase for a mammal.
        """
        return 'I\'m walking'


class Bird(Animal, Flying):
    def __init__(self, name: str, age: int) -> None:
        """Constructor of the bird class, calls the superclass constructor.

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
            str: The movement phrase for a bird.
        """
        return 'I\'m a bird and I\'m moving'
    
    
    


class Reptile(Animal):
    def __init__(self, name: str, age: int) -> None:
        """Constructor of the reptile class, calls the superclass constructor.

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
            str: The movement phrase for a reptile.
        """
        return 'I\'m crawling'


class Duck(Animal, Flying, Aquatic):
    def __init__(self, name: str, age: int) -> None:
        super().__init__(name, age)

    def move(self):
        return "I'm a duck and I'm walking"

    def fly(self):
        return "I'm a duck and I'm flying"
    
    




class Zoo:
    def __init__(self) -> None:
        """Constructor of the class Zoo, inicializate the list of the animals
        """
        self.animals = []
    
    def add_animal(self, animal_type: str, name: str, age: int) -> None:
        """Add a new animal to the list

        Args:
            animal_type (str): Type of the animakl
            name (str): Name of the animal
            age (int): Age of the animal
        """
        
        if  animal_type.lower() == 'mammal':
            animal = Mammal(name=name, age=age)
        elif animal_type.lower() == 'bird':
            animal = Bird(name=name, age=age)
        elif animal_type.lower() == 'reptile':
            animal = Reptile(name=name, age=age)
        else:
            print("That type doesn't exist")
            return

        self.animals.append(animal)
    

    def show_animals(self) -> None:
        """Shows all the animals (name, age and type)
        """
        print("################ Zoo Animals ################")
        for animal in self.animals:
            if isinstance(animal, Mammal):
                print(animal, ", Type: Mammal")
            elif isinstance(animal, Bird):
                print(animal, ", Type: Bird")
            elif isinstance(animal, Reptile):
                print(animal, ", Type: Reptile")
        
        print("")
    
    def make_noises(self) -> None:
        """This function allows the animals to make its own noise
        """
        print("################ Making Noises ################")
        for animal in self.animals:
            print(animal.make_noise())
        print("")

    def move_animals(self) -> None:
        """This function allows the animals to move
        """
        print("################ Moving Animals ################")
        for animal in self.animals:
            print(animal.move())
        print("")



def add_animal(zoo: Zoo) -> None:
    """This function allows the user to add a new animal to the zoo

    Args:
        zoo (Zoo): The zoo where the animals will be stored
    """
    error = True
    while error:
        type = input("Select the type of the animal (mammal/bird/reptile): ")

        if type == "mammal" or type == "bird" or type == "reptile":
            error = False
    
    name = input("Type the animal's name: ")
    
    try:
        age = int(input("Type the animal's age: "))

        zoo.add_animal(animal_type=type, name=name, age=age)
    except ValueError:
        print("The age of the animal must be an integer!")


def menu(zoo: Zoo) -> None:
    """Menu function, allows to the user to do a few things

    Args:
        zoo (Zoo): The Zoo
    """
    while True:
        print("1. Add habitat")
        print("2. Add animal to an habitat")
        print("3. Show all habitats")
        print("4. Count all animals in the zoo")
        print("5. Do some habitats operations")
        print("6. Exit")
        
        try:
            option = int(input("Choose one option: "))

            match option:
                case 1:
                    add_animal(zoo=zoo)
                case 2:
                    zoo.show_animals()
                case 3:
                    zoo.make_noises()
                case 4:
                    zoo.move_animals()
                case 5:
                    print('Goodbye!')
                    break
                case other:
                    print('That option does not exist')
        except ValueError:
            print("The option must be an integer")


def main():
    """Main function
    """
    zoo = Zoo()
    menu(zoo=zoo)

if __name__ == "__main__":
    main()