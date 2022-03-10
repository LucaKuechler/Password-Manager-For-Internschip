'''
    Author: lck
    Filename: db_operations.py
    Created: 25-01-2022
    Description:
'''
import sqlite3
import os.path
from cryptography.fernet import Fernet
from cryptography.fernet import Fernet
import base64
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import os


def connect_to_db(path: str):
    """Same as in setup.py."""
    if os.path.exists(path):
        path = sqlite3.connect(path)
        print("Datenbank ist verbunden")
        return path
    else:
        print ("Die Datenbank ist nicht vorhanden")    
    
class Credentials:
    def __init__(self, title, username, password, url, f):
        self.title = title
        self.username = username
        self.password = f.decrypt(password).decode()
        self.url = url
        self.f = f
    # @property
    # def password(self):
    #     tmp = self.f.decrypt(self.password).decode()
    #     return tmp

# @password.setter
# def password(self, password):
#      self.password = password
    


def read_db_data(conn, password):
    """
        Read all credentials (tilte, username, password and url) form the database 
        and return them.
    """

    c = conn.cursor()
    c.execute("""SELECT * FROM pw_manager""")
    data = c.fetchall()
    list_ = []
    
    s = b"hallo"
    kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=32,
    salt=s,
    iterations=390000
    )
    key = base64.urlsafe_b64encode(kdf.derive(bytes(password, encoding="ascii")))
    f = Fernet(key)

    for item in data:
        Objekt = Credentials(item[0], item[1], item[2], item[3], f)
        datadict = {"title" : Objekt.title, "username" : Objekt.username, "password" : Objekt.password, "url" : Objekt.url}
        list_.append(datadict)
    conn.close()
    return list_
