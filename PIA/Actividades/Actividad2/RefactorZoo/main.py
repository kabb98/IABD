from modules.place.Zoo import Zoo
from modules import menu

def main() -> None:
    """Main function to start the zoo program."""
    zoo = Zoo()
    menu.menu(zoo=zoo)


if __name__ == "__main__":
    main()