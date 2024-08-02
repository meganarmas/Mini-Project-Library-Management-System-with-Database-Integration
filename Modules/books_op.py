from Modules.class_books import Def_Books

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
    title = input("Add title of book: ")
    author = input("Add author of the book: ")
    isbn = input("Enter isbn: ")
    full_book = {'title': {title}, 'author': {author}, 'isbn': {isbn}, 'status': 'available'}
    if len(books) >= 1:
        for book in books:
            if title in book.values():
                print(f"User {book} exists already.")
            else:
                books.append(full_book)
                print(f"{full_book} has been added")
    else:
        books.append(full_book)
        print(f"{full_book} has been added")

def borrow_books():
    isbn_borrow = input("Enter the ISBN of a book you would like to borrow: ")
    book = isbn_borrow 
    try:
        if len(isbn_borrow) > 1:
            print("Multiple books found.")
        index = int(isbn_borrow ) - 1
        if 0 <= index < len(books):
            for book in enumerate(isbn_borrow , start=1):
                books[index]['status'] = 'borrowed'
                print(f"Book with the isbn {book} is out of the library!")
    except ValueError:
        print("A book with that ISBN was not found.")

def return_books():
    isbn_book = input("Enter the ISBN of the book to be returned: ")
    book = isbn_book
    try:
        if len(isbn_book) > 1:
            print("Multiple books found.")
        index = int(isbn_book) - 1
        if 0 <= index < len(books):
            for book in enumerate(isbn_book, start=1):
                books[index]['status'] = 'available'
                print(f"Book with the isbn {book} found and returned")
    except ValueError:
        print("A book with that ISBN was not found.")
                    
def search_book():
    title = input("What is the name of the book you would like to find: ")
    book = title
    if book:
        print(f"Found {book} in the library!")
    else:
        print("Book with that title was not found.")

def display_books():
    if books:
            for book in books:
                print(book)
    else:
        print("No books found in the library.")