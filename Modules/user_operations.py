from Modules.class_users import UserClass

users = []


def user_op_menu():
    print("1. Add a new user")
    print("2. View user details")
    print("3. Display all users")
    choice = input("Enter choice: ")

    if choice == '1':
        add_new_user()
    elif choice == '2':
        view_users()
    elif choice == '3':
        display_all_details()
    else:
        print("Please enter a valid number.")
    

def add_new_user():
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    library_id = input("Enter library ID: ")
    new_user = {'first Name': first_name, 'last Name': last_name, 'library id': library_id}
    if len(users) >= 1:
        for user in users:
            if first_name in user.values():
                print(f"User {user} exists already.")
            else:
                users.append(new_user)
                print(f"{new_user} has been added")
    else:
        users.append(new_user)
        print(f"{new_user} has been added")

def view_users():
        library_id = input("Enter library ID of user: ")
        for user in users:
            if user in library_id:              
                print(f"{user}found!")
                print(f"first name: {user["first name"]}, last name: {user["last name"]}, Library ID: {user["library id"]}")
        else:
            print("User was not found.")

def display_all_details():
    if users:
            for user in users:
                print(user)
    else:
        print("No users have been added to the library.")
