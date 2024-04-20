import csv

def calculate_total_revenue(csv_file_path='Day54Totals.csv'):
    total_revenue = 0.0
    with open(csv_file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            cost = float(row['Cost'])  
            quantity = int(row['Quantity'])  
            total_revenue += cost * quantity
    print(f"🌟Shop $$ Tracker🌟\n\nYour shop took £{total_revenue:.2f} pounds today.")

# Call the function to calculate and print the total revenue
calculate_total_revenue()