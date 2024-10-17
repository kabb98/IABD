from modules.place import Zoo
from modules import menu

def main() -> None:
    """Main function to start the zoo program."""
    zoo = Zoo()
    menu(zoo=zoo)


if __name__ == "__main__":
    main()