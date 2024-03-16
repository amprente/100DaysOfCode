print("~ Grade Generator ~")
print()

# Ask user for test name, max score, and score received
test_name = input("Enter the name of the test: ")
max_score = input("Enter the maximum score for the test: ")
score = input("Enter the score you received: ")

# Convert the scores to integers
max_score = int(max_score)
score = int(score)

# Calculate percentage
percentage = round((score / max_score) * 100, 2)

# Determine grade using if/elif statements
if percentage >= 90:
    grade = 'A+'
elif percentage >= 80:
    grade = 'A'
elif percentage >= 70:
    grade = 'B'
elif percentage >= 60:
    grade = 'C'
elif percentage >= 50:
    grade = 'D'
else:
    grade = 'U'

# Print out grade and percentage
print()
print("For the " + test_name + " test:")
print("You scored " + str(score) + " out of " + str(max_score) + ".")
print("This is a percentage of " + str(percentage) + "%.")
print("Your grade is: " + grade)


if grade == 'A+' or grade == 'A':
    print("🎉 Congratulations on your excellent grade!🎉")
elif grade == 'B':
    print("Good job!👍")
elif grade == 'C':
    print("You passed!😊")
else:
    print("Better luck next time.😢")
    
