print("Welcome to the Generation Generator!")

birth_year = int(input("What year were you born? "))

if birth_year >= 1925 and birth_year <= 1946:
  print("You are a Silent Generation citizen . Respect your elders! 😁 ")
elif birth_year >= 1947 and birth_year <= 1964:
  print("Woah! You're a Baby Boomer ☮️. The world needed your optimism! 😊")
elif birth_year >= 1965 and birth_year <= 1981:
  print("Greetings, Generation X member . You're independent and resourceful! 😎 ")
elif birth_year >= 1982 and birth_year <= 1995:
  print("Welcome, Millennial ! You're the tech-savvy generation.😀")
elif birth_year >= 1996 and birth_year <= 2015:
  print("Yo, Generation Z ! You're the digital natives. 💻")
else:
  print("Seems you're either too young or a time traveler! 😄 ")
