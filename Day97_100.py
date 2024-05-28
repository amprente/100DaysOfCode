import requests
from bs4 import BeautifulSoup
import openai
import os

# Access OpenAI API key from Replit's Secrets
openai.api_key = os.getenv('OPENAI_API_KEY')

# Function to scrape Wikipedia article
def scrape_wikipedia_article(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract the main content of the article
    content = soup.find('div', {'class': 'mw-parser-output'})
    paragraphs = content.find_all('p')
    article_text = ' '.join([p.get_text() for p in paragraphs])

    # Extract references
    references = soup.find_all('ol', {'class': 'references'})
    reference_text = ' '.join([ref.get_text() for ref in references])
    
    return article_text, reference_text

# Function to summarize text using OpenAI
def summarize_text(text):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"Please summarize the following article in no more than 3 paragraphs:\n\n{text}"}
        ],
        max_tokens=500
    )
    summary = response['choices'][0]['message']['content'].strip()
    return summary

# Main function
def main():
    url = input("Paste wiki URL > ")
    article_text, reference_text = scrape_wikipedia_article(url)
    summary = summarize_text(article_text)
    
    print("Summary:\n")
    print(summary)
    print("\nReferences:\n")
    print(reference_text)

if __name__ == "__main__":
    main()
