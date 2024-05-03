'''I've provided you with a folder called "Guess Who" containing images of 4 people.

Your program should:

Prompt the user to input a name.
If the user inputs 'Charlotte', 'Gerald', 'Kate' or 'Mo', then their image should load.
Otherwise an 'image not found' message should display.'''




import tkinter as tk
from tkinter import simpledialog, messagebox

def load_image(name):
    try:
        # Try to create a PhotoImage object from the file
        return tk.PhotoImage(file=f'Guess Who/{name}.jpg')
    except tk.TclError:
        # If the file is not found or not a valid image, return None
        return None

def update_image():
    name = simpledialog.askstring("Input", "Enter the name:")
    photo = load_image(name)
    if photo:
        label.config(image=photo, text='')  # Clear any previous text and update the image
        label.image = photo  # Keep a reference!
    else:
        label.config(image='', text="Image not found")  # Clear any previous image and show message

# Set up the main window
root = tk.Tk()
root.title("Guess Who")

# Set up the label that will display the image or message
label = tk.Label(root, text="Enter a name to display the image.")
label.pack(padx=20, pady=20)

# Button to prompt user input
button = tk.Button(root, text="Find", command=update_image)
button.pack(pady=20)

root.mainloop()
