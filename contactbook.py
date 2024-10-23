contacts = []

def add_contact():
    name = input("Enter contact name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    contacts.append({
        'name': name,
        'phone': phone,
        'email': email,
        'address': address
    })
    print(f"Contact '{name}' added successfully!")

def view_contacts():
    if contacts:
        print("\nContact List:")
        for i, contact in enumerate(contacts, 1):
            print(f"{i}. Name: {contact['name']}, Phone: {contact['phone']}")
    else:
        print("No contacts available.")

def search_contact():
    search = input("Enter name or phone number to search: ").lower()
    found = False
    for contact in contacts:
        if search in contact['name'].lower() or search in contact['phone']:
            print(f"\nContact Found: \nName: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}, Address: {contact['address']}")
            found = True
            break
    if not found:
        print("Contact not found.")

def update_contact():
    search = input("Enter name or phone number of contact to update: ").lower()
    for contact in contacts:
        if search in contact['name'].lower() or search in contact['phone']:
            print(f"\nUpdating Contact: {contact['name']}")
            contact['name'] = input("Enter new name: ") or contact['name']
            contact['phone'] = input("Enter new phone number: ") or contact['phone']
            contact['email'] = input("Enter new email: ") or contact['email']
            contact['address'] = input("Enter new address: ") or contact['address']
            print("Contact updated successfully!")
            return
    print("Contact not found.")

def delete_contact():
    search = input("Enter name or phone number of contact to delete: ").lower()
    for i, contact in enumerate(contacts):
        if search in contact['name'].lower() or search in contact['phone']:
            print(f"\nDeleting Contact: {contact['name']}")
            confirm = input("Are you sure you want to delete this contact? (yes/no): ").lower()
            if confirm == "yes":
                contacts.pop(i)
                print(f"Contact '{contact['name']}' deleted successfully!")
            return
    print("Contact not found.")

def contact_menu():
    while True:
        print("\n=== Contact Management System ===")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        
        choice = input("Select an option (1-6): ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")
            
contact_menu()