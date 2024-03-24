import random

def roll_dice(sides):
    return random.randint(1, sides)

def play_game():
    print("Infinity Dice 🎲")
    print()
    sides = int(input("How many sides?: "))
    keep_playing = "yes"
    print()

    while keep_playing == "yes":
        print("You rolled " + str(roll_dice(sides)))
        keep_playing = input("Roll again? ")
        print()

    print("Thanks for playing!")

# Start the game
play_game()
