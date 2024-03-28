def print_in_color(word, color):
  if color == "red":
      print("\033[31m", word, sep="", end="")
  elif color == "green":
      print("\033[32m", word, sep="", end="")
  elif color == "yellow":
      print("\033[33m", word, sep="", end="")
  elif color == "blue":
      print("\033[34m", word, sep="", end="")
  elif color == "purple":
      print("\033[35m", word, sep="", end="")
  elif color == "cyan":
      print("\033[36m", word, sep="", end="")
  elif color == "white":
      print("\033[37m", word, sep="", end="")
  else:
      # Default color
      print(word, end="")
  # Reset color to default after printing
  print("\033[0m", end="")

# Title and regular text
print("~ Super Subroutine ~")
print()
print("\033[4m", "Now, I can have some rainbows in my text.", "\033[0m")

# Text in different colors
print_in_color(" Super", "red")
print_in_color(" Subroutine ", "green")
print_in_color("with", "yellow")
print_in_color(" my", "blue")
print_in_color(" Super", "purple")
print_in_color(" Subroutine", "cyan")
