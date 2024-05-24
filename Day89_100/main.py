'''Build a community chat app.'''


from flask import Flask, render_template, request, redirect, url_for, session
from replit import db
import time

app = Flask(__name__)
app.secret_key = 'ampry'  # Replace with a secure key

# Ensure admin username is correctly set
ADMIN_USERNAME = "Amprente"

@app.route('/')
def index():
    if 'username' in session:
        return redirect(url_for('chat'))
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    session['username'] = username
    # In a real application, you would add proper authentication here.
    return redirect(url_for('chat'))

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

@app.route('/chat', methods=['GET', 'POST'])
def chat():
    if 'username' not in session:
        return redirect(url_for('index'))

    username = session['username']
    profile_pic = "https://source.unsplash.com/random/30x30?profile"  # Example profile picture

    if request.method == 'POST':
        message = request.form['message']
        timestamp = str(int(time.time() * 1000))
        db[timestamp] = {
            'username': username,
            'profile_pic': profile_pic,
            'message': message
        }
        return redirect(url_for('chat'))

    # Fetch the last five messages
    messages = sorted(db.items(), key=lambda x: x[0], reverse=True)[:5]

    return render_template('chat.html', messages=messages, username=username, admin=username == ADMIN_USERNAME)

@app.route('/delete/<timestamp>')
def delete_message(timestamp):
    if 'username' not in session or session['username'] != ADMIN_USERNAME:
        return redirect(url_for('index'))

    del db[timestamp]
    return redirect(url_for('chat'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81)
