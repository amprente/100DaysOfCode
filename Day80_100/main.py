'''Go and grab your login form code from yesterday.
Connect it up to Flask.
Make it work.'''

from flask import Flask, request, render_template

app = Flask(__name__)

# Dictionary storing valid username and password combinations
valid_users = {
    "user1": "pass1",
    "user2": "pass2",
    "user3": "pass3"
}

@app.route('/')
def login_form():
    return render_template('login_form.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    if valid_users.get(username) == password:
        return render_template('success.html', username=username)
    else:
        return render_template('failure.html'), 403

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81)
