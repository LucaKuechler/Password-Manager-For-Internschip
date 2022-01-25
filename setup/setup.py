'''
    Author: lck
    Filename: setup.py
    Created: 25-01-2022
    Description: This file builds or database.
'''

import sqlite3


def read_csv_file(filename: str):
    """Read the content from a given csv file."""


def connect_to_db(db_path: str):
    """
        1. Check if the db.sqlite3 file exists. If not throw an error.
        2. Connect to the database and return the connection object.
    """


def create_table(conn):
    """Create a table where title, username, password and the url can be stored."""


def insert_csv_data(conn):
    """Insert the csv data in the database table."""


def main() -> None:
    csv_data = read_csv_file("data.csv")
    
    conn = connect_to_db("../src/db.sqlite3")
 
    create_table(conn)
    
    insert_csv_data(conn, csv_data)


if __name__ == '__main__':
    main()
