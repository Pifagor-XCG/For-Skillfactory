phones = {"Anna": "255_345_43", "Boris": "255_143_32", "Nataly": "255_154_69"}

def show_contacts():
    print("Contact list:")
    for person, num in phones.items():
        print(f"{person}: {num}")

while True:
    print("\nWHAT WOULD YOU LIKE TO DO?")
    print("1 - Find")
    print("2 - Add")
    print("3 - Delete")
    print("4 - Edit")
    print("5 - Exit the program")
    try:
        Choose = int(input("Enter your choice: "))
    except ValueError:
        print("Please enter a number from 1 to 5!")
        continue

    if Choose == 1:
        print("Available contacts:", ', '.join(phones.keys()))
        name = input("Which contact would you like to find? ")
        if name in phones:
            print(f"The phone number for {name} is {phones.get(name)}")
        else:
            print("This contact is not in the list!")

    elif Choose == 2:
        print("Add a new contact")
        add_new_person = input("Enter the name you want to add: ")
        if add_new_person in phones:
            print("This contact already exists!")
        else:
            new_num = input("Enter the phone number: ")
            phones[add_new_person] = new_num
            show_contacts()

    elif Choose == 3:
        print("Delete a contact")
        print("Current contacts:", ', '.join(phones.keys()))
        delete_the_pers = input("Enter the name of the contact to delete: ")
        if delete_the_pers in phones:
            phones.pop(delete_the_pers)
            print(f"{delete_the_pers} was successfully deleted")
            show_contacts()
        else:
            print("This contact is not in the list")

    elif Choose == 4:
        print("Edit a contact’s phone number")
        print("Current contact list:")
        for key in phones:
            print(f"{key} - {phones.get(key)}")
        find_the_pers = input("Enter the name of the contact to edit: ")
        if find_the_pers in phones:
            new_num = input("Enter the new phone number: ")
            phones[find_the_pers] = new_num
            print(f"{find_the_pers}'s phone number was successfully updated to {new_num}")
            show_contacts()
        else:
            print("This contact does not exist")

    elif Choose == 5:
        print("Program terminated. Goodbye!")
        break