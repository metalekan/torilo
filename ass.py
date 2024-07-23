# helper function
def validate_name(name):
    if name.isalpha() and len(name) >= 3:
        return True

def validate_phone(phone):
    if phone.isdigit() and len(phone) >= 8:
        return True

def validate_email(email):
    if "@" in email:
        return True
    
def email_exist(contacts, email):
    contact_set = set()
    if not contacts:
        return True
    for contact in contacts:
        contact_set.add(contact['email'])
        if email not in contact_set:
            return True

# function that welcome the user and instruct the user on use the system
def welcome():
    print("\nWelcome to Torilo CMS platform")
    print("Press 1. to Add a new contact")
    print("Press 2. to View contacts")
    print("Press 3. to Delete existing contact")
    print("Press exit to close this application\n")
    
# function to add a new contact
def add_new_contact(contacts):
    print("\nPlease add your new contact here below\n")
    first_name = input("Enter your first name: ") #validate
    last_name = input("Enter your last name: ") #validate
    phone_number = input("Enter your phone number: ") #validate
    address = input("Enter your address: ")
    email = input("Enter your email address: ") #unique
    
    if not validate_name(first_name):
        print("First Name must be Alphabet and be greater than 3")
        return 
    elif not validate_name(last_name):
        print("Last Name must be Alphabet and be greater than 3")
        return
    elif not validate_phone(phone_number):
        print("Phone must begreater than 8")
        return
    elif not validate_email(email):
        print("Invalid email")
        return
    elif not email_exist(contacts, email):
        print("Email already exist")
        return
    
    contact = {
        "first_name":first_name,
        "last_name":last_name,
        "phone_number":phone_number,
        "address":address,
        "email":email
    }
    contacts.append(contact)
    print("contact added successfully")
    return

# function to view the contact
def view_contact(contacts):
    if not contacts:
        print("your contact is empty")
        return
    for contact in contacts:
        print(f"first name: {contact["first_name"]}")
        print(f"last name: {contact["last_name"]}")
        print(f"phone number: {contact["phone_number"]}")
        print(f"email: {contact["email"]}")
        print(f"address: {contact["address"]}")
        
# function to delete the contact
def delete(contacts):
    first_name = input("Inser the first name of contact to delete: ")
    for contact in contacts:
        if contact["first_name"] == first_name:
            contacts.remove(contact)
            print("contact removed succesfully")
            return
        print("contact does not exist in DB")
        return
    
# function to exit
# main

# welcome()
contacts = []
while True:
    welcome()
    option = input("Enter an option below: ")
    if option == "1":
        add_new_contact(contacts)
    elif option == "2":
        view_contact(contacts)
    elif option == "3":
        delete(contacts)
    elif option == "exit":
        break
    else:
        print("Do something bro!!!")
