import random


print("=== Bingo Card Generator ===\n")

def generate_bingo_card():
    # Create an empty 2D list
    bingo_card = [[0 for _ in range(5)] for _ in range(5)]

    # Generate numbers for each column
    for i in range(5):
        numbers = random.sample(range(i*15+1, (i+1)*15+1), 5)
        numbers.sort()
        for j in range(5):
            bingo_card[j][i] = numbers[j]

    # Replace the center with 'BINGO!'
    bingo_card[2][2] = 'BINGO!'

    return bingo_card

def print_bingo_card(bingo_card):
    print('-'*30)
    for row in bingo_card:
        print('|', end='')
        for num in row:
            print(f' {num: <4}|', end='')
        print('\n' + '-'*30)

bingo_card = generate_bingo_card()
print_bingo_card(bingo_card)
