from sql_database.class_authors import Authors_Class

author_class = Authors_Class

authors = []


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
    author_name = input("Enter the author's name: ")
    biography = input ("Enter the author's biography: ")
    new_author = {'name': {author_name}, 'biography': {biography}}
    if len(authors) >= 1:
        for author in authors:
            if author_name in author.values():
                print(f"User {author} exists already.")
            else:
                users.append(new_author)
                print(f"{author} has been added")
    else:
        authors.append(new_author)
        print(f"{new_author} has been added")

def view_details():
    for author_name in authors:
        print(author_name)
                    
def display_authors():
    author = authors
    if author in authors:
        print(author)
    else:
        print("No authors found.")