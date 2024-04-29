'''You're going to curate your own library with these subroutines.

Go back through your programs and choose some subroutines that you've used a lot. Perhaps it was your dice roller. Could be your prettyPrint. Maybe it was your 'generate random baldy insult' subroutine. Whatever. Find them.
Create a new file that contains all your best subroutines.
Import this file into your main.py and call a few to show that it works.'''


from mylib import dice_roll, pretty_print, insult_generator

# Testing dice_roll
print("Dice Roll:", dice_roll())

# Testing pretty_print
test_data = {"\nName": "Cody", "Occupation": "Coding Ninja", "Language": "Python"}
print("\nPretty Print:")
pretty_print(test_data)

# Testing insult_generator
print("\nRandom Insult:", insult_generator())
