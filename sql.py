from sql_database.library_database import connect_database
import Error

conn = connect_database()
if conn is not None:
    try:
        cursor = conn.cursor()
        query = "SELECT * FROM CUSTOMERS"
        cursor.execute(query)
        for row in cursor.fetchall():
            print(row)
    
    except Error as e:
        print(f"Error: {e}")
    
    finally:
        cursor.close()
        conn.close()