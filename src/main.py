'''
    Author: lck
    Filename: main.py
    Created: 25-01-2022
    Description:
'''
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def Home():
    """This route lists all available passwords from the database."""

    # connect to database (function in db_operations.py)

    # read credentials from database (function in db_operations.py)

    # close database connection

    # format data for frontend change render_template('home.html') to render_template('home.html', your_data=credentials)

    return render_template('home.html') 

if __name__ == '__main__':
    app.run(port=3333, debug=True)
