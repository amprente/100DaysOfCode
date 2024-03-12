print("Welcome to the Fake Fan Quiz!")

print()
topic = input("What are you a big fan of? (e.g., Movie, Band, Book): ")

print()
if topic == "Movie":
  favorite_movie = input("What's your all-time favorite movie from that franchise? ")
  if favorite_movie == "Star Wars: Episode V - The Empire Strikes Back":
    print("Great choice! But who is Luke's real father?")  
  else:
    print("Hmm, interesting choice. But have you seen every single movie in the series?")

elif topic == "Band":
  favorite_band = input("Who is your favorite member of the band? ")
  if len(favorite_band) > 2:
    print("Cool! " + favorite_band.title() + " is awesome. Can you name their debut album?")
  else:
    print("The band has some great members! Can you tell me all their names?")

elif topic == "Book":
  favorite_quote = input("What's your favorite quote from the book? ")
  if "..." in favorite_quote:  
    print("Wow, that's a deep quote! What's the significance behind it?")  
  else:
    print(favorite_quote.title() + " is a great read! Have you read the entire series?")


else:
  print("Interesting taste! I don't have specific questions for " + topic + " yet. Let me know if you'd like to add some!")

print()
print("Thanks for playing the Fake Fan Quiz!")
