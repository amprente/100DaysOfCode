'''build a flask website with a signup form.

The signup form should:

Ask for name, username and password.
Create a user account in a repl db usnig these details.
Direct you to the login form, which gets username and password as input.
If the details are valid, 'Hello' and the user's name should be displayed on screen.'''




from flask import Flask, render_template, request, redirect, url_for, flash
from replit import db
import hashlib

app = Flask(__name__)
app.secret_key = 'supersecretkey'

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        name = request.form['name']
        username = request.form['username']
        password = hash_password(request.form['password'])

        if username in db.keys():
            flash('Username already exists!')
            return redirect(url_for('signup'))

        db[username] = {'name': name, 'password': password}
        flash('Signup successful! Please log in.')
        return redirect(url_for('login'))

    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = hash_password(request.form['password'])

        if username not in db.keys() or db[username]['password'] != password:
            flash('Invalid username or password!')
            return redirect(url_for('login'))

        flash(f'Hello, {db[username]["name"]}! Welcome back.')
        return render_template('welcome.html', name=db[username]['name'])

    return render_template('login.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81)
