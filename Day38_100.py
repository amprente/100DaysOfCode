import random

print("~~~ Code the rainbow ~~~" + "\n")

def random_color():
    return "\033[38;2;{};{};{}m".format(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

def colorize_text(input_string):
    output_string = ">>> "
    for char in input_string:
        output_string += random_color() + char
    # Reset color at the end
    output_string += '\033[0m'
    return output_string

input_string = input("Enter a sentence: ")
print()
print(colorize_text(input_string))
