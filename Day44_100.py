import random
import os

def clear_screen():
    # Clears the console
    if os.name == 'nt':  # for Windows
        os.system('cls')
    else:  # for macOS and Linux
        os.system('clear')

def generate_bingo_card():
    bingo_card = [[0 for _ in range(5)] for _ in range(5)]
    for i in range(5):
        numbers = random.sample(range(i*15+1, (i+1)*15+1), 5)
        numbers.sort()
        for j in range(5):
            bingo_card[j][i] = numbers[j]

    return bingo_card

def print_bingo_card(bingo_card):
    print('-'*30)
    for row in bingo_card:
        print('|', end='')
        for num in row:
            if isinstance(num, int):
                print(f' {num: <4}|', end='')
            else:
                print(f' {num[:4]: <4}|', end='')  # Ensure all entries fit in the space
        print('\n' + '-'*30)

def mark_number(bingo_card, number):
    marked = False
    for i, row in enumerate(bingo_card):
        for j, value in enumerate(row):
            if value == number:
                bingo_card[i][j] = 'X'
                marked = True
    return marked

def check_win(bingo_card):
    # Check all rows, columns and two diagonals
    size = len(bingo_card)
    for row in bingo_card:
        if all(x == 'X' for x in row):
            return True
    for col in range(size):
        if all(row[col] == 'X' for row in bingo_card):
            return True
    if all(bingo_card[i][i] == 'X' for i in range(size)):
        return True
    if all(bingo_card[i][size-i-1] == 'X' for i in range(size)):
        return True
    return False

def main():
    bingo_card = generate_bingo_card()
    print("=== Bingo Card Generator ===\n")
    print_bingo_card(bingo_card)

    while True:
        try:
            number_called = int(input("\nEnter the next number (1-75): "))
            if not 1 <= number_called <= 75:
                print("\nPlease enter a number between 1 and 75.")
                continue
        except ValueError:
            print("Please enter a valid integer.")
            continue

        if mark_number(bingo_card, number_called):
            clear_screen()  # Clear the screen
            print("Number marked!\n")
            print_bingo_card(bingo_card)
            if check_win(bingo_card):
                print("\n🎉 Congratulations! You've won Bingo! √🎉")
                break
        else:
            print("\nNumber not on your card.")

if __name__ == "__main__":
    main()
