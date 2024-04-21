'''Create a backup folder.
Create a random filename.
Save a copy of the data to that file.
This should all happen before the auto save.'''

import os
import random
import string

def create_backup(data):
    backup_folder = 'backup_folder'
    file_exists = False

    # Check if backup folder exists, if not, create it
    if not os.path.exists(backup_folder):
        os.mkdir(backup_folder)
        print("Backup folder created.\n")

    # Generate a random filename
    filename = ''.join(random.choices(string.ascii_letters + string.digits, k=10)) + '.txt'
    file_path = os.path.join(backup_folder, filename)

    # Check if file already exists
    if not os.path.exists(file_path):
        # Save data to the file
        with open(file_path, 'w') as file:
            file.write(data)
            file_exists = True
            print(f"Data saved to {filename}")    
    

    if file_exists:
        print("\nBackup was created before auto-saving.")
    else:
        print("\nBackup file already exists.")

# Example usage:
create_backup("\nYour data here that needs to be backed up.")
