from flask import Flask


app = Flask(__name__, static_url_path="/static")

@app.route('/')
def index():
    return 'Hello from Flask!'


@app.route('/portfolio')
def portfolio():
    page = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Portfolio</title>
    <!-- Link to the CSS file -->
    <link href="/static/css/portfolio.css" rel="stylesheet" type="text/css" />
</head>
<body>

    <h1>Amprente's - Portfolio</h1>

    <div class="project">
        <h2> - Calculator - 📅</h2>
        <p>This project is a calculator that performs basic arithmetic operations. It includes functions for addition, subtraction, multiplication, and division.</p>
        <a href="https://replit.com/@Amprente/Day-66100">
            <img src="/static/Images/calculator.jpg" alt="Calculator Project">
        </a>
    </div>

    <div class="project">
        <h2>🌟Jobs Jobs Jobs!🌟</h2>
        <p>This project helps users create classes to represent jobs and get an output with the information for each job.</p>
        <a href="https://replit.com/@Amprente/Day-64100">
            <img src="/static/Images/jobs.jpg" alt="Jobs Jobs Jobs Project">
        </a>
    </div>

    <div class="project">
        <h2>=_= PRIVATE DIARY =_= ✍</h2>
        <p>This is a private digital diary where users can record their daily thoughts and activities. It has features like encryption for privacy and a search function.</p>
        <a href="https://replit.com/@Amprente/Day-72100">
            <img src="/static/Images/private_diary.jpg" alt="Private Diary Project">
        </a>
    </div>

    <div class="project">
        <h2>🍕 Pizza Shop 🍕</h2>
        <p>This project simulates a pizza ordering system. Customers can choose their preferred toppings and place orders online.</p>
        <a href="https://replit.com/@Amprente/Day-52100">
            <img src="/static/Images/pizza_shop.jpg" alt="Pizza Shop Project">
        </a>
    </div>

    <div class="project">
        <h2>🌟Life Organizer🌟</h2>
        <p>This project helps users organize their daily tasks and priorities. It includes features like task lists, calendar integration, and reminders.</p>
        <a href="https://replit.com/@Amprente/Day-51100">
            <img src="/static/Images/life_organizer.jpg" alt="Life Organizer Project">
        </a>
    </div>

</body>
</html>
"""
    return page


@app.route('/linktree')
def linktree():
    page = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Portfolio - Maura Pascariu</title>
    <!-- Include Google Fonts -->
    <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;700&display=swap" rel="stylesheet">
    <!-- Link to External CSS -->
    <link href="static/css/linktree.css" rel="stylesheet" type="text/css" />
</head>
<body>
    <header class="header">
        <img src="/static/Images/Amprente.png" alt="Profile Photo">
        <h1>Maura Pascariu</h1>
        <p>Welcome to my portfolio page!</p>
    </header>

    <section class="social-links">
        <h2>Social Media</h2>
        <a href="https://replit.com/@Amprente" target="_blank" class="social-link">Replit</a>
        <a href="https://github.com/amprente" target="_blank" class="social-link">GitHub</a>
        <a href="https://www.linkedin.com/in/mauura/" target="_blank" class="social-link">LinkedIn</a>
    </section>

    <section class="portfolio">
        <h2>My Portfolio</h2>
        <a href="https://replit.com/@Amprente/Day-74100?v=1#index.html" target="_blank" class="portfolio-item">Projects under development</a>        
    </section>

</body>
</html>
"""
    return page

app.run(host='0.0.0.0', port=81)
