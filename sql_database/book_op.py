from Modules.class_books import Def_Books

from library_database import connect_database
import Error

conn = connect_database()

books_def = Def_Books

books = []
genres = []
authors = []



def book_menu():
    print("Book Operations Menu")
    print("1. Add a new book")
    print("2. Borrow a book")
    print("3. Return a book")
    print("4. Search for a book")
    print("5. Display all books")
    choice = input("Enter choice: ")

    if choice == '1':
        add_book()
    elif choice == '2':
        borrow_books()
    elif choice == '3':
        return_books()
    elif choice == '4':
        search_book()
    elif choice == '5':
        display_books()
    else:
        print("Please enter a valid number.")

def add_book():
    if conn is not None:
        try:
            cursor = conn.cursor()
            query = "INSERT INTO books (title, author, isbn) VALUES (%s, %s)", title, author, isbn
            cursor.commit(query)
            print("New book added to the library.")
        
        except Error as e:
            print(f"Error: {e}")
        
        finally:
            cursor.close()
            conn.close()

def borrow_books():
    if conn is not None:
        try:
            cursor = conn.cursor()
            query = "insert here"
            cursor.execute(query)
            for row in cursor.fetchall():
                print(row)
        
        except Error as e:
            print(f"Error: {e}")
        
        finally:
            cursor.close()
            conn.close()

def return_books():
    if conn is not None:
        try:
            cursor = conn.cursor()
            query = "insert here"
            cursor.execute(query)
            for row in cursor.fetchall():
                print(row)
        
        except Error as e:
            print(f"Error: {e}")
        
        finally:
            cursor.close()
            conn.close()
                    
def search_book():
    if conn is not None:
        try:
            cursor = conn.cursor()
            query = "insert here"
            cursor.execute(query)
            for row in cursor.fetchall():
                print(row)
        
        except Error as e:
            print(f"Error: {e}")
        
        finally:
            cursor.close()
            conn.close()

def display_books():
    if conn is not None:
        try:
            cursor = conn.cursor()
            query = "SELECT * FROM books"
            cursor.execute(query)
            for row in cursor.fetchall():
                print(row)
        
        except Error as e:
            print(f"Error: {e}")
        
        finally:
            cursor.close()
            conn.close()