import random
import os
import time

totalAttempts = 0

def game():
    attempts = 0
    number = random.randint(1, 100)  # Move the number generation outside of the while loop
    while True:
        guess = int(input("\nPick a number between 1 and 100: "))
        if guess > number:
            print("\nToo high")
            attempts += 1
        elif guess < number:
            print("\nToo low")
            attempts += 1
        else:
            print("\nJust right!")
            print(f"\n{attempts} attempts this round")
            return attempts

while True:
    menu = input("1: Guess the random number game\n2: Total Score\n3: Exit\n> ")
    if menu == '1':
        totalAttempts += game()
    elif menu == '2':
        print(f"\nYou've had {totalAttempts} attempts")
    elif menu == '3':
        break
    else:
        print("Invalid input")