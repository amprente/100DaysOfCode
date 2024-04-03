print("~~ Create a list of people's names ~~\n")

# Start with an empty list
names = []

def add_name(first_name, last_name):
    # Strip any extra spaces and capitalize the first letter of each name
    first_name = first_name.strip().capitalize()
    last_name = last_name.strip().capitalize()

    # Create a new string that combines the tidied up version of the first name and last name
    full_name = f"{first_name} {last_name}"
    print()

    # Do not allow duplicates
    if full_name not in names:
        names.append(full_name)

# Create a while True loop, including input for first and last name
while True:
    first_name = input("\nPlease enter the first name: ")
    last_name = input("Please enter the last name: ")
    

    add_name(first_name, last_name)

    # Each time you add a new name, print out the full list
    print(names)
