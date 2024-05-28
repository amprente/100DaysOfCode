import schedule
import time
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import random

# Function to read quotes from a text file
def read_quotes(filename):
    with open(filename, 'r') as file:
        quotes = file.readlines()
    return [quote.strip() for quote in quotes]

password = os.environ['mailPassword']
username = os.environ['mailUsername']

def sendMail():
    quotes = read_quotes('quotes.txt')
    quote = random.choice(quotes)  # Pick a random quote

    server = "smtp.gmail.com"  # Address of the mail server
    port = 587  # Port of the mail server
    s = smtplib.SMTP(host=server, port=port)  # Creates the server connection
    s.starttls()  # Sets the encryption mode
    s.login(username, password)  # Logs into the email server

    msg = MIMEMultipart()  # Creates the message
    msg['To'] = "samemail@email.com"  # Replace with the recipient's email address
    msg['From'] = f"Motivational Bot <{username}>"  # Sets the sender's display name and email address
    msg['Subject'] = "Your Daily Motivational Quote"  # Sets the subject of the message
    msg.attach(MIMEText(quote, 'html'))  # Attaches the quote content to the message as HTML

    s.send_message(msg)  # Sends the message
    del msg  # Deletes the message from memory

# Schedule the task to send a motivational quote every day at 8 AM
schedule.every().day.at("08:00").do(sendMail)


# Keep the script running
while True:
    schedule.run_pending()
    time.sleep(60)  # Wait one minute

if __name__ == "__main__":
    sendMail()  # Send a quote immediately when the script is run for the first time
