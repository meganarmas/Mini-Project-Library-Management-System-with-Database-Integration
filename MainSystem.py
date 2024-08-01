from Modules.user_operations import user_op_menu
from Modules.authors_op import authors_menu
from Modules.books_op import book_menu
from Modules.genres_op import genre_main


class LibraryManagement():

    def main(self):
        while True:
            print("Welcome to the Library Management System! \nMenu")
            print("1. Book Operations")
            print("2. User Operations")
            print("3. Author Operations")
            print("4. Genre Operations")
            print("5. Quit")
            choice = input("Enter choice: ")
            

            if choice == '1':
                book_menu()
            elif choice == '2':
                user_op_menu()
            elif choice == '3':
               authors_menu()
            elif choice == '4':
                genre_main()
            elif choice == '5':
                print("Thank you for using the Library Management System! Now closing...")
                break
            else:
                print("Please enter a valid number.")

if __name__ == "__main__": 
    library_management = LibraryManagement()
    library_management.main()