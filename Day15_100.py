print("Welcome to the Animal Sound Machine!")
print()
exit = "no"  # Set initial value to 'no' to start the loop

while exit == "no":

    animal_sound = input("What animal sound do you want to hear?: ")
    print()
    # Check for different animal sounds using multiple if statements
    if animal_sound == "cow":
        print(" Moo")
    elif animal_sound == "pig":
        print(" Oink")
    elif animal_sound == "sheep":
        print(" Baaa")
    elif animal_sound == "duck":
        print(" Quack, Quack")
    elif animal_sound == "dog":
        print(" Woof, Woof")
    elif animal_sound == "cat" or animal_sound == "kitten":
        print(" Meow")  
    elif animal_sound == "horse":
        print(" Neigh")
    elif animal_sound == "chicken":
        print(" Cluck, Cluck")
    elif animal_sound == "goat":
        print(" Baa")
    elif animal_sound == "lion":
        print(" Roar")
    elif animal_sound == "elephant":
        print(" Trumpet")
    elif animal_sound == "bear":
        print(" Growl")
    elif animal_sound == "frog":
        print(" Ribbit")
    elif animal_sound == "bird":
        print(" Chirp, Chirp")
    elif animal_sound == "snake":
        print(" Hiss, Hiss")    
    elif animal_sound == "A Lesser Spotted lemur":
        print("Ummm...the Lesser Spotter Lemur goes awooga.")
    else:
        print("Ummm... I don't know that animal sound, but it probably goes...")
        print("Awooga")
    
    # Ask if the user wants to exit
    print()
    exit = input("Do you want to exit? (yes/no) ")
    print()
print("Thanks for playing!")
