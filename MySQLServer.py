import mysql.connector
from mysql.connector import Error
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="@Lynn4820"

)
mycursor=mydb.cursor()
try:
    mycursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store;")
    mydb.commit()
    print("Database 'alx_book_store' created successfully!")
except Error as e:
    print(f"Error creating database: {e}")

finally:
     mycursor.close()
     mydb.close()

