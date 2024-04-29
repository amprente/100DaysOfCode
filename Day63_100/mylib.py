import random

def dice_roll():
    """Simulates rolling a dice and returns a number between 1 and 6."""
    return random.randint(1, 6)

def pretty_print(data):
    """Pretty prints a dictionary with key-value pairs."""
    for key, value in data.items():
        print(f"{key}: {value}")

def insult_generator():
    """Generates a random insult."""
    insults = ["You code like I type... with my elbows.👾", "Your coding is so slow, it might have a 28.8 kbps modem.", "You're as useful as comments in minified JavaScript."]
    return random.choice(insults)
