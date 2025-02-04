#!/usr/bin/python3
"""Script to create MySQL database alx_book_store"""
import mysql.connector

def create_database():
    """Function to create the alx_book_store database"""
    connection = None
    cursor = None

    try:
        # Connect to MySQL server
        connection = mysql.connector.connect(
            host='localhost',
            user='fab',
            password='fab@250'  
        )

        if connection.is_connected():
            cursor = connection.cursor()
            
            # Create database
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as error:
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