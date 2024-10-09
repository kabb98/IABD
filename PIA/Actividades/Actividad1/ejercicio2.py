
def menu():
    """Show the menu.
    Returns:
        int: The option selected by the user.
    """
    print("1. Convert meters to kilometer")
    print("2. Convert pounds to kilogram")
    print("3. Convert Celcius to Fahrenheit")
    print("4. Exit")

    opcion = int(input("Select an option: "))
    return opcion


def meters_to_kilometers(n: float):
    """Obtains the kilometers from meters
    
    Args:
        n (float): The number of meters
    
    Returns:
        float: The number of kilometers
    """

    return n / 1000

def pounds_to_kilogram(n: float):
    """Obtains the kilograms from pounds
    Args:
        n (float): The number of pounds
    
    Returns:
        float: The number of kilograms
    """
    pound_factor = 0.453592
    return n * pound_factor 

def celcius_to_farhrenheit(n: float):
    """Obtains the fahrenheit degrees from celsius degrees.
    Args:
        n (float): The number of celsius degrees
        
        Returns:
        float: The number of fahrenheit degrees
    """
    return n * 9/5 + 32


def main():
    while True:
        opcion = menu()

        if opcion == 1:
            try:
                n = float(input("Enter the number of meters: "))
                print(f"There are {meters_to_kilometers(n)} kilometers.")
            except ValueError:
                print("The number must be float")
        elif opcion == 2:
            try:
                n = float(input("Enter the amount of pounds: "))
                print(f"There are {pounds_to_kilogram(n)} kilograms.")
            except ValueError:
                print("The number must be float")
        elif opcion == 3:
            try:
                n = float(input("Enter the celsius value: "))
                print(f"There are {celcius_to_farhrenheit(n)} ºF.")
            except ValueError:
                print("The number must be float")
        elif opcion == 4:
            print("See you later!!")
            break
        else:
            print("That option doesn't exist")

if __name__ == "__main__":
    main()