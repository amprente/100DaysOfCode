'''If the URL ends in /english, then display the English page.
If it ends in /otherLanguage, then display your translated page instead.'''


from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def default_page():
    return render_template('english.html')

@app.route('/<language>')
def language_page(language):
    if language == 'english':
        return render_template('english.html')
    elif language == 'otherLanguage':
        return render_template('otherLanguage.html')
    else:
        return "Page not found", 404

if __name__ == '__main__':
     app.run(host='0.0.0.0', port=81)
