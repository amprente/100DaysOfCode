print("🍕 Pizza Shop 🍕")
print("----------------\n")


def get_integer_input(prompt):
    """ Prompt user for an integer input and handle non-integer errors. """
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("You must input a numerical character, try again.")

def calculate_price(quantity, size):
    """ Calculate the total cost based on the quantity and size of pizzas. """
    size_prices = {'S': 10, 'M': 15, 'L': 20}
    price_per_pizza = size_prices.get(size.upper(), 10)  # Default to small if undefined size
    return quantity * price_per_pizza

def add_order(orders):
    """ Adds a new order to the list after taking inputs from the user. """
    quantity = get_integer_input("\nHow many pizzas?: > ")
    size = input("\nWhat size? (S, M, L) > ")
    name = input("\nName please: > ")
    cost = calculate_price(quantity, size)
    orders.append([name, quantity, size, cost])
    print(f"\nThanks {name}, your pizzas will cost ${cost}")
    save_orders(orders)

def view_orders(orders):
    """ Display all orders from the list. """
    for order in orders:
        name, quantity, size, cost = order
        print(f"\n{name} ordered {quantity} size {size} pizzas for ${cost}")

def load_orders():
    """ Load orders from a file. """
    try:
        with open("orders.txt", "r") as file:
            orders = [line.strip().split(',') for line in file]
            return [[parts[0], int(parts[1]), parts[2], int(parts[3])] for parts in orders]
    except FileNotFoundError:
        return []

def save_orders(orders):
    """ Save all orders to a file. """
    with open("orders.txt", "w") as file:
        for order in orders:
            file.write(','.join(map(str, order)) + '\n')

def main():
    orders = load_orders()
    while True:
        choice = input("\nChoose an option: Add (A), View (V), Exit (E) > ").upper()
        if choice == 'A':
            add_order(orders)
        elif choice == 'V':
            view_orders(orders)
        elif choice == 'E':
            print("\nExiting program.")
            break
        else:
            print("Invalid choice, please choose again.")

if __name__ == '__main__':
    main()
