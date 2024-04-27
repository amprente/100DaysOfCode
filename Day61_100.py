'''Display a menu - Add or View tweets.

'Add' should:

Get the tweet input.
Store it to the database with the current timestamp as the key value.
'View' should:

Show the tweets in reverse chronological order.
Show 10 tweets at a time.
Prompt the user to show another 10 tweets (yes or no).
A 'no' choice goes back to the menu.'''


import os
import datetime
from replit import db

def clear_screen():
    os.system('clear')  # use 'cls' if on Windows

def add_tweet():
    tweet = input("\nWhat's on your mind today? ")
    timestamp = datetime.datetime.now()
    db[timestamp.isoformat()] = tweet
    print("\nTweet added!")

def view_tweets():
    keys = sorted(db.keys(), reverse=True)
    index = 0
    while index < len(keys):
        clear_screen()
        for _ in range(10):
            if index < len(keys):
                print(f"{keys[index]}: {db[keys[index]]}")
                index += 1
        if index >= len(keys) or input("\nShow next 10 tweets? (yes/no) ") == 'no':
            break

def main_menu():
    while True:
        choice = input("\nChoose an option - Add (A) or View (V) tweets, or Quit (Q): ")
        if choice.lower() == 'a':
            add_tweet()
        elif choice.lower() == 'v':
            view_tweets()
        elif choice.lower() == 'q':
            break
        else:
            print("\nInvalid option, please choose again.")

if __name__ == "__main__":
    main_menu()
