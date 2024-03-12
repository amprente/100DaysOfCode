print("Welcome to the Tip Calculator!")

print()
my_bill = float(input("What was the total bill?: "))
tip_percentage = float(input("What percentage tip would you like to leave? (e.g., 15, 18, 20): "))

# Calculate tip amount
tip_rate = tip_percentage / 100
tip_amount = my_bill * tip_rate

# Calculate total bill including tip
total_bill = my_bill + tip_amount

# Get number of people splitting the bill
number_of_people = int(input("How many people are splitting the bill?: "))

# Calculate amount per person
amount_per_person = total_bill / number_of_people

# Display results
print()
print("The total bill with a", tip_percentage, "% tip is $", total_bill, ".")
print("Each person owes $", round(amount_per_person), ".")

