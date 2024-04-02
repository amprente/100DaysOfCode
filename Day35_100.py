# a simple TO-Do list

import os
import time
from colorama import Fore, Style, init

# Initialize colorama
init()

# Initialize the to-do list
todo_list = []

# Define a subroutine to print the to-do list
def view_list():
    print("\n📝 To-Do List:")
    for i, item in enumerate(todo_list):
        print(f"{Fore.GREEN}{i+1}. {item}{Style.RESET_ALL}")
    print()

# Main loop
while True:
    print(f"\n{Fore.YELLOW}📋=== To-Do List Manager ===📋{Style.RESET_ALL}\n")
    print(f"\n{Fore.CYAN}Do you want to: \n1 - view, \n2 - add, \n3 - remove one by one, \n4 - edit your to-do list, \n5 - erase the entire list.{Style.RESET_ALL}")

    action = input("> ")

    if action == "1" or action.lower() == "view":
        view_list()
        input("Press Enter to continue...")
    elif action == "2" or action.lower() == "add":
        item = input(f"{Fore.CYAN}What do you want to add to your to-do list?: {Style.RESET_ALL}")
        if item in todo_list:
            print(f"{Fore.RED}❌ '{item}' already exists in your to-do list.{Style.RESET_ALL}")
        else:
            todo_list.append(item)
            print(f"{Fore.GREEN}✅ Added '{item}' to your to-do list.{Style.RESET_ALL}")
    elif action == "3" or action.lower() == "remove":
        if len(todo_list) == 0:
            print(f"{Fore.RED}❌ Your to-do list is empty.{Style.RESET_ALL}")
        else:
            view_list()
            try:
                item_number = int(input(f"{Fore.CYAN}Which item number do you want to remove?: "))
                if 1 <= item_number <= len(todo_list):
                    item_to_remove = todo_list[item_number - 1]
                    confirm = input(f"{Fore.YELLOW}Are you sure you want to remove '{item_to_remove}'? (yes/no): {Style.RESET_ALL}").lower()
                    print()  # Add an empty line
                    if confirm == "yes":
                        removed_item = todo_list.pop(item_number - 1)
                        print(f"{Fore.GREEN}✅ Removed '{removed_item}' from your to-do list.{Style.RESET_ALL}")
                        time.sleep(3)  # Pause to allow user to see the options
                    else:
                        print(f"{Fore.YELLOW}⚠️ Removal canceled.{Style.RESET_ALL}")
                else:
                    print(f"{Fore.RED}❌ Invalid item number.{Style.RESET_ALL}")
            except ValueError:
                print(f"{Fore.RED}❌ Please enter a valid item number.{Style.RESET_ALL}")
    elif action == "4" or action.lower() == "edit":
        view_list()
        try:
            item_number = int(input(f"{Fore.CYAN}Which item number do you want to edit?: "))
            if 1 <= item_number <= len(todo_list):
                new_item = input(f"{Fore.CYAN}Enter the new text for item {item_number}: {Style.RESET_ALL}")
                todo_list[item_number - 1] = new_item
                print(f"{Fore.GREEN}✅ Item {item_number} updated to '{new_item}'.{Style.RESET_ALL}")
            else:
                print(f"{Fore.RED}❌ Invalid item number.{Style.RESET_ALL}")
        except ValueError:
            print(f"{Fore.RED}❌ Please enter a valid item number.{Style.RESET_ALL}")
    elif action == "5" or action.lower() == "erase":
        confirm_erase = input(f"{Fore.YELLOW}Are you sure you want to erase the entire to-do list? \nThis action cannot be undone. (yes/no): ")
        print()  # Add an empty line
        if confirm_erase == "yes":
            todo_list.clear()
            print(f"{Fore.GREEN}✅ Your entire to-do list has been erased.{Style.RESET_ALL}")
        else:
            print(f"{Fore.YELLOW}⚠️ Erase operation canceled.{Style.RESET_ALL}")

    # Clear the console
    os.system('cls' if os.name == 'nt' else 'clear')
