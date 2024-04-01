import random
import time
import os

# List of email addresses
email_list = ["john@test.com", "mary@example.com", "david@email.com", "sarah@test.org", "james@example.org", "linda@email.com", "michael@example.com", "emma@test.org", "chris@email.com", "jennifer@example.org"]


def send_silly_email(address, message):
    print(f"Sending email to {address}:")
    print(message)
    #print("Email sent successfully (maybe)! \n")  # Add a touch of whimsy


def create_silly_message(address):
    """Creates a silly message using the recipient's name"""
    name = address.split('@')[0]  # Get username from email
    nouns = ["sock", "potato", "and very important potato", "and a flock of pigeons wearing tiny hats", "and unicycle made entirely of cheese",]
    verbs = ["juggles", "sings opera", "teaches ballet", "writes a song about", "writes a poem about", "writes a letter"]
    adjective = random.choice(["purple", "wrinkled", "operatic, but not as bad as", "smelly", "slimy", "slippery"])

    noun = random.choice(nouns)
    verb = random.choice(verbs)

    message = f"\nDear {name},\nI just saw someone {verb} with a {adjective} {noun}.\nIsn't that something?\n\n\nYour friend,\nThe Silly Mailer\n"
    return message


def main():
    while True:
        print("1. Add an email address")
        print("2. View all email addresses")
        print("3. Send silly email to an address")
        print("4. Get SPAMMING!") 
        print("5. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            email = input("\nEnter the email address: ")
            email_list.append(email)
            print("Email address added successfully!\n")
        elif choice == '2':
            print("\nList of email addresses:")
            for email in email_list:
                print(email)
            print()
        elif choice == '3':
            email = input("\nEnter the email address to send the silly email: ")
            if email in email_list:
                silly_message = create_silly_message(email)
                send_silly_email(email, silly_message)
            else:
                print("Email address not found!\n")
        elif choice == '4':
            print("Getting SILLY!\n")
            for address in email_list[:10]:  # Send silly emails to first 10 addresses
                os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen
                silly_message = create_silly_message(address)
                send_silly_email(address, silly_message)
                time.sleep(3)  # Pause for 3 seconds before sending the next email
        elif choice == '5':
            print("Quitting...")
            break
        else:
            print("Invalid choice. Please try again.\n")


if __name__ == "__main__":
    main()
