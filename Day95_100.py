import os
import openai
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from newsapi import NewsApiClient

# Set your API keys
NEWS_API_KEY = os.getenv('NEWS_API_KEY')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
SPOTIPY_CLIENT_ID = os.getenv('SPOTIPY_CLIENT_ID')
SPOTIPY_CLIENT_SECRET = os.getenv('SPOTIPY_CLIENT_SECRET')

# Initialize APIs
newsapi = NewsApiClient(api_key=NEWS_API_KEY)
openai.api_key = OPENAI_API_KEY

# Initialize Spotify API without cache
auth_manager = SpotifyClientCredentials(client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET)
sp = spotipy.Spotify(auth_manager=auth_manager, requests_session=False)

# Get the top 5 news stories
def get_top_news():
    top_headlines = newsapi.get_top_headlines(language='en', page_size=5)
    return top_headlines['articles']

# Summarize the news stories
def summarize_article(url):
    prompt = f"Summarize the article at {url} in no more than four words."
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=5
    )
    return response.choices[0].message['content'].strip()

# Search for songs on Spotify
def search_spotify(query):
    results = sp.search(q=query, limit=1, type='track')
    if results['tracks']['items']:
        track = results['tracks']['items'][0]
        return track['name'], track['preview_url']
    return None, None

def main():
    articles = get_top_news()
    for article in articles:
        summary = summarize_article(article['url'])
        track_name, preview_url = search_spotify(summary)
        if track_name and preview_url:
            print(f"Track Name: {track_name}")
            print(f"Prompt Words: {summary}")
            print(f"Sample URL: {preview_url}\n")

if __name__ == "__main__":
    main()
