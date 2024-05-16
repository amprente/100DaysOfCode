from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    metal = request.form.get('metal')
    dream = request.form.get('dream').lower()
    origin = request.form.get('origin')

    is_robot = False

    # Check radio button answer
    if metal == 'yes':
        is_robot = True

    # Check free text input
    robot_keywords = ['ed-209', 'robot', 'cybernetic']
    if any(keyword in dream for keyword in robot_keywords):
        is_robot = True

    # Check dropdown answer
    if origin == 'yes':
        is_robot = True

    if is_robot:
        result_text = "You're a robot"
        result_class = "text-red-500"
    else:
        result_text = "Not a robot"
        result_class = "text-green-500"

    return render_template('result.html', result_text=result_text, result_class=result_class)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81)
