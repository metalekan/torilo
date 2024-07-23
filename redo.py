# function to welcome user
def welcome():
    print("\nwelcome to the contact management system 🚧\n")
    print("Select 1. to Add a new user.")
    print("Select 2. to View users.")
    print("Select 3. to Delete a user.")
    print("Select 4. to exit.\n")
    
# function to add a new user
def add_user(users):
    username = input("\nEnter your username: ")
    email = input("Enter your email: ")
    country = input("Enter your country: ")
    
    user = {
        'username' : username,
        'email' : email,
        'country' : country
    }
    
    users.append(user)
    print(users)
    
# function to view a user
def view_users(users):
    if not users:
        print("\nusers list is empty 🛒")
    else:
        print(users)
        
# function to delete a user
users = []
while True:
    welcome()
    selection = input("chose an operation: ")
    if selection == "1":
        add_user(users)
    elif selection == "2":
        view_users(users)
        

