import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import schedule
import time
from replit import db
import os

# Define the email sender (Replit username) and retrieve the receiver's email and password from secrets
email_sender = os.environ['EMAIL_SENDER']
email_password = os.environ['EMAIL_PASSWORD']
email_receiver = os.environ['EMAIL_RECEIVER']

# Define the topics of interest
topics_of_interest = ['Python', 'Machine Learning', 'Data Science']

# Define the URL of the Replit Community Hub events page
url = 'https://replit.com/community-hub'

# Function to scrape the Replit Community Hub for events
def scrape_events():
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    events = []

    # Example parsing logic (adjust based on actual HTML structure)
    for event in soup.find_all('div', class_='event'):
        title = event.find('h3').text
        link = event.find('a')['href']
        description = event.find('p').text
        events.append({'title': title, 'link': link, 'description': description})

    return events

# Function to filter events by topics of interest
def filter_events(events, topics):
    filtered_events = []
    for event in events:
        for topic in topics:
            if topic.lower() in event['title'].lower() or topic.lower() in event['description'].lower():
                filtered_events.append(event)
                break
    return filtered_events

# Function to send an email notification
def send_email(event):
    subject = f"New Event: {event['title']}"
    body = f"Check out this new event: {event['title']}\n\nDescription: {event['description']}\n\nLink: {event['link']}"

    msg = MIMEMultipart()
    msg['From'] = email_sender
    msg['To'] = email_receiver
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(email_sender, email_password)
        text = msg.as_string()
        server.sendmail(email_sender, email_receiver, text)
        server.quit()
        print(f"Email sent to {email_receiver} about event: {event['title']}")
    except Exception as e:
        print(f"Failed to send email: {e}")

# Function to check and notify new events
def check_and_notify():
    events = scrape_events()
    filtered_events = filter_events(events, topics_of_interest)

    for event in filtered_events:
        if event['link'] not in db:
            db[event['link']] = event['title']
            send_email(event)

# Schedule the check_and_notify function to run every 6 hours
schedule.every(6).hours.do(check_and_notify)

# Run the scheduler
while True:
    schedule.run_pending()
    time.sleep(1)
