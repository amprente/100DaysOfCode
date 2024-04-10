# 1. Create a dictionary to store the beast's details
mokebeast = {}

# 2. Ask the user to input the details
details = input("Enter the beast's name, type (earth, fire, air, water or spirit), special move, starting HP, and starting MP separated by commas: ").split(", ")

# Check if the user input contains the correct number of values
if len(details) != 5:
    print("Invalid input. Please provide all the required details separated by commas.")
else:
    mokebeast["name"] = details[0]
    mokebeast["type"] = details[1].lower()
    mokebeast["special_move"] = details[2]
    mokebeast["hp"] = int(details[3])
    mokebeast["mp"] = int(details[4])

    # 3. Output the beast's details
    print(f"\n👾 MokéBeast - The Beast Battle Game 👾")

    # 4. Change the text color based on the beast's type
    if mokebeast["type"] == "earth":
        color = "\033[32m"  # Green
    elif mokebeast["type"] == "fire":
        color = "\033[31m"  # Red
    elif mokebeast["type"] == "water":
        color = "\033[34m"  # Blue
    elif mokebeast["type"] == "air":
        color = "\033[37m"  # White
    else:
        color = "\033[35m"  # Purple (for spirit)

    print(f"\n{color}Your beast is called {mokebeast['name']}. It is a {mokebeast['type']} beast with a special move of {mokebeast['special_move']}\033[0m")
    print(f"\nStarting HP: {mokebeast['hp']} \nStarting MP: {mokebeast['mp']}")