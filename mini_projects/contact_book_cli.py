contacts = {}
while True:
    print("===== CONTACT BOOK =====\n1. Add Contact \n2. View Contacts \n3. Search Contact \n4. Delete Contact \n5. Exit")
    while True:
        try:    
            x = int(input("Enter the number: "))
            break
        except ValueError:
            print("Please enter a number.")
    if x == 1:
        name = input("Enter name: ")
        contact = input("Enter contact: ")
        contacts[name] = contact
        print("Contact added successfully.")

    elif x == 2:
        if not contacts:
            print("No contacts found.")
        for i, k in contacts.items():
                print(f"{i}: {k}")

    elif x == 3:
        name = input("Enter name: ")
        if name in contacts:
            print(contacts[name])
        else:
            print("Contact not found.")

    elif x == 4:
        name = input("Enter name: ")
        if name in contacts:
            del contacts[name]
            print("Contact deleted.")
        else:
            print("Contact not found.")

    elif x == 5:
        break
    else:
        print("Please enter a number between 1 to 5.")