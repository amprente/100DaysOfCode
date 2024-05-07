'''The first time the diary is run, the user must create a username and password.
Salt & hash the password and store it in the database with the username as the key.
Then proceed to the diary.
The next time that program is run, it should prompt for the username and password, and only allow access if they are correct.
The username, password, and salt should be excluded from diary entry outputs, for obvious reasons.'''


import datetime
import sys
from replit import db
from hashlib import sha256
import os  
import getpass

SALT_SIZE = 16
HASH_ITERATIONS = 100000

def hash_password(password: str, salt: bytes) -> bytes:
    return sha256(salt + password.encode()).hexdigest()

def get_password_input(prompt: str) -> str:
    return getpass.getpass(prompt)

def create_user():
    username = input("Create a new username: ").strip()
    password = get_password_input("Create a new password: ").strip()

    salt = os.urandom(SALT_SIZE)
    password_hash = hash_password(password, salt)
    db[username] = {"salt": salt.hex(), "password_hash": password_hash, "diary": {}}

    print("User created successfully!")
    return username

def authenticate_user():
    username = input("Enter your username: ").strip()
    if username not in db:
        print("Username not found. Please create a new account.")
        sys.exit()

    user_data = db[username]
    password = get_password_input("Enter your password: ").strip()
    salt = bytes.fromhex(user_data["salt"])
    password_hash = hash_password(password, salt)

    if password_hash != user_data["password_hash"]:
        print("\nIncorrect password. Exiting.")
        sys.exit()

    return username

def add_entry(username):
    entry = input("\nType your diary entry: ")
    timestamp = datetime.datetime.now()
    diary = db[username]["diary"]
    diary[timestamp.isoformat()] = entry
    db[username] = {"salt": db[username]["salt"], "password_hash": db[username]["password_hash"], "diary": diary}
    print("Entry added.")

def view_entries(username):
    diary = db[username]["diary"]
    if not diary:
        print("\nNo entries to display.")
        return

    for date, entry in sorted(diary.items(), reverse=True):
        print(f"\nEntry from {date}:")
        print(entry)
        if input("\nType 'next' to view the next entry or 'menu' to return to the main menu: ") == "menu":
            break

def view_entry_from_specific_date(username):
    diary = db[username]["diary"]
    date_str = input("Enter the date (YYYY-MM-DD): ")
    try:
        date_requested = datetime.datetime.strptime(date_str, "%Y-%m-%d")
        entries = {date: diary[date] for date in diary if datetime.datetime.fromisoformat(date).date() == date_requested.date()}
        if entries:
            for date, entry in sorted(entries.items(), reverse=True):
                print(f"\nEntry from {date}:")
                print(entry)
        else:
            print("\nNo entries found for that date.")
    except ValueError:
        print("Invalid date format.")

def main():
    print("=_= PRIVATE DIARY =_= ✍\n")

    if len(db.keys()) == 0:
        print("First-time setup:")
        username = create_user()
    else:
        username = authenticate_user()

    while True:
        print("\nMain Menu:")
        print("\n1. Add Entry")
        print("2. View Entries")
        print("3. View Entry from Specific Date")
        print("4. Exit\n")
        choice = input("Choose an option: ")

        if choice == "1":
            add_entry(username)
        elif choice == "2":
            view_entries(username)
        elif choice == "3":
            view_entry_from_specific_date(username)
        elif choice == "4":
            print("Exiting.")
            break
        else:
            print("\nInvalid option. Please choose again.")

if __name__ == "__main__":
    main()
