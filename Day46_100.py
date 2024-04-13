import sys

# Function to add ANSI color to text
def add_color(text, color):
    colors = {
        "red": "\033[91m",
        "green": "\033[92m",
        "yellow": "\033[93m",
        "blue": "\033[94m",
        "magenta": "\033[95m",
        "cyan": "\033[96m",
        "white": "\033[97m",
        "reset": "\033[0m"
    }
    return colors[color] + text + colors["reset"]

print(add_color("🌟 MokeBeast Generator 🌟\n", "cyan"))

# Initialize an empty dictionary to store the Mokébeasts
mokedex = {}

while True:
    # Get user input for the beast's details
    name = input("Input the beast name > ").strip().title()
    element = input("Input the beast element > ").strip().capitalize()
    special_move = input("Input the beast special move > ").strip().capitalize()
    hp = int(input("Input the beast starting HP > "))
    mp = int(input("Input the beast starting MP > "))

    # Add the beast to the Mokédex
    mokedex[name] = {
        "element": element,
        "special move": special_move,
        "HP": hp,
        "MP": mp
    }

    # Ask the user if they want to add another beast
    again = input("\nAgain? y/n > ")
    if again.lower() != 'y':
        break

def prettyPrint(mokedex):
    # Output the full Mokédex
    for name, details in mokedex.items():
        details_str = f"name: {add_color(name, 'green')} | element: {add_color(details['element'], 'red')} | special move: {add_color(details['special move'], 'yellow')} | HP: {add_color(str(details['HP']), 'blue')} | MP: {add_color(str(details['MP']), 'magenta')}"
        print(details_str)

prettyPrint(mokedex)
