print("🌟Star Wars Name Generator🌟\n")
user_input = input("Input your first name, last name, mother's maiden name, and the city where you were born, separated by spaces: > ")
first_name, last_name, maiden_name, city = user_input.split()

# Generate Star Wars first name
sw_first_name = (first_name[:3] + last_name[:3]).title()

# Generate Star Wars last name
sw_last_name = (maiden_name[:2] + city[-3:]).title()

print(f"\nYour Star Wars name is: {sw_first_name} {sw_last_name}")
