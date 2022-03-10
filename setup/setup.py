'''
    Author: lck
    Filename: setup.py
    Created: 25-01-2022
    Description: This file builds or database.
'''

import sqlite3
import csv
import os.path
from cryptography.fernet import Fernet
import base64
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import os
import getpass


def read_csv_file(fdata: str, f):
    listdata = []
    with open(fdata, mode = "r") as csvfile:
        csvReader = csv.reader(csvfile, delimiter=";")
        for row in csvReader:
            token = f.encrypt(bytes(row[2], encoding="ascii"))
            row[2] = token
            listdata.append(row)
            print (row)
    return listdata


def connect_to_db(db_path: str):
    """
    1. Check if the db.sqlite3 file exists. If not throw an error.
    2. Connect to the database and return the connection object.
    """
    if os.path.exists(db_path):
        path = sqlite3.connect(db_path)
        print("Die Datenbank ist verbunden")
        return path
    else:
        print("Diese Datenbank existiert nicht")



def create_table(conn):
    """Create a table where title, username, password and the url can be stored."""
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS pw_manager(
               title text,
                username blob,
                password blob,
                url blob  
                )""")


def insert_csv_data(conn, csv_data):
    """Insert the csv data in the database table."""
    c = conn.cursor()
    del csv_data[0]
    c.executemany("""INSERT INTO pw_manager (title, username, password, url) VALUES (?,?,?,?)""", csv_data)
    print("Datenbank eingetragen")
    conn.commit()
    conn.close()

def crypt():
    password = getpass.getpass(prompt="Passwort: ", stream=None)
    s = b"hallo"
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=s,
        iterations=390000
        )
    key = base64.urlsafe_b64encode(kdf.derive(bytes(password, encoding="ascii")))
    f = Fernet(key)
    return f



def main() -> None:
    
    f = crypt()

    csv_data = read_csv_file("data.csv", f)

    conn = connect_to_db("../src/pwdatabase.db")

    create_table(conn)
    
    insert_csv_data(conn, csv_data)

if __name__ == '__main__':
    main()
