'''Allow your normal blog page to be visible to anyone, regardless of login status.
If a user logs in, and it's you, take them to the admin page.
If a user logs in, and it's not you, tell them off for being naughty!'''



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
            userid = request.headers.get('X-Replit-User-Id')
            if userid == '13197838':  # Replace with your actual user ID
                session['username'] = username
                return redirect(url_for('admin'))
            else:
                return "Naughty! You are not allowed to access the admin page."
        else:
            return "Invalid credentials, please try again."
    return render_template('login.html')

# Admin page route
@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if 'username' not in session or session['username'] != 'amprente':
        return redirect(url_for('home'))

    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        post_id = str(len(db.keys()) + 1)
        db[post_id] = {'title': title, 'content': content, 'date': date}
        return redirect(url_for('admin'))

    keys = list(db.keys())
    posts = [db[key] for key in reversed(keys)]
    return render_template('dashboard.html', posts=posts)

# Logout route
@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('home'))

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=81)


