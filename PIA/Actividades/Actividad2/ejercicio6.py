class Contact:

    def __init__(self, phone: int, name: str) -> None:
        """Constructor of Contact class

        Args:
            phone (int): Phone of the contact
            name (str): Name of the contact
        """
        self.phone = phone
        self.name = name
    
    def update_phone(self, new_phone: int) -> None:
        """This functions allows to update the phone number of the contact

        Args:
            new_phone (int): The new phone number
        """
        self.phone = new_phone
    
    def __str__(self) -> str:
        """This function allows to print the contact object

        Returns:
            str: Name and phone number
        """
        return f'Name: {self.name}, Phone: {self.phone}'
    

class AddressBook:

    def __init__(self) -> None:
        """Constructor of Address Book, initialize the contacts list
        """
        self.contacts = []
    
    def add_contact(self, contact: Contact) -> None:
        """This function allows to add a new contact to the list

        Args:
            contact (Contact): The contact to add
        """
        self.contacts.append(contact)
    
    def delete_contact(self, contact_name: str) -> None:
        """This function allows to delete a contact by its name

        Args:
            contact_name (str): The name of the contact to delete
        """
        for contact in self.contacts:
            if contact.name == contact_name:
                self.contacts.remove(contact)
                print("You have deleted the contact!")
                return
        
        print(f'There are no contacts to delete by the name {contact_name}')

    def update_phone_number(self, idx: int, phone_number: int) -> None:
        """Function to update the phone number, we use the index

        Args:
            idx (int): The index of the contact
            phone_number (int): New phone number
        """
        try:
            self.contacts[idx].update_phone(phone_number)
        except IndexError:
            print("You have to choose a contact of the list")

    def search_by_name(self, name: str) -> None:
        """This function allows to search a contact by its name

        Args:
            name (str): The name of the contact to search
        """
        for contact in self.contacts:
            if contact.name == name:
                print(contact)
                return
        
        print(f'There is no contact with the name {name}')
    
    def show_all_contacts(self) -> None:
        """This function shows all the contacts that the address book has stored
        """
        if len(self.contacts) < 1:
            print(f'There are no contacts')
            return
        
        print("######### Address Book #########")
        for i, contact in enumerate(self.contacts):
            print(f'{i + 1}. {contact}')
        print("")


def add_new_contact(agenda: AddressBook):
    """This function calls to the address book function
    to the add a new contact

    Args:
        agenda (AddressBook): The address book
    """
    name = input("Type the name of the contact: ")
    try:
        phone = int(input("Type the phone of the contact: "))
        contact = Contact(phone=phone, name=name)
        agenda.add_contact(contact=contact)
    except ValueError:
        print("The phone number must be just numbers!")


def delete_contact(agenda: AddressBook):
    """This function calls to the address book function
    to the delete a contact by its name

    Args:
        agenda (AddressBook): The address book
    """
    name = input("Type the name of the contact to delete: ")
    agenda.delete_contact(contact_name=name)


def update_contact(agenda: AddressBook):
    """This function calls to the address book function
    to the update a contact by its name

    Args:
        agenda (AddressBook): The address book
    """
    agenda.show_all_contacts()
    try:
        idx = int(input("Select one of the contacts to update: "))
        try:
            new_phone = int(input("Insert the new phone number: "))
            agenda.update_phone_number(idx=idx-1,
                                       phone_number=new_phone)
        except ValueError:
            print("You have to insert a phone number with just digits")
    except ValueError:
        print("You can only type digits")


def search_contact(agenda: AddressBook):
    """This function calls to the address book function
    to the search a contact by its name

    Args:
        agenda (AddressBook): The address book
    """
    name = input("Type the name of the contact that you want to search: ")
    agenda.search_by_name(name=name)

def menu(agenda: AddressBook):
    """Menu function, allows to the user to do a few things

    Args:
        agenda (AddressBook): The address book
    """
    while True:
        print("1. Add new contact")
        print("2. Delete contact")
        print("3. Update contact")
        print("4. Search contact")
        print("5. Show all contacts")
        print("6. Exit")

        try:

            option = int(input("Choose one option: "))

            match option:
                case 1:
                    add_new_contact(agenda)
                case 2:
                    delete_contact(agenda)
                case 3:
                    update_contact(agenda)
                case 4:
                    search_contact(agenda)
                case 5:
                    agenda.show_all_contacts()
                case 6:
                    print('Goodbye!')
                    break
                case other:
                    print('That option does not exist')
        except ValueError:
            print("The option must be an integer")

def main():
    """Main function
    """
    agenda = AddressBook()
    menu(agenda=agenda)

if __name__ == "__main__":
    main()