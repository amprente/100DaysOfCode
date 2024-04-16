# Read the high.score file
with open('high.score', 'r') as file:
    lines = file.readlines()

# Initialize variables to track the highest score
max_score = -1
max_score_name = ""

# Process each line in the file
for line in lines:
    name, score = line.strip().split()
    score = int(score.replace(',', ''))  # Remove commas and convert score to an integer
    if score > max_score:
        max_score = score
        max_score_name = name

# Output the result
print("🌟Current Leader🌟\n")
print("Analyzing high scores......\n")
print(f"Current leader is {max_score_name} {max_score:,}")
