import requests, os
import openai

# API keys
NEWS_API_KEY = os.environ['newsapi']
OPENAI_API_KEY = os.environ['openai']
ORGANIZATION_ID = os.environ['organizationID']

openai.api_key = OPENAI_API_KEY

def fetch_top_news(api_key, country='us', category='general', page_size=5):
    url = ('https://newsapi.org/v2/top-headlines?'
           f'country={country}&'
           f'category={category}&'
           f'pageSize={page_size}&'
           f'apiKey={api_key}')
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

def summarize_article(url):
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": f"Summarize the following article: {url}"}
    ]
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        max_tokens=150
    )
    return response.choices[0].message['content'].strip()

def main():
    print("Fetching top news stories...")
    news_data = fetch_top_news(NEWS_API_KEY)
    articles = news_data.get('articles', [])

    if not articles:
        print("No news articles found.")
        return

    for idx, article in enumerate(articles):
        print(f"\nArticle {idx + 1}: {article['title']}")
        print(f"Source: {article['source']['name']}")
        print(f"URL: {article['url']}")

        try:
            summary = summarize_article(article['url'])
            print(f"Summary: {summary}")
        except Exception as e:
            print(f"Failed to summarize article: {e}")

if __name__ == "__main__":
    main()
