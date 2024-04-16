import random

def menu():
    while True:
        choice = input("🌟Idea Storage🌟\n\nAdd an idea or see a random idea? a/r: ").strip().lower()
        if choice == 'a':
            add_idea()
        elif choice == 'r':
            show_random_idea()
        else:
            print("Please enter 'a' to add an idea or 'r' to see a random idea.\n")

def add_idea():
    idea = input("\nInput your idea: ")
    with open('my.ideas', 'a') as file:
        file.write(idea + '\n')
    print("Nice! Your idea has been stored.\n")

def show_random_idea():
    try:
        with open('my.ideas', 'r') as file:
            ideas = file.readlines()
        if ideas:
            print(random.choice(ideas).strip().capitalize())
        else:
            print("\nNo ideas stored yet.")
    except FileNotFoundError:
        print("\nNo ideas stored yet.")

if __name__ == "__main__":
    menu()
