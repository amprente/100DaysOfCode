from flask import Flask, render_template, request, redirect, url_for, flash, session
from replit import db
import hashlib

app = Flask(__name__)
app.secret_key = 'supersecretkey'

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

@app.route('/')
def home():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
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

        session['logged_in'] = True
        session['username'] = username
        flash(f'Hello, {db[username]["name"]}! Welcome back.')
        return redirect(url_for('welcome'))

    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    flash('You have been logged out.')
    return redirect(url_for('login'))

@app.route('/welcome')
def welcome():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    username = session.get('username')
    name = db[username]['name']
    return render_template('welcome.html', name=name)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81)
