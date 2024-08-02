from Modules.class_genres import Genre_Class

from library_database import connect_database
import Error

conn = connect_database()

genre_class = Genre_Class

genres = []



def genre_main():
    print("Genre Menu.")
    print("1. Add a new genre")
    print("2. View genre details")
    print("3. Display all genres")
    choice = input("Enter choice: ")

    if choice == '1':
        add_new_genre()
    elif choice == '2':
        view_genres()
    elif choice == '3':
        display_genres()
    else:
        print("Please enter a valid number.")

def add_new_genre():
    if conn is not None:
        try:
            cursor = conn.cursor()
            query = "INSERT INTO genres (name, description, category) VALUES (%s, %s, %s)", name, description, category
            cursor.commit(query)
            print("New genre added to the system.")
        
        except Error as e:
            print(f"Error: {e}")
        
        finally:
            cursor.close()
            conn.close()
                
def view_genres():
   if conn is not None:
        try:
            cursor = conn.cursor()
            query = "SELECT * FROM genres"
            cursor.execute(query)
            for row in cursor.fetchone():
                print(row)
        
        except Error as e:
            print(f"Error: {e}")
        
        finally:
            cursor.close()
            conn.close()
        

def display_genres():
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

