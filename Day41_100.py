print("🌟Website Rating🌟\n")

# Initialize the dictionary with keys and None values
website_info = {"Name": None, "URL": None, "Description": None, "Rating": None}

# Ask the user for input and split it into a list
user_input = input("Please enter the name of website, URL, description, and star rating out of 5, separated by commas: ").split(',')

# Check if the user has provided enough inputs
if len(user_input) != len(website_info):
    print("You have not provided enough information. Please try again.")
else:
    # Iterate over the keys in the dictionary and assign the corresponding user input
    for i, key in enumerate(website_info.keys()):
        website_info[key] = user_input[i].strip()

    # Print the content of the dictionary 
    print()
    print(', \n'.join(f'{k}: {v}' for k, v in website_info.items()))
