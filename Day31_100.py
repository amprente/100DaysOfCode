# Define the color-changing function
def color_text(text, color):
    colors = {"red": "\033[91m", "green": "\033[92m", "yellow": "\033[93m", "blue": "\033[94m", "purple": "\033[95m", "cyan": "\033[96m", "white": "\033[0m"}
    return f"{colors[color]}{text}{colors['white']}"

# Define the variables for Interface 1
title = "♫~~♫ Music Station ♫~~♫"
text = "Please select an option below:"
artist1 = "💿 Lady Gaga"
artist2 = "💿 Taylor Swift"
artist3 = "💿 Queen"
prev = "⇦Prev"
next = "Next⇨"
pause = "↭Pause↭"

# Print Interface 1
print(f"{color_text(title, 'purple')}\n\n{color_text(text, 'green')}\n\n{color_text(artist1, 'cyan')}\n{color_text(artist2, 'cyan')}\n{color_text(artist3, 'cyan')}")
print()
print(f"{color_text(prev, 'red').ljust(15)}{color_text(pause, 'blue').center(20)}{color_text(next, 'red').rjust(15)}")
print()

# Add empty space
for _ in range(4):
    print()

# Define the variables for Interface 2
title = "=◙= User Management System =◙="
username = "Username:"
password = "Password:"
login = "Log In"
register = "Register"
previous = "⇦Prev"
next = "Next⇨"

# Calculate the spacing needed for alignment
max_length = max(len(username), len(password), len(previous), len(next))
username_spacing = " " * (max_length - len(username))
password_spacing = " " * (max_length - len(password))
previous_spacing = " " * (max_length - len(previous))
next_spacing = " " * (max_length - len(next))

# Print Interface 2
print(f"{color_text(title, 'purple')}\n\n{color_text(username, 'yellow')}{username_spacing}:   [        ]\n{color_text(password, 'yellow')}{password_spacing}:   [        ]\n\n{color_text(previous, 'red')}{previous_spacing}         {color_text(login, 'green')}         {color_text(register, 'green')}         {color_text(next, 'red')}{next_spacing}")
print()
