import random
import time
import os

def generate_character():
    first_names = ['Sheila', 'John', 'Alice', 'Bob', 'Emma', 'David', 'Sophia', 'Michael', 'Olivia', 'William', 'Emily', 'James', 'Ava', 'Benjamin']
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

def character_damage(attacker_strength, defender_health):
    damage = max(0, attacker_strength - defender_health) + 3
    return damage

# ANSI color codes
COLOR_RESET = '\033[0m'
COLOR_GREEN = '\033[92m'
COLOR_RED = '\033[91m'
COLOR_BLUE = '\033[94m'

# Initialize characters
character1_name, character1_type = generate_character()
character1_health = generate_health()
character1_strength = generate_strength()

character2_name, character2_type = generate_character()
character2_health = generate_health()
character2_strength = generate_strength()

round_count = 1

while True:
    print("*" * 20)
    print(COLOR_BLUE + "⚔️  BATTLE TIME ⚔️" + COLOR_RESET)
    print("*" * 20)
    print()
    print("Round " + str(round_count))
    print()

    print(COLOR_GREEN + character1_name + " the " + character1_type + COLOR_RESET)
    print("HEALTH: " + str(character1_health))
    print("STRENGTH: " + str(character1_strength))
    print()

    print(COLOR_RED + character2_name + " the " + character2_type + COLOR_RESET)
    print("HEALTH: " + str(character2_health))
    print("STRENGTH: " + str(character2_strength))
    print()

    time.sleep(3)
    os.system('clear')

    # Simulate battle
    print("💥 The battle begins!💥")
    print()
    time.sleep(3)

    character1_roll = roll_dice(6)
    character2_roll = roll_dice(6)

    if character1_roll > character2_roll:
        print(COLOR_BLUE + character1_name + " wins the first blow!💪" + COLOR_RESET)
        damage = character_damage(character1_strength, character2_health)
        character2_health -= damage
        print(COLOR_RED + character2_name + " takes a hit, with " + str(damage) + " damage" + COLOR_RESET)
    elif character2_roll > character1_roll:
        print(COLOR_RED + character2_name + " wins the first blow!💪" + COLOR_RESET)
        damage = character_damage(character2_strength, character1_health)
        character1_health -= damage
        print(COLOR_BLUE + character1_name + " takes a hit, with " + str(damage) + " damage" + COLOR_RESET)
    else:
        print("It's a tie! No damage dealt.👉👈")

    print()
    print(COLOR_BLUE + character1_name + " HEALTH: " + str(character1_health) + COLOR_RESET)
    print(COLOR_RED + character2_name + " HEALTH: " + str(character2_health) + COLOR_RESET)

    if character1_health <= 0:
        print("Oh no! " + COLOR_GREEN + character1_name + " has died!👻" + COLOR_RESET)
        print()
        print(COLOR_RED + character2_name + " wins the battle!🏆" + COLOR_RESET)
        break
    elif character2_health <= 0:
        print("Oh no! " + COLOR_RED + character2_name + " has died!👻" + COLOR_RESET)
        print()
        print(COLOR_GREEN + character1_name + " wins the battle!🏆" + COLOR_RESET)
        print()
        break

    round_count += 1
    print()
    time.sleep(5)
    os.system('clear')
