'''Change theme as an example:
blog/entry2?theme=dark
blog/entry1?theme=light'''

from flask import Flask, render_template, redirect, url_for, request
from datetime import date

app = Flask(__name__, static_folder='static', template_folder='template')

# Blog entries data
entries = {
    "entry1": {
        "heading": "Hello Everyone!",
        "date": str(date.today()),
        "content": "This is the content of the first blog post."
    },
    "entry2": {
        "heading": "Life is Really, Really Good!",
        "date": str(date.today()),
        "content": "This is the content of the second blog post."
    }
}

@app.route('/')
def home():
    return redirect(url_for('blog_entry', entry_id='entry1'))

@app.route('/blog/<entry_id>')
def blog_entry(entry_id):
    entry = entries.get(entry_id)
    theme = request.args.get('theme', 'default')
    if entry:
        return render_template('blog.html', theme=theme, **entry)
    else:
        return "Blog entry not found", 404

@app.route('/1')
def redirect_to_entry1():
    return redirect(url_for('blog_entry', entry_id='entry1'))

@app.route('/2')
def redirect_to_entry2():
    return redirect(url_for('blog_entry', entry_id='entry2'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81)
