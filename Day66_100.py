import tkinter as tk

def add_digit(digit):
    global current_input
    current_input += str(digit)
    display_var.set(current_input)

def add_operator(operator):
    global current_input, last_number, operation
    last_number = float(current_input) if '.' in current_input else int(current_input)
    operation = operator
    current_input = ""
    display_var.set(operation)

def calculate():
    global current_input, last_number, operation
    second_number = float(current_input) if '.' in current_input else int(current_input)
    if operation == "+":
        result = last_number + second_number
    elif operation == "-":
        result = last_number - second_number
    elif operation == "*":
        result = last_number * second_number
    elif operation == "/":
        if second_number == 0:
            result = "Error"
        else:
            result = last_number / second_number
    display_var.set(result)
    current_input = str(result)

def clear():
    global current_input, last_number, operation
    current_input = ""
    last_number = 0
    operation = ""
    display_var.set("0")

# Main Window
root = tk.Tk()
root.title("Calculator")

# Variables
current_input = ""
last_number = 0
operation = ""
display_var = tk.StringVar()

# Display Label
display_label = tk.Label(root, textvariable=display_var, height=2, width=10, font=("Arial", 24))
display_label.grid(row=0, column=0, columnspan=4)
display_var.set('0')

# Buttons
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3)
]

for (text, row, col) in buttons:
    button = tk.Button(root, text=text, width=5, height=2, font=("Arial", 14),
                       command=lambda text=text: add_digit(text) if text.isdigit() else add_operator(text) if text in '+-*/' else calculate() if text == '=' else clear())
    button.grid(row=row, column=col)

# Main loop
root.mainloop()
