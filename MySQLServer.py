#!/usr/bin/python3
import mysql.connector
from mysql.connector import Error

def create_database():
    connection = None
    cursor = None
    
    try:
        # Establish connection to MySQL server
        connection = mysql.connector.connect(
            host="localhost",
            user="root",  # replace with your MySQL username
            password=""   # replace with your MySQL password
        )

        if connection.is_connected():
            # Create a cursor object to execute queries
            cursor = connection.cursor()
            
            # Create database without using SELECT or SHOW
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            
            print("Database 'alx_book_store' created successfully!")

    except Error as err:
        if err.errno == 1045:  # Access denied error
            print("Error: Access denied. Please check your username and password")
        elif err.errno == 2003:  # Server not found error
            print("Error: Unable to connect to the MySQL server. Please check if server is running")
        else:
            print(f"Error while connecting to MySQL: {err}")
        return False

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return False

    finally:
        try:
            if cursor:
                cursor.close()
            if connection and connection.is_connected():
                connection.close()
                print("MySQL connection is closed")
        except Error as e:
            print(f"Error while closing connection: {e}")

if __name__ == "__main__":
    create_database()