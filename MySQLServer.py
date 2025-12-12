import mysql.connector
from mysql.connector import Error


try:
    connection = mysql.connector.connect(
    host = "localhost",
    user ="root",
    password = "2oo6k0j0@mysql",
    database = "alx_book_store"
)
    
    if connection.is_connected():
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")

except Error as e:
    print(f"Error while connecting to MySQL: {e}")


cursor.close()
connection.close()