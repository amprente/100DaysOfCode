import random

print("Guess the Number!")
print()
print("""Try to guess a number between 1 and 1,000,000 and I will tell you if you are too low, too high, or get it""")
print()

# Pick a number between 0 and 1,000,000
correct_number = random.randint(0, 1000000)

# Counter for the number of attempts
attempts = 0

while True:
    # Ask the user to guess the number
    guess = input("Guess the number or type 'exit' to quit: ")

    # If the user types 'exit', quit the game
    if guess == str('exit'):
        print("You chose to exit the game. Goodbye!")
        break

    # Convert the guess to an integer
    guess = int(guess)

    # If the user types a negative number, exit the program
    if guess < 0:
        print("You entered a negative number. Exiting the program.")
        break

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
