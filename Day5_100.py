print("Which character are you?")

print()
is_brave = input("Are you brave? (yes/no): ")
has_magic = input("Do you have magical powers? (yes/no): ")

print()
if is_brave == "yes" and has_magic == "yes":
    print("Wow! You must be a powerful mage!")
else:
    if is_brave == "yes":
        is_tech_savvy = input("Are you good with technology? (yes/no): ")
        if is_tech_savvy == "yes":
            print("Looks like you're a brilliant inventor with a courageous spirit!")
        else:
            print("You seem brave! Perhaps a future hero?")
    else:  
        print("Hmm, interesting! You might be a unique character yet to be discovered!")

print()
print("Thanks for playing!")
