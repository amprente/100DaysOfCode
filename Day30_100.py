print("~ Thought of each of the 30 days of challenges ~")
print()

num_days = 30

printed_heading = False  # Flag to track if heading is printed

for day in range(1, num_days + 1):
  if not printed_heading:
    print(f"\n{num_days} Days Down")
    printed_heading = True  # Set flag to avoid repeating heading
  print(f"\nDay {day}:")
  thought = input("What did you think of Day " + str(day) + "?: ")

  # Center align response (adjust spaces as needed)
  response = f" You thought Day {day} was {thought}."
  spaces_before = (len(f"{num_days} Days Down") - len(response)) // 2
  print(f"{' ' * spaces_before}{response}")
