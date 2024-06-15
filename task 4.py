def add_contact(contact_book):
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    contact_book[name] = {'phone': phone, 'email': email, 'address': address}
    print("Contact added successfully!")

def view_contacts(contact_book):
    if not contact_book:
        print("Contact book is empty.")
    else:
        for name, details in contact_book.items():
            print(f"Name: {name}")
            print(f"Phone: {details['phone']}")
            print(f"Email: {details['email']}")
            print(f"Address: {details['address']}")
            print("-" * 20)

def search_contact(contact_book):
    name = input("Enter the name to search: ")
    if name in contact_book:
        details = contact_book[name]
        print(f"Name: {name}")
        print(f"Phone: {details['phone']}")
        print(f"Email: {details['email']}")
        print(f"Address: {details['address']}")
    else:
        print("Contact not found.")

def update_contact(contact_book):
    name = input("Enter the name of the contact to update: ")
    if name in contact_book:
        phone = input("Enter new phone number: ")
        email = input("Enter new email: ")
        address = input("Enter new address: ")
        contact_book[name] = {'phone': phone, 'email': email, 'address': address}
        print("Contact updated successfully!")
    else:
        print("Contact not found.")

def delete_contact(contact_book):
    name = input("Enter the name of the contact to delete: ")
    if name in contact_book:
        del contact_book[name]
        print("Contact deleted successfully!")
    else:
        print("Contact not found.")

def main():
    contact_book = {}
    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_contact(contact_book)
        elif choice == '2':
            view_contacts(contact_book)
        elif choice == '3':
            search_contact(contact_book)
        elif choice == '4':
            update_contact(contact_book)
        elif choice == '5':
            delete_contact(contact_book)
        elif choice == '6':
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()