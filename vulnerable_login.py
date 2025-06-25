# vulnerable_login.py
import sqlite3
from flask import Flask, request

app = Flask(__name__)
conn = sqlite3.connect('users.db', check_same_thread=False)
cursor = conn.cursor()

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    #  SQL Injection Vulnerability (Unsafe-Query)
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    cursor.execute(query)
    result = cursor.fetchone()

    if result:
        return "Login successful!"
    else:
        return "Invalid credentials"

if __name__ == '__main__':
    app.run(debug=True)
