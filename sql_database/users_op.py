from class_users import UserClass

from library_database import connect_database


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
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            library_id = input("Enter library ID: ")
            new_user = (first_name, last_name, library_id)
            query = "INSERT INTO users (first_name, last_name, library_id) VALUES (%s, %s, %s)"
            cursor.execute(query, new_user)
            conn.commit()
            print("New user added to the library system.")
        
        except Exception as e:
            print(f"Error {e}")
        
        finally:
            cursor.close()
            conn.close()

def view_users():
    if conn is not None:
        try:
            cursor = conn.cursor()
            query = "SELECT * FROM users WHERE id = %s"
            cursor.execute(query)
            conn.commit()
            for row in cursor.fetchone():
                print(row)
        
        except Exception as e:
            print(f"Error {e}")
        
        finally:
            cursor.close()
            conn.close()


def display_all_details():
    if conn is not None:
        try:
            cursor = conn.cursor()
            query = "SELECT * FROM users"
            cursor.execute(query)
            conn.commit()
            for row in cursor.fetchall():
                print(row)
        
        except Exception as e:
            print(f"Error {e}")
        
        finally:
            cursor.close()
            conn.close()
