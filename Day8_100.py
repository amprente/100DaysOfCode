print("Welcome to your Daily Affirmation Generator!")

print()
name = input("What's your name? ")

print()
day = input("What day of the week is it (Monday, Tuesday, etc.)? ")

print()
favorite_color = input("What's your favorite color? ")
favorite_food = input("What's your favorite food? ")
favorite_animal = input("What's your favorite animal? ")

print()
affirmation = "Hey " + name + ", " 

if day == "Monday" or "monday" or "MONDAY":
  affirmation += "This week is a fresh start, just like a bright " + favorite_color + ". "
  affirmation += "You have the strength and resilience of your favorite animal, the " + favorite_animal + ", to overcome any challenges!"
elif day == "Tuesday" or "tuesday" or "TUESDAY": 
  affirmation += "Today, fuel your focus with the energy of your favorite food, the " + favorite_food + ". "
  affirmation += "Remember, even small steps lead to big accomplishments!"
elif day == "Wednesday" or "wednesday" or "WEDNSDAY": 
  affirmation += "You're halfway through the week! Celebrate your progress and keep shining brightly like your favorite color, " + favorite_color + "."
elif day == "Thursday" or "thursday" or "THURSDAY":  
  affirmation += "Almost there! Embrace the adventurous spirit of your favorite animal, the " + favorite_animal + ", and conquer the rest of the week!"
elif day == "Friday" or "friday" or "FRIDAY": 
  affirmation += "It's Friday! Time to reward yourself with your favorite food, the " + favorite_food + ". "
  affirmation += "Enjoy the weekend and recharge for next week's adventures!"
else:
  affirmation += "Have a fantastic weekend, " + name + "! Remember, you're awesome every day!"

print()
print(affirmation)
