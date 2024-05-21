'''Today's challenge is to build a fully functional blog engine.'''

from flask import Flask, render_template, request, redirect, url_for, session
import replit
from replit import db
from datetime import datetime
import os


app = Flask(__name__)
app.secret_key = 'ampry'  # Replace with a secure secret key

# Home route
@app.route('/')
def home():
    if 'username' in session:
        # User is logged in, show the dashboard
        keys = list(db.keys())
        posts = [db[key] for key in reversed(keys)]
        return render_template('dashboard.html', posts=posts)
    else:
        # User is not logged in, show the feed
        keys = list(db.keys())
        posts = [db[key] for key in reversed(keys)]
        return render_template('feed.html', posts=posts)

# Login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Replace these with your actual username and password
        if username == 'user' and password == '12345':
            session['username'] = username
            return redirect(url_for('home'))
        else:
            return "Invalid credentials, please try again."
    return render_template('login.html')

# Logout route
@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('home'))

# Add post route
@app.route('/add_post', methods=['POST'])
def add_post():
    if 'username' in session:
        title = request.form['title']
        content = request.form['content']
        date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        post_id = str(len(db.keys()) + 1)
        db[post_id] = {'title': title, 'content': content, 'date': date}
        return redirect(url_for('home'))
    else:
        return redirect(url_for('login'))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=81)
