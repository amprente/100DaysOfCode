# Show 10 songs from that year

from flask import Flask, request, render_template, url_for
import requests
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import os

app = Flask(__name__)

# Set up Spotify API credentials from environment variables
SPOTIFY_CLIENT_ID = os.getenv('SPOTIFY_CLIENT_ID')
SPOTIFY_CLIENT_SECRET = os.getenv('SPOTIFY_CLIENT_SECRET')

# Check if credentials are correctly fetched
if not SPOTIFY_CLIENT_ID or not SPOTIFY_CLIENT_SECRET:
    raise ValueError("Spotify Client ID and Secret must be set in the environment variables.")

# Initialize Spotify API client
auth_manager = SpotifyClientCredentials(client_id=SPOTIFY_CLIENT_ID, client_secret=SPOTIFY_CLIENT_SECRET)
sp = spotipy.Spotify(auth_manager=auth_manager)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        year = request.form['year']
        offset = int(request.form.get('offset', 0))
        songs = get_songs(year, offset)
        return render_template('index.html', songs=songs, year=year, offset=offset)
    return render_template('index.html', songs=[], year='', offset=0)

def get_songs(year, offset):
    # Query Spotify API for songs from the specified year
    query = f'year:{year}'
    results = sp.search(q=query, type='track', limit=10, offset=offset)
    songs = []
    for item in results['tracks']['items']:
        song = {
            'name': item['name'],
            'artist': item['artists'][0]['name'],
            'preview_url': item['preview_url']
        }
        songs.append(song)
    return songs

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81, debug=True)
