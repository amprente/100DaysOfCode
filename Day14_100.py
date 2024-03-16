print("~ Welcome to Rock, Paper, Scissors! ~")

# Get player 1's choice
print()
player_1_choice = input("Player 1, choose (R)ock, (P)aper, or (S)cissors: ").upper()

# Get player 2's choice
print()
player_2_choice = input("Player 2, choose (R)ock, (P)aper, or (S)cissors: ").upper()

# Determine the winner
print()
if player_1_choice == player_2_choice:
    print("It's a tie! ")
elif player_1_choice == "R" and player_2_choice == "S":
    print("Rock crushes scissors! Player 1 wins!🪨✂️")
elif player_1_choice == "P" and player_2_choice == "R":
    print("Paper covers rock! Player 1 wins!🪨")
elif player_1_choice == "S" and player_2_choice == "P":
    print("Scissors cut paper! Player 1 wins!✂️️")
else:
    # Player 2 wins
    if player_2_choice == "R" and player_1_choice == "S":
        print("Rock crushes scissors! Player 2 wins!🪨✂️")
    elif player_2_choice == "P" and player_1_choice == "R":
        print("Paper covers rock! Player 2 wins!🪨")
    elif player_2_choice == "S" and player_1_choice == "P":
        print("Scissors cut paper! Player 2 wins!✂️️")

# Handle invalid choices (optional)
print()
if player_1_choice not in ("R", "P", "S") or player_2_choice not in ("R", "P", "S"):
    print("Invalid choice. Please enter 'R', 'P', or 'S' next time.")
