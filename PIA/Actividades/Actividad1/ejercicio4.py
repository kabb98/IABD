
def menu():
    """Show the menu.
    Returns:
        int: The option selected by the user.
    """
    print("1. Calculate IMC")
    print("2. Exit")

    opcion = int(input("Select an option: "))
    return opcion


def calculate_imc(weight: float, height: float):
    """Calculate the IMC of a person
    
    Args:
        weight (float): The weight of the person in kilograms
        height (float): The height of the person in meters
    
    Returns:
        None
    """
    imc = weight / (height ** 2)

    if imc < 18.5:
        print("Your weight is low")
    elif imc >= 18.5 and imc <= 24.9:
        print("You are in a good weight")
    elif imc >= 25 and imc <= 29.9:
        print("You are overweight")
    elif imc >= 30:
        print("You have obesity")

def main():
    while True:
        opcion = menu()

        if opcion == 1:
            try:
                weight = float(input("Insert your weight in kilograms: "))
                height = float(input("Insert your height in meters: "))
                calculate_imc(weight=weight, height=height)
            except ValueError:
                print("The number must be integer")
        elif opcion == 2:
            print("See you later!!")
            break
        else:
            print("That option doesn't exist")
            
if __name__ == "__main__":
    main()