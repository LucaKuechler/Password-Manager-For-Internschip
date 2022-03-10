'''
    Author: lck
    Filename: main.py
    Created: 25-01-2022
    Description:
'''


from flask import Flask, flash, render_template, request, session, redirect, url_for
import db_operations
from cryptography.fernet import Fernet
import base64
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import os
import getpass
import hashlib



app = Flask(__name__)

@app.route('/')
def Home():
    """This route lists all available passwords from the database."""
    if not app.config["login"]:
        return render_template("login.html")

    conn = db_operations.connect_to_db("pwdatabase.db")

    # read credentials from database (function in db_operations.py)
    list_ = db_operations.read_db_data(conn, app.config["pw"])

    # close database connection

    # format data for frontend change render_template('home.html') to render_template('home.html', credentials=your_data)

    return render_template('home.html', credentials=list_) 


@app.route("/login")
def do_login():
    return render_template("login.html")

@app.route("/login/status", methods = ["POST"])
def authenticate_login():
    tmp = hashlib.md5(bytes(request.form["password"], encoding="ascii"))

    if tmp.hexdigest() == app.config["hashpw"]:
        app.config["pw"] = request.form["password"]
        app.config["login"] = True
        return redirect(url_for("Home"))
    return "Falsches Passwort"
    

if __name__ == '__main__':
    app.config["login"] = False
    app.config["pw"] = ""
    app.config["hashpw"] = "195efe600e8ee7550c43b93116820275"

    app.run(port=3333, debug=True)
