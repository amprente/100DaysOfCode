'''pull in data for 10 users using randomuser.me.

The program should:

Save the medium quality version of the profile pic as a local file named {firstName} {lastName}.jpg.
Each picture should be saved to a different file.'''



import requests
import os

# Define the URL for the randomuser API with parameters for 10 users
url = "https://randomuser.me/api/?results=10"

# Make a request to the API
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()

    # Loop through each user in the results
    for user in data["results"]:
        first_name = user["name"]["first"]
        last_name = user["name"]["last"]
        picture_url = user["picture"]["medium"]

        # Define the file name
        file_name = f"{first_name}_{last_name}.jpg"

        # Get the image content
        img_response = requests.get(picture_url)

        # Check if the image request was successful
        if img_response.status_code == 200:
            # Save the image to a local file
            with open(file_name, 'wb') as file:
                file.write(img_response.content)

            print(f"Saved {file_name}")
        else:
            print(f"Failed to download image for {first_name} {last_name}")
else:
    print("Failed to retrieve data from randomuser.me API")

# Ensure that the files are saved in the current directory
os.listdir()
