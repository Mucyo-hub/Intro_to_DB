#!/usr/bin/python3
"""Script to create MySQL database alx_book_store"""
import mysql.connector
from mysql.connector import Error


def create_database():
    """Function to create the alx_book_store database"""
    # Initialize connection and cursor as None
    connection = None
    cursor = None

    try:
        # Connect to MySQL server
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password=''  # Add your MySQL password here
        )

        if connection.is_connected():
            cursor = connection.cursor()
            
            # Create database
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except Error as error:
        print(f"Error while connecting to MySQL: {error}")
        return False

    finally:
        if cursor is not None:
            cursor.close()
        if connection is not None and connection.is_connected():
            connection.close()
            print("MySQL connection is closed")


if __name__ == "__main__":
    create_database()