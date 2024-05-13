'''Build a place to store your reflections on the next 22 days of code.'''

from flask import Flask, render_template
app = Flask(__name__)

# Data storing the content for each day
days_content = {
    "78": {
        "title": "Day 78 Reflection",
        "reflection": "Today I learned about Flask dynamic routing...",
        "repl_link": "https://replit.com/@Amprente/Day-78100?v=1#main.py"
    },
    "79": {
        "title": "Day 79 Reflection",
        "reflection": "Reflections on Flask templates and styling...",
        "repl_link": "https://replit.com/@Amprente/Day-79100?v=1#main.py"
    }
    # Add more days as needed
}

@app.route('/<dayNumber>')
def index(dayNumber):
    day_info = days_content.get(dayNumber, None)
    if day_info:
        return render_template('day_template.html', day=day_info)
    else:
        return f"No reflection found for day {dayNumber}", 404

app.run(host='0.0.0.0', port=81)
