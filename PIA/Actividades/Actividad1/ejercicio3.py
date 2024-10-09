
def menu():
    """Show the menu.
    Returns:
        int: The option selected by the user.
    """
    print("1. Obtain table of multiply")
    print("2. Exit")

    opcion = int(input("Select an option: "))
    return opcion


def obtain_multiplication_table(n: int):
    """Obtain the multiplication of a number between 1 and 10
    
    Args:
        n (int): The number that we want its multiplication table
    
    Returns:
        None
    """
    for i in range(11):
        print(f"{n} * {i} = {i*n}")

def main():
    while True:
        opcion = menu()

        if opcion == 1:
            try:
                n = int(input("Type the number to obtain its multiplication table: "))
                if n < 1 or n > 10:
                    print("The number must be between 1 and 10")
                else:
                    obtain_multiplication_table(n)
            except ValueError:
                print("The number must be integer")
        elif opcion == 2:
            print("See you later!!")
            break
        else:
            print("That option doesn't exist")
            
if __name__ == "__main__":
    main()