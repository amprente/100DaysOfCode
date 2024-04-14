import os
import random


def clear():
    os.system('clear')

def main():
    # Initial teachers dictionary with dynamic stat ranges
    teachers = {
        'Mr. Jitaru': {'Intelligence': random.randint(70, 100), 'Charisma': random.randint(70, 100), 
                       'Mystery': random.randint(50, 100), 'Coffee Consumption': random.randint(1, 10)},
        'Miss. Bercea': {'Intelligence': random.randint(70, 100), 'Charisma': random.randint(70, 100), 
                         'Mystery': random.randint(50, 100), 'Coffee Consumption': random.randint(1, 10)}
    }

    print("🌟 Top Trumps 🌟\n\nWelcome to the 'Most Eccentric Educators' Simulator")

    while True:
        print("\nWould you like to add a new character? (y/n)")
        if input("> ").lower() == 'y':
            name = input("Enter the character's name: ")
            # Assigning random stats when a new character is added
            teachers[name] = {
                'Intelligence': random.randint(70, 100),
                'Charisma': random.randint(70, 100),
                'Mystery': random.randint(50, 100),
                'Coffee Consumption': random.randint(1, 10)
            }

        # Display teachers
        print("\nChoose your card:")
        for index, name in enumerate(teachers, start=1):
            print(f"{index} - {name}")

        # Players choose a card
        choice = int(input("> ")) - 1
        if choice < 0 or choice >= len(teachers):
            print("\nInvalid choice, try again.")
            continue
        chosen_teacher = list(teachers)[choice]

        # Select a random opponent (not the same as chosen_teacher)
        opponents = [t for t in teachers if t != chosen_teacher]
        if not opponents:
            print("\nNo opponents available, adding more characters.")
            continue
        other_teacher = random.choice(opponents)

        # Display stats
        print(f"\nYou chose {chosen_teacher}. Your opponent is {other_teacher}.\n\nChoose your stat:")
        for index, stat in enumerate(teachers[chosen_teacher], start=1):
            print(f"{index}. {stat}")

        stat_choice = int(input("> ")) - 1
        stats_list = list(teachers[chosen_teacher].keys())
        if stat_choice < 0 or stat_choice >= len(stats_list):
            print("\nInvalid choice, try again.")
            continue
        chosen_stat = stats_list[stat_choice]

        # Compare the stat with the other teacher
        chosen_stat_value = teachers[chosen_teacher][chosen_stat]
        other_stat_value = teachers[other_teacher][chosen_stat]
        print(f"\n{chosen_teacher} has a {chosen_stat} stat of {chosen_stat_value}")
        print(f"{other_teacher} has a {chosen_stat} stat of {other_stat_value}")

        if chosen_stat_value > other_stat_value:
            print(f"\n************* {chosen_teacher} wins! *************")
        elif chosen_stat_value < other_stat_value:
            print(f"\n************* {other_teacher} wins! *************")
        else:
            print("\n************* It's a tie! *************")

        # Ask if they want to play again
        again = input("\nAgain? y/n > ").lower()
        if again != 'y':
            break
        clear()



if __name__ == "__main__":
    main()
