'''Have two types of user - admin and normal. Each should have their own username and password.
The admin user should be greeted with 'Hello admin'.
The normal user should be greeted with 'Hello normie'.'''


print("=_= Login System =_=")
print()
# User database
users = {
    "admin1": ("password123", "admin"),
    "user1": ("password456", "normal")
}

def login(username, password):
    # Check if the username exists and the password matches
    if username in users and users[username][0] == password:
        return users[username][1]
    return None

def greet(user_type):
    # Greet user based on type
    if user_type == "admin":
        print("\nHello admin")
    elif user_type == "normal":
        print("\nHello normie")

def main():
    # Input from user
    username = input("Enter username: ")
    password = input("Enter password: ")

    # Attempt to login
    user_type = login(username, password)
    if user_type:
        greet(user_type)
    else:
        print("Invalid username or password")

# Run the program
if __name__ == "__main__":
    main()
