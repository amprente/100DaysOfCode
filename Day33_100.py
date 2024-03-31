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
    action = input(f"{Fore.CYAN}Do you want to view, add, or edit your to-do list?: {Style.RESET_ALL}").lower()

    if action == "view":
        view_list()
    elif action == "add":
        item = input(f"{Fore.CYAN}What do you want to add to your to-do list?: {Style.RESET_ALL}")
        todo_list.append(item)
        print(f"{Fore.GREEN}✅ Added '{item}' to your to-do list.\n{Style.RESET_ALL}")
    elif action == "edit":
        view_list()
        item_number = int(input(f"{Fore.CYAN}Which item number did you complete?: {Style.RESET_ALL}")) - 1
        if 0 <= item_number < len(todo_list):
            completed_item = todo_list.pop(item_number)
            print(f"{Fore.GREEN}✅ Removed '{completed_item}' from your to-do list.\n{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}❌ Invalid item number.\n{Style.RESET_ALL}")

    # Pause and clear the console
    time.sleep(3)
    os.system('cls' if os.name == 'nt' else 'clear')
