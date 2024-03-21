# Initial loan amount
loan_amount = 1000

# Annual interest rate
interest_rate = 0.05

# Number of years
years = 10

# Calculate the total amount owed after 10 years
for i in range(years):
    loan_amount += loan_amount * interest_rate

print("The total amount owed after 10 years is: $" + str(round(loan_amount, 2)))
