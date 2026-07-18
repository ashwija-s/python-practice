contacts = {}
def menu():
    print("===== CONTACT BOOK =====\n1. Add Contact \n2. View Contacts \n3. Search Contact \n4. Delete Contact \n5. Exit")

def add_contact():
    name = input("Enter name: ")
    contact = input("Enter contact: ")
    contacts[name] = contact
    print("Contact added successfully.")

def view_contact():
    if not contacts:
        print("No contacts found.")
    else:
        for name, contact in contacts.items():
            print(f"{name}: {contact}")
            print(" 1")
def search_contact():
    name = input("Enter name: ")
    if name in contacts:
        print(contacts[name])
    else:
        print("Contact not found.")
def delete_contact():
    name = input("Enter name: ")
    if name in contacts:
        del contacts[name]
        print("Contact deleted.")
    else:
        print("Contact not found.")
while True:
    menu()
    while True:
        try:    
            x = int(input("Enter the number: "))
            break
        except ValueError:
            print("Please enter a number.")


    if x == 1:
        add_contact()

    elif x == 2:
        view_contact()

    elif x == 3:
        search_contact()

    elif x == 4:
        delete_contact()

    elif x == 5:
        break
    else:
        print("Please enter a number between 1 to 5.")
