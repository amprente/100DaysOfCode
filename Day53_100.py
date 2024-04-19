import os
import time

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main_menu():
    while True:
        clear_screen()
        print("\n🌟RPG Inventory🌟")
        print("\n1: Add  2: Remove  3: View  4: Exit")
        choice = input("\nChoose an option: ")
        if choice == '1':
            add_item()
        elif choice == '2':
            remove_item()
        elif choice == '3':
            view_items()
        elif choice == '4':
            print("\nExiting the program.")
            break
        else:
            print("\nInvalid option, please try again.")

def add_item():
    item = input("\nInput the item to add: ").capitalize()
    try:
        with open("inventory.txt", "a") as file:
            file.write(item + "\n")
        print(f"\n{item} has been added to your inventory.")
        time.sleep(2)  # Pause for 2 seconds to let the user read the message
    except Exception as e:
        print("\nAn error occurred while adding the item:", e)
    finally:
        clear_screen()  # Clears the screen after adding an item

def remove_item():
    item = input("\nInput the item to remove: ").capitalize()
    try:
        with open("inventory.txt", "r") as file:
            items = file.readlines()
        with open("inventory.txt", "w") as file:
            removed = False
            for i in items:
                if i.strip() != item or removed:
                    file.write(i)
                else:
                    removed = True
            if removed:
                print(f"\n{item} has been removed from your inventory.")
                time.sleep(2)  # Pause to let the user read the message
            else:
                print(f"\n{item} was not found in the inventory.")
                time.sleep(2)  # Pause to let the user read the message
    except Exception as e:
        print("\nAn error occurred while removing the item:", e)
    finally:
        clear_screen()  # Clears the screen after removing an item

def view_items():
    item = input("\nInput the item to view: ").capitalize()
    try:
        with open("inventory.txt", "r") as file:
            items = [line.strip() for line in file if line.strip()]
        count = items.count(item)
        if count > 0:
            print(f"\nYou have {count} {item}(s)")
        else:
            print(f"\nNo {item} found in inventory.")
        input("\nPress Enter to continue...")  # Waits for user input before clearing the screen
    except Exception as e:
        print("\nAn error occurred while viewing the inventory:", e)

if __name__ == "__main__":
    main_menu()
