'''1.Start the program with no image displayed. 2. If the user inputs a name that can't be found, a new label should appear in the image location saying 'Unable to find image'.'''

import tkinter as tk
from tkinter import simpledialog

def load_image(name):
    try:
        return tk.PhotoImage(file=f'Guess Who/{name.strip()}.jpg')  # Strip spaces from name
    except tk.TclError:
        return None

def update_images():
    names = simpledialog.askstring("Input", "Enter names separated by commas:")
    if names:
        name_list = names.split(',')  # Split the string into a list of names
        for name in name_list:
            photo = load_image(name)
            if photo:
                error_label.pack_forget()  # Hide error message
                label.config(image=photo, text='')  # Update the image
                label.image = photo  # Keep a reference
                label.pack(padx=20, pady=20)  # Repack the label with image
                break  # Stop after the first successful image load
        else:
            label.pack_forget()  # Hide the image label
            error_label.pack(padx=20, pady=20)  # Show error message
    else:
        label.pack_forget()  # No input given, hide the label
        error_label.pack(padx=20, pady=20)  # Show error message

# Set up the main window
root = tk.Tk()
root.title("Guess Who")

# Set up the label that will display the image or message
label = tk.Label(root)
error_label = tk.Label(root, text="Unable to find image")  # Error message label

# Button to prompt user input
button = tk.Button(root, text="Find", command=update_images)
button.pack(pady=20)

root.mainloop()
