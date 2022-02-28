'''
    Author: lck
    Filename: db_operations.py
    Created: 25-01-2022
    Description:
'''
import sqlite3
import os


def connect_to_db(path: str):
    """Same as in setup.py."""
    if not os.path.isfile(path):
        raise Exception("error")

    con = sqlite3.connect(path)
    print(con)
    return con


def read_db_data(conn):
    """
        Read all credentials (title, username, password and url) from the database
        and return them.
    """
    cursor = conn.cursor()
    #for lines in db:
        #print(lines)

    #data = [
    #    {
    #        "username": "daniel",
    #        "password": "jesg",

    #    },
    #     {
    #        "username": "daniel",
    #        "password": "jesg",

     #    }
     #]

    data = []
    cursor.execute('''SELECT title, username, password, url FROM PW''')
    for lines in cursor.fetchall():
        title = lines[0]
        username = lines[1]
        password = lines[2]
        url = lines[3]
        ein_dict ={"title": title, "username": username, "password": password, "url": url}
        data.append(ein_dict)
    return data
