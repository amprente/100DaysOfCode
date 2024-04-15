# This script manages a high score table by appending new scores to 'high.score' file.

def main():
    with open('high.score', 'a') as file:  # Open the file in append mode
        while True:
            # Get user input for initials and score in one line and split them
            data = input("🌟HIGH SCORE TABLE🌟\n\nPlease enter both initials and score separated by a space: >").split()
            if len(data) < 2:  # Ensure both initials and score were entered         
                continue

            initials, score = data[0], data[1]
            # Write the initials and score to the file with a new line
            file.write(f"{initials} {score}\n")
            print("Added to high score table.\n")

            # Check if the user wants to add another score
            if input("\nAdd another? y/n? ") != 'y':
                break  # Exit the loop if the user does not want to continue

if __name__ == "__main__":
    main()
