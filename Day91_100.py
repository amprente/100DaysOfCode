# Give you a random joke

import requests
import replit
from replit import db

# Function to fetch a random joke
def fetch_random_joke():
    url = "https://icanhazdadjoke.com/"
    headers = {"Accept": "application/json"}
    response = requests.get(url, headers=headers)
    data = response.json()
    return data['id'], data['joke']

# Function to save a joke ID to the Replit DB
def save_joke(joke_id):
    if 'joke_ids' not in db:
        db['joke_ids'] = []
    db['joke_ids'].append(joke_id)
    #print(f"Debug: Current saved joke IDs: {db['joke_ids']}")  # Debugging line

# Function to fetch a joke by ID
def fetch_joke_by_id(joke_id):
    url = f"https://icanhazdadjoke.com/j/{joke_id}"
    headers = {"Accept": "application/json"}
    response = requests.get(url, headers=headers)
    data = response.json()
    return data['joke']

# Function to display saved jokes
def display_saved_jokes():
    if 'joke_ids' in db:
        for joke_id in db['joke_ids']:
            print(fetch_joke_by_id(joke_id))
    else:
        print("No jokes saved yet.")

def main():
    joke_id, joke = fetch_random_joke()
    print("Here's a random joke for you:\n")
    print(joke)

    save = input("\nDo you want to save this joke? (yes/no): ").strip().lower()
    if save == 'yes':
        save_joke(joke_id)
        print("Joke saved!\n")

    show_saved = input("\nDo you want to see your saved jokes? (yes/no): ").strip().lower()
    if show_saved == 'yes':
        print("Here are your saved jokes:\n")
        display_saved_jokes()

if __name__ == "__main__":
    main()
