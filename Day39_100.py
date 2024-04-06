import random

# List of words to choose from
word_list = ["hangman", "python", "programming", "gaming", "intelligence", "challenge", "learning", "amazing", "excellent", "superb", "outstanding", "incredible", "brilliant", "genius", "awesome", "wonderful", "fantastic",]

# Function to draw hangman
def draw_hangman(lives):
    stages = [
        """
           --------
           |      |
           |      O
           |     \|/
           |      |
           |     / \\
          ---
        """,
        """
           --------
           |      |
           |      O
           |     \|/
           |      |
           |     / 
          ---
        """,
        """
           --------
           |      |
           |      O
           |     \|/
           |      |
           |      
          ---
        """,
        """
           --------
           |      |
           |      O
           |     \|
           |      |
           |     
          ---
        """,
        """
           --------
           |      |
           |      O
           |      |
           |      |
           |     
          ---
        """,
        """
           --------
           |      |
           |      O
           |    
           |    
           |     
          ---
        """,
        """
           --------
           |      |
           |      
           |    
           |    
           |     
          ---
        """
    ]
    return stages[lives]

def hangman():
    word = random.choice(word_list).lower()
    guessed_letters = []
    guessed_word = ['_'] * len(word)
    incorrect_guesses = 0

    print("🌟 Hangman 🌟\n")

    while True:
        print(' '.join(guessed_word))

        guess = input("Choose a letter: ").lower()

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("Correct!")

            # Update guessed_word with correct guesses
            for i in range(len(word)):
                if word[i] == guess:
                    guessed_word[i] = guess
        else:
            print("Nope, not in there.")
            incorrect_guesses += 1
            print(draw_hangman(incorrect_guesses))
            print(f"{6 - incorrect_guesses} left.\n")

        if '_' not in guessed_word:
            print("You won with", 6 - incorrect_guesses, "lives left. The word was:", word)
            break

        if incorrect_guesses == 6:
            print("You lost! The word was:", word)
            break

hangman()
