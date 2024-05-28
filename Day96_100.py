import requests
from bs4 import BeautifulSoup

# URL of Hacker News
url = 'https://news.ycombinator.com/'

# Fetch the content from the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code != 200:
    print("Failed to retrieve the webpage")
    exit()

content = response.content

# Parse the HTML content
soup = BeautifulSoup(content, 'html.parser')

# Find all the headlines
headlines = soup.find_all('a', class_='storylink')

# Debug: Print all headlines
print("All headlines:")
for headline in headlines:
    print(headline.get_text())

print("\nFiltered headlines containing 'Python' or 'Replit':")

# Iterate through headlines and display those containing 'Python' or 'Replit'
for headline in headlines:
    title = headline.get_text()
    if 'Python' in title or 'Replit' in title:
        print(title)
