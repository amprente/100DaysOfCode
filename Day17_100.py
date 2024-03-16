# Initialize scores
player_1_score = 0
player_2_score = 0

# Start the game
while True:
    print("~ Let's play Rock, Paper, Scissors! ~")

    # Get player 1's choice
    print()
    player_1_choice = input("Player 1, choose (R)ock, (P)aper, or (S)cissors or Exit: ")

    # Check if player 1 wants to exit the game
    if player_1_choice == "Exit":
        print("Player 1 has chosen to exit the game.")
        break

    # Get player 2's choice
    print()
    player_2_choice = input("Player 2, choose (R)ock, (P)aper, or (S)cissors or Exit: ")

    # Check if player 2 wants to exit the game
    if player_2_choice == "Exit":
        print("Player 2 has chosen to exit the game.")
        break

    # Determine the winner
    print()
    if player_1_choice == player_2_choice:
        print("It's a tie! ")
        continue
    elif player_1_choice == "R" and player_2_choice == "S":
        print("Rock crushes scissors! Player 1 wins!")
        print()
        player_1_score += 1
    elif player_1_choice == "P" and player_2_choice == "R":
        print("Paper covers rock! Player 1 wins!")
        print()
        player_1_score += 1
    elif player_1_choice == "S" and player_2_choice == "P":
        print("Scissors cut paper! Player 1 wins!")
        print()
        player_1_score += 1
    else:
        # Player 2 wins
        if player_2_choice == "R" and player_1_choice == "S":
            print("Rock crushes scissors! Player 2 wins!")
            print()
            player_2_score += 1
        elif player_2_choice == "P" and player_1_choice == "R":
            print("Paper covers rock! Player 2 wins!")
            print()
            player_2_score += 1
        elif player_2_choice == "S" and player_1_choice == "P":
            print("Scissors cut paper! Player 2 wins!")
            print()
            player_2_score += 1

    # Handle invalid choices (optional)
    print()
    if player_1_choice not in ("R", "P", "S", "Exit") or player_2_choice not in ("R", "P", "S", "Exit"):
        print("Invalid choice. Please enter 'R', 'P', or 'S' next time.")
        continue

    # Check if a player has won 3 rounds
    if player_1_score == 3:
        print("Player 1 has won the game!")
        break
    elif player_2_score == 3:
        print("Player 2 has won the game!")
        break

# Print final scores
print("Final scores:")
print("Player 1: ", player_1_score)
print("Player 2: ", player_2_score)
