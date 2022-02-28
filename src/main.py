'''
    Author: lck
    Filename: main.py
    Created: 25-01-2022
    Description:
'''
from flask import Flask, render_template
from db_operations import connect_to_db
from db_operations import read_db_data
app = Flask(__name__)


@app.route('/')
def Home():
    """This route lists all available passwords from the database."""

    # connect to database (function in db_operations.py)
    conn = connect_to_db("db.sqlite3")

    # read credentials from database (function in db_operations.py)
    your_data = read_db_data(conn)

    # close database connection
    conn.close()

    # format data for frontend change render_template('home.html') to render_template('home.html', your_data=credentials)

    return render_template('home.html', credentials=your_data)

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
