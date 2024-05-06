import hashlib
import random
from getpass import getpass
from replit import db  

def generate_salt():
    return str(random.randint(1000, 9999))

def hash_password(password, salt):
    hasher = hashlib.sha256()
    hasher.update(f"{password}{salt}".encode())
    return hasher.hexdigest()

def add_user():
    username = input("\nUsername: ")
    if username in db.keys():
        print("\nUser already exists!")
        return
    password = getpass("\nPassword: ")
    salt = generate_salt()
    password_hash = hash_password(password, salt)
    db[username] = {'salt': salt, 'hash': password_hash}  # Storing data in repl db
    print("\nDetails stored.")

def login():
    username = input("\nUsername: ")
    if username not in db.keys():
        print("\nUser not found!")
        return
    password = getpass("\nPassword: ")
    user_data = db[username]  # Retrieving user data from repl db
    salt = user_data['salt']
    password_hash = hash_password(password, salt)
    if password_hash == user_data['hash']:
        print("\nLogin successful")
    else:
        print("\nInvalid password!")

def main():
    while True:
        print("\n🌟Login System🌟")
        choice = input("\n1: Add User, 2: Login, 3: Exit > ")
        if choice == '1':
            add_user()
        elif choice == '2':
            login()
        elif choice == '3':
            print("\nExiting...")
            break
        else:
            print("\nInvalid choice")

if __name__ == "__main__":
    main()
