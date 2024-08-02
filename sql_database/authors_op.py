from Modules.class_authors import Authors_Class

author_class = Authors_Class

authors = []

from library_database import connect_database
import Error

conn = connect_database()


def authors_menu():
    print("Author Menu.")
    print("1. Add a new author")
    print("2. View author details")
    print("3. Display all authors")
    choice = input("Enter choice: ")

    if choice == '1':
        add_new_author()
    elif choice == '2':
        view_details()
    elif choice == '3':
        display_authors()
    else:
        print("Please enter a valid number.")

def add_new_author():
    if conn is not None:
        try:
            cursor = conn.cursor()
            query = "INSERT INTO authors (name, biography) VALUES (%s, %s)", name, biography
            cursor.commit(query)
            print("New author added to SQL.")
        
        except Error as e:
            print(f"Error: {e}")
        
        finally:
            cursor.close()
            conn.close()

def view_details():
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
                    
def display_authors():
    if conn is not None:
        try:
            cursor = conn.cursor()
            query = "SELECT * FROM authors"
            cursor.execute(query)
            for row in cursor.fetchall():
                print(row)
        
        except Error as e:
            print(f"Error: {e}")
        
        finally:
            cursor.close()
            conn.close()