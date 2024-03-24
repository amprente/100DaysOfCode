import random

print("~ Guess the Number! ~")
print()
print("""Try to guess a number between 1 and 1,000,000 and I will tell you if you are too low, too high, or get it""")
print()

# Pick a number between 1 and 1,000,000
correct_number = random.randint(1, 1000000)

# Counter for the number of attempts
attempts = 0

while True:
    # Ask the user to guess the number
    guess = input("Guess the number or type 'exit' to quit: ")

    # If the user types 'exit', quit the game
    if guess.lower() == 'exit':
        print("You chose to exit the game. Goodbye!")
        break

    # Convert the guess to an integer
    guess = int(guess)

    # If the user types a number outside the range 1-1,000,000, ask them to guess again
    if guess < 1 or guess > 1000000:
        print("Please enter a number between 1 and 1,000,000.")
        continue

    # Count the attempt
    attempts += 1

    # Check if the guess is too low, too high, or correct
    if guess < correct_number:
        print("Too low!")
    elif guess > correct_number:
        print("Too high!")
    else:
        print("You're a winner! 🎉")
        print("It took you", attempts, "attempts to guess the number.")
        break
