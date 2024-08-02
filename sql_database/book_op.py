from class_books import Def_Books

from library_database import connect_database

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
            title = input("Add title of book: ")
            author = input("Add author of the book: ")
            isbn = input("Enter isbn: ")
            publication_date = input("Enter the publication date (YEAR-MONTH-DAY): ")
            newly_added_book = (title, author, isbn, publication_date, availability_status)
            query = "INSERT INTO books (title, author, isbn, publication_date, availability_status) VALUES (%s, %s, %s, %s, %s)", 
            cursor.execute(query, newly_added_book)
            conn.commit()
            print("New book added to the library.")
        
        except Exception as e:
            print(f"Error {e}.")
        
        finally:
            cursor.close()
            conn.close()

def borrow_books():
    if conn is not None:
        try:
            cursor = conn.cursor()
            isbn_borrow = input("Enter the ISBN of a book you would like to borrow: ")
            book_found = (isbn_borrow)
            query = "INSERT INTO availbility_status (title, author, isbn, availbility_status) VALUES (%s, %s, %s, %s)"
            cursor.execute(query, book_found)
            conn.commit()
            print("The book has been borrowed from the library.")
        
        except Exception as e:
            print(f"Error {e}.")
        
        finally:
            cursor.close()
            conn.close()

def return_books():
    if conn is not None:
        try:
            cursor = conn.cursor()
            isbn_book = input("Enter the ISBN of the book to be returned: ")
            returned_book = (isbn_book)
            query = "UPDATE availbility_status SET return_date = %s WHERE user_id = %s  book_id = %s AND return_date is null)"
            cursor.execute(query, returned_book)
            conn.commit()
            print("The book has been returned to the library and is now available for checkout again!")
        
        except Error as e:
            print(f"Error {e}.")
        
        finally:
            cursor.close()
            conn.close()
                    
def search_book(): #search by isbn
    if conn is not None:
        try:
            cursor = conn.cursor()
            title = input("What is the name of the book you would like to find: ")
            found_book = (title)
            query = "SELECT * FROM books WHERE isbn LIKE %s"
            cursor.execute(query, found_book)
            conn.commit()
            for row in cursor.fetchall():
                print(row)
        
        except Exception as e:
            print(f"Error {e}")
        
        finally:
            cursor.close()
            conn.close()

def display_books():
    if conn is not None:
        try:
            cursor = conn.cursor()
            query = "SELECT * FROM books"
            cursor.execute(query)
            conn.commit()
            for row in cursor.fetchall():
                print(row)
        
        except Exception as e:
            print(f"Error {e}.")
        
        finally:
            cursor.close()
            conn.close()