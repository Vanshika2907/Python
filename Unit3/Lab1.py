'''
Write a python program to create a simple Contact Book using list & dictionaries.
The program should allow the user to add a contact, display all contacts, search
for a contact by name, and delete a contact by name.
'''

def add_contact(contacts):
    name = input("Enter contact name: ")

    # Check if name already exists
    for i in contacts:
        if i['name'].lower() == name.lower():
            print("Contact name already exists!")
            return

    phone = input("Enter contact phone number: ")

    # Check if phone number contains exactly 10 digits
    if not phone.isdigit() or len(phone) != 10:
        print("Invalid phone number! Enter exactly 10 digits.")
        return

    contacts.append({"name": name, "phone": phone})
    print(f"Contact {name} added successfully!")


def display_contacts(contacts):
    if not contacts:
        print("No contacts to display.")
        return

    print("Contacts:")
    for i in contacts:
        print(f"Name: {i['name']}, Phone: {i['phone']}")


def search_contact(contacts):
    name = input("Enter contact name to search: ")

    for i in contacts:
        if i['name'].lower() == name.lower():
            print(f"Contact found: Name: {i['name']}, Phone: {i['phone']}")
            return

    print("Contact not found!")


def delete_contact(contacts):
    name = input("Enter contact name to delete: ")

    for i in contacts:
        if i['name'].lower() == name.lower():
            contacts.remove(i)
            print(f"Contact {name} deleted successfully!")
            return

    print("Contact not found!")


contacts = []

while True:
    print("\nContact Book Menu:")
    print("1. Add Contact")
    print("2. Display Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        add_contact(contacts)

    elif choice == '2':
        display_contacts(contacts)

    elif choice == '3':
        search_contact(contacts)

    elif choice == '4':
        delete_contact(contacts)

    elif choice == '5':
        print("Exiting Contact Book.")
        break

    else:
        print("Invalid choice. Please try again.")
