from modules.place import Zoo
from modules import menu
from modules.animals.aves import Bird

def main() -> None:
    """Main function to start the zoo program."""
    zoo = Zoo()
    menu(zoo=zoo)


if __name__ == "__main__":
    # main()
    bird = Bird(name='Piolin', age=2)