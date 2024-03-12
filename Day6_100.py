print("Welcome to the fantastical realm of...")

world = "Earth"  
print(world + "! Where magic and wonder intertwine.")
print()

username = input("Enter your adventurer's name: ")
password = input("Speak the secret word to unlock the portal: ")

print()


if username == "user1" and password == "abracadabra":
    print("Greetings, " + username + "! The mystical gateway to " + world + " awaits!")
elif username == "user2" and password == "open sesame":
    print("By uttering the forgotten phrase, " + username + ", you reveal the path to " + world + "!")
elif username == "user3" and password == "friend":
    print("Welcome, " + username + ", your friendship grants you passage to the extraordinary " + world + "!")
else:
    print("The ancient incantations seem unfamiliar to you, " + username + ". Perhaps another forgotten word holds the key?")
