print("Welcome to 'Name the Lyrics' game!")
print()
print("""Let's see if you can complete the mmissing word from lyrics...
~I'm feeling alright, I'm gonna ____ the night~""")
print()

# Define the song lyrics with blanks
lyrics = "I'm feeling alright, I'm gonna ____ the night"
# Define the correct answer
correct_answer = "own"
attempts = 0

# Start the game loop
while True:
    # Ask the user for input
    user_input = input("Complete the lyrics: ")
    attempts += 1

    # Check if the user input matches the correct answer
    if user_input == correct_answer:
        print("Well done! It only took you " + str(attempts) + " attempts.")
        break
    else:
        print("Not quite, give it another shot!")
        print()
