print("How many seconds are in a year?")

# Define the number of seconds in a minute, minutes in an hour, hours in a day, and days in a year
seconds_in_minute = 60
minutes_in_hour = 60
hours_in_day = 24
days_in_year = 365
days_in_leap_year = 366

# Calculate the number of seconds in a year
seconds_in_year = seconds_in_minute * minutes_in_hour * hours_in_day * days_in_year

# Calculate the number of seconds in a leap year
seconds_in_leap_year = seconds_in_minute * minutes_in_hour * hours_in_day * days_in_leap_year

# Print the results
print()
print()
print("The number of seconds in a year is:", seconds_in_year)
print()
print("The number of seconds in a leap year is:", seconds_in_leap_year)
