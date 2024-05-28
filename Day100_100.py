import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

# Dictionary to store product info
products = {
    "Samsung Galaxy S24 Ultra": {
        "url": "https://www.emag.ro/telefon-mobil-samsung-galaxy-s24-ultra-dual-sim-12gb-ram-512gb-5g-titanium-black-sm-s928bzkheue/pd/DF6L7KYBM/",
        "current_price": 6.229,
        "target_price": 6.000  # Adjust this value as needed
    },
}

# Function to scrape the current price of the product
def scrape_price(url):
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")

    # Correct the price extraction logic
    price_element = soup.find("p", {"class": "product-new-price"})
    if price_element:
        # Sometimes the price might be split into multiple spans for the currency symbol and digits
        price_str = ''.join(price_element.stripped_strings)
        # Clean up the price string to convert it to a float
        price = float(price_str.replace("Lei", "").replace(".", "").replace(",", ".").strip())
        return price
    else:
        raise ValueError("Price element not found on the page")

# Function to send email notification
def email_me(target_price, current_price, url):
    sender_email = os.getenv("EMAIL")
    receiver_email = os.getenv("EMAIL")
    password = os.getenv("PASSWORD")

    subject = "Price Alert!"
    body = f"The price of the product at {url} has dropped to {current_price} Lei.\nYour target price was {target_price} Lei."

    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg["Subject"] = subject

    msg.attach(MIMEText(body, "plain"))

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
        server.close()
        print("Email sent successfully")
    except Exception as e:
        print(f"Error sending email: {e}")

# Main function to check prices and send notifications
def check_prices():
    for key, value in products.items():
        url = value["url"]
        current_price = value["current_price"]
        target_price = value["target_price"]

        try:
            this_price = scrape_price(url)
            if this_price != current_price:
                products[key]["current_price"] = this_price
                if this_price <= target_price:
                    print("Cheaper")
                    email_me(target_price, this_price, url)
        except Exception as e:
            print(f"Error scraping price for {key}: {e}")

if __name__ == "__main__":
    check_prices()
