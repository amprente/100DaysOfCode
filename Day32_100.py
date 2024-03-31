import random

# List of greetings in different languages
greetings = [
    "Salut", #Romanian
    "Hello",  # English
    "Bonjour",  # French
    "Hola",  # Spanish
    "Ciao",  # Italian
    "Hallo",  # German
    "Konnichiwa",  # Japanese
    "Namaste",  # Hindi
    "Salam",  # Arabic
    "Nǐ hǎo",  # Mandarin Chinese
    "Olá",  # Portuguese
    "Guten Tag",  # German
    "Shalom",  # Hebrew
    "こんにちは",  # Japanese
    "안녕하세요",  # Korean
    "你好",  # Chinese       
]

# Generate a random index to select a greeting
random_index = random.randint(0, len(greetings) - 1)

# Print a random greeting
print(f"Random greeting: {greetings[random_index]}")
