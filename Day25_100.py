import random

print("~ ⚔️  Character Stats Generator ⚔️  ~")
print()
print()

def roll_dice(sides):
    """Roll a dice of any size and return the result."""
    return random.randint(1, sides)

def calculate_health():
    """Roll a six-sided dice and an eight-sided dice, multiply the results together, and return the result."""
    return roll_dice(6) * roll_dice(8)

def generate_character():
    """Ask the user for a character name and generate health stats for the character."""
    name = input("Name your hero: ")
    print()
    health = calculate_health()
    print("\033[92m" + "Your hero's name is: " + name + "\033[0m")  # Print the name in green
    print("\x1b[1;31m" + "The health status is: " + str(health) + "hp ❤ ❤ ❤" + "\033[0m")  # Print the health in red
    print()

def main():
    """Main function to generate characters and their health stats."""
    while True:
        generate_character()
        cont = input("Do you want to generate health stats for another character? (y/n): ")
        print()
        if cont != "y":
            break

if __name__ == "__main__":
    main()
