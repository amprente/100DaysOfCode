import random
import time
import os

def generate_character():
    first_names = ['Sheila', 'John', 'Alice', 'Bob', 'Emma', 'David', 'Sophia', 'Michael', 'Olivia' , 'William', 'Emily', 'James', 'Ava', 'Benjamin']
    character_types = ['Human', 'Imp', 'Wizard', 'Elf', 'Orc', 'Dwarf', 'Gnome', 'Fairy', 'Dragon', 'Undead']
    name = random.choice(first_names)
    character_type = random.choice(character_types)
    return name, character_type

def roll_dice(sides):
    return random.randint(1, sides)

def generate_health():
    health = 1
    for _ in range(3):  # Roll a 6-sided dice 3 times
        health *= roll_dice(6)
    return health

def generate_strength():
    strength = 1
    for _ in range(3):  # Roll a 6-sided dice 3 times
        strength *= roll_dice(6)
    return strength

while True:
    name, character_type = generate_character()
    health = generate_health()
    strength = generate_strength()

    print("~ Character Builder ~")
    print()
    print("Name of Your Hero:")
    print()
    print(name + " the " + character_type)
    print("HEALTH: " + str(health))
    print("STRENGTH: " + str(strength))
    print()
    print("May your name go down in Legend...")
    print("")

    play_again = input("Would you like to create another character? (yes/no): ")
    if play_again != "yes":
        break

    time.sleep(2)
    os.system('clear')
