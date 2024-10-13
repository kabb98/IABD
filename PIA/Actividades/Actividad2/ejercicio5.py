class Person:
    """Class Person
    """
    
    def __init__(self, name: str, age: int) -> None:
        """Constructor of Person class

        Args:
            name (str): Name of the person
            age (int): Age of the person
        """
        self.name = name
        self.age = age
    
    def show_info(self) -> None:
        """Shows the info of the person, its name and age
        """
        print(f'Name: {self.name}')
        print(f'Age: {self.age}')
    

class Employee(Person):
    """Class Employee

    Args:
        Person (Person): It is the class from which it inherits
    """
    
    def __init__(self, name: str, age: int, salary: float) -> None:
        """ Constructor of Employee class

        Args:
            name (str): Name of the employee
            age (int): Age of the employee
            salary (float): Salary of the employee
        """
        super().__init__(name, age)
        self.salary = salary
    
    def show_info(self) -> None:
        """Shows the info of the employee, its name, age and salary
        """
        super().show_info()
        print(f'Salary: {self.salary}')

class Executive(Employee):
    """Class Executive

    Args:
        Employee (Employee): It is the class from which it inherits
    """

    def __init__(self, name: str, age: int, salary: float, departament: str) -> None:
        """ Constructor of Executive class

        Args:
            name (str): Name of the executive
            age (int): Age of the executive
            salary (float): Salary of the executive
            departament(str): Departament of the executive
        """
        super().__init__(name, age, salary)
        self.departament = departament
    
    def show_info(self) -> None:
        """Shows the info of the executive, its name, age, salary and departament.
        """
        super().show_info()
        print(f'Departament: {self.departament}')
    
    def assign_departament(self, new_departament: str) -> None:
        """Change the departament of the executive.
        Args:
            departament(str): New departament of the executive
        """
        self.departament = new_departament


def main():
    person = Person('Kenny', 25)
    person.show_info()
    
    employee = Employee('Raul', 25, 5000)
    employee.show_info()
    
    directivo = Executive('Toni', 35, 10000, 'Software Development')
    directivo.show_info()

    directivo.assign_departament('Database Management')
    directivo.show_info()


if __name__ == '__main__':
    main()