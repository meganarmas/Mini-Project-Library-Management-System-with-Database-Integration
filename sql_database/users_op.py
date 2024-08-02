from Modules.class_users import UserClass

from library_database import connect_database
import Error

conn = connect_database()

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
    if conn is not None:
        try:
            cursor = conn.cursor()
            query = "INSERT INTO users (first_name, last_name, library_id) VALUES (%s, %s, %s)", first_name, last_name, library_id
            cursor.commit(query)
            print("New user added to the library system.")
        
        except Error as e:
            print(f"Error: {e}")
        
        finally:
            cursor.close()
            conn.close()

def view_users():
    if conn is not None:
        try:
            cursor = conn.cursor()
            query = "SELECT * FROM users WHERE id = %s"
            cursor.execute(query)
            for row in cursor.fetchone():
                print(row)
        
        except Error as e:
            print(f"Error: {e}")
        
        finally:
            cursor.close()
            conn.close()


def display_all_details():
    if conn is not None:
        try:
            cursor = conn.cursor()
            query = "SELECT * FROM users"
            cursor.execute(query)
            for row in cursor.fetchall():
                print(row)
        
        except Error as e:
            print(f"Error: {e}")
        
        finally:
            cursor.close()
            conn.close()
