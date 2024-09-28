contacts = []

print("Welcome to the Contact Book!")

while True:
    print("\n--- Contact Book ---")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")
    
    choice = input("Enter your choice (1-6): ")
    
    if choice == '1':
        print("\nAdd New Contact")
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        email = input("Enter email: ")
        address = input("Enter address: ")
        contacts.append({"name": name, "phone": phone, "email": email, "address": address})
        print("Contact added successfully!")

    elif choice == '2':
        if not contacts:
            print("No contacts found.")
        else:
            print("\nContact List:")
            for i, contact in enumerate(contacts, 1):
                print(f"{i}. {contact['name']}: {contact['phone']}")

    elif choice == '3':
        search_term = input("Enter name or phone number to search: ").lower()
        results = [contact for contact in contacts 
                   if search_term in contact['name'].lower() or search_term in contact['phone']]
        if results:
            print("\nSearch Results:")
            for contact in results:
                print(f"Name: {contact['name']}, Phone: {contact['phone']}")
        else:
            print("No matching contacts found.")

    elif choice == '4':
        name = input("Enter the name of the contact to update: ").lower()
        for contact in contacts:
            if contact['name'].lower() == name:
                contact['phone'] = input("Enter new phone number: ")
                contact['email'] = input("Enter new email: ")
                contact['address'] = input("Enter new address: ")
                print("Contact updated successfully!")
                break
        else:
            print("Contact not found.")

    elif choice == '5':
        name = input("Enter the name of the contact to delete: ").lower()
        for contact in contacts:
            if contact['name'].lower() == name:
                contacts.remove(contact)
                print("Contact deleted successfully!")
                break
        else:
            print("Contact not found.")

    elif choice == '6':
        print("Thank you for using the Contact Book!")
        break

    else:
        print("Invalid choice. Please try again.")#