print("~ List of Numbers Generator ~")
print()

# Ask the user for the starting number, ending number, and increment
start = int(input("Start at: "))
end = int(input("End before: "))
increment = int(input("Increment between values: "))
print()

# Use a for loop with the range function to generate and print the list
for i in range(start, end, increment):
    print(i)
