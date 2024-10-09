
def menu():
    """Show the menu.
    Returns:
        int: The option selected by the user.
    """
    print("1. Check if number is prime")
    print("2. Range of prime numbers")
    print("3. Exit")

    opcion = int(input("Select an option: "))
    return opcion
    

def is_prime(num):
    if num < 2:
        return False
    
    for i in range(2, num):
        if num % i == 0:
            return False
    
    return True

def prime_range(n1, n2):
    primos = []

    for i in range(n1, n2+1):
        if is_prime(i):
            primos.append(i)
    
    print(f"The range of prime numbers for {n1} and {n2} is:")
    for p in primos:
        print(f"{p}", end='-')
    print("")
    
    

def main():

    while True:
        opcion = menu()

        if opcion == 1:
            try:
                num = int(input("Insert a number: "))
                if is_prime(num=num):
                    print(f'The number {num} is prime')
                else:
                    print(f'The number {num} is not prime')
            except ValueError:
                print("The number must be integer")
            
        elif opcion == 2:
            try:
                n1 = int(input("Insert the first number: "))
                n2 = int(input("Insert the second number: "))
            except ValueError:
                print("The number must be integer")
            prime_range(n1, n2)
        elif opcion == 3:
            print("See you later!!")
            break
        else:
            print("That option doesn't exist")

if __name__ == "__main__":
    main()