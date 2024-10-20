from .place.Zoo import Zoo

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