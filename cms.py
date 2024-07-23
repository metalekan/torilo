import re

def display_menu():
    print("\nContact Management System")
    print("1. Add a New Contact")
    print("2. View All Contacts")
    print("3. Update a Contact")
    print("4. Delete a Contact")
    print("5. Exit")
    

def capitalize_name(name):
    return name.capitalize()

def validate_email(email):
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(pattern, email)

def validate_phone(phone):
    return phone.isdigit()

def add_contact(contacts, email_set):
    first_name = capitalize_name(input("Enter first name: "))
    last_name = capitalize_name(input("Enter last name: "))
    phone_number = input("Enter phone number: ")

    while not validate_phone(phone_number):
        print("Invalid phone number. It should contain only digits.")
        phone_number = input("Enter phone number: ")

    email = input("Enter email: ")

    while not validate_email(email):
        print("Invalid email format.")
        email = input("Enter email: ")

    address = input("Enter address: ")

    if email in email_set:
        print("A contact with this email already exists.")
    else:
        contact = {
            'first_name': first_name,
            'last_name': last_name,
            'phone_number': phone_number,
            'email': email,
            'address': address
        }
        contacts.append(contact)
        email_set.add(email)
        print("Contact added successfully.")

def view_contacts(contacts):
    if not contacts:
        print("No contacts available.")
    else:
        print("\nContacts List:")
        for contact in contacts:
            print(f"Name: {contact['first_name']} {contact['last_name']}")
            print(f"Phone: {contact['phone_number']}")
            print(f"Email: {contact['email']}")
            print(f"Address: {contact['address']}\n")

def update_contact(contacts, email_set):
    first_name = capitalize_name(input("Enter the first name of the contact to update: "))
    for contact in contacts:
        if contact['first_name'] == first_name:
            print("Contact found. Enter new details (leave blank to keep current value):")
            new_first_name = input(f"First name ({contact['first_name']}): ") or contact['first_name']
            new_last_name = input(f"Last name ({contact['last_name']}): ") or contact['last_name']
            new_phone_number = input(f"Phone number ({contact['phone_number']}): ") or contact['phone_number']

            while new_phone_number != contact['phone_number'] and not validate_phone(new_phone_number):
                print("Invalid phone number. It should contain only digits.")
                new_phone_number = input(f"Phone number ({contact['phone_number']}): ") or contact['phone_number']

            new_email = input(f"Email ({contact['email']}): ") or contact['email']

            while new_email != contact['email'] and not validate_email(new_email):
                print("Invalid email format.")
                new_email = input(f"Email ({contact['email']}): ") or contact['email']

            if new_email != contact['email'] and new_email in email_set:
                print("A contact with this email already exists.")
            else:
                if new_email != contact['email']:
                    email_set.remove(contact['email'])
                    email_set.add(new_email)
                contact['first_name'] = new_first_name
                contact['last_name'] = new_last_name
                contact['phone_number'] = new_phone_number
                contact['email'] = new_email
                contact['address'] = input(f"Address ({contact['address']}): ") or contact['address']
                print("Contact updated successfully.")
            return
    print("Contact not found.")

def delete_contact(contacts, email_set):
    first_name = capitalize_name(input("Enter the first name of the contact to delete: "))
    for contact in contacts:
        if contact['first_name'] == first_name:
            contacts.remove(contact)
            email_set.remove(contact['email'])
            print("Contact deleted successfully.")
            return
    print("Contact not found.")

def main():
    contacts = []
    email_set = set()
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            add_contact(contacts, email_set)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            update_contact(contacts, email_set)
        elif choice == '4':
            delete_contact(contacts, email_set)
        elif choice == '5':
            print("Exiting the Contact Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
