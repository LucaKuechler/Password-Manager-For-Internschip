'''
    Author: lck
    Filename: setup.py
    Created: 25-01-2022
    Description: This file builds or database.
'''

import sqlite3
import csv
import os


def read_csv_file(filename: str):
    """Read the content from a given csv file."""

    content_list = []


    with open(filename, mode ='r') as file:
        csvFile = csv.DictReader(file, delimiter=";")

        for lines in csvFile:
            content_list.append(lines)
        print(csvFile)
        return content_list

def connect_to_db(db_path: str):
    """
        1. Check if the db.sqlite3 file exists. If not throw an error.
        2. Connect to the database and return the connection object.
    """
    if os.path.isfile(db_path):
        raise Exception("error")

    con = sqlite3.connect(db_path)
    print(con)
    return con


def create_table(conn):
    """Create a table where title, username, password and the url can be stored."""
    cursor = conn.cursor()
    sql = '''CREATE TABLE IF NOT EXISTS PW(
       ID INTEGER PRIMARY KEY,
       TITLE VARCHAR,
       USERNAME VARCHAR,
       PASSWORD VARCHAR,
       URL VARCHAR
    )'''
    cursor.execute(sql)
    conn.commit()


def insert_csv_data(conn, csv_data):
    """Insert the csv data in the database table."""
    cursor = conn.cursor()
    for lines in csv_data:
        print(lines)
        title = lines["title"]
        username = lines["username"]
        password = lines["password"]
        url = lines["url"]

        sql = '''INSERT INTO PW
        (TITLE, USERNAME, PASSWORD, URL) VALUES
        (?, ?, ?, ?)'''
        cursor.execute(sql, (title, username, password, url))
        conn.commit()


def main() -> None:
    csv_data = read_csv_file("data.csv")
    for lines in csv_data:
        print(lines["title"])

    conn = connect_to_db("../src/db.sqlite3")
 
    create_table(conn)
    
    insert_csv_data(conn, csv_data)


if __name__ == '__main__':
    main()
