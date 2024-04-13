import os
import time

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def add_todo(todos):
    task = input("What is the task:? > ")
    due_by = input("When is it due by:? > ")
    priority = input("What is the priority (High, Medium, Low):? > ")
    todos.append({'task': task, 'due by': due_by, 'priority': priority})
    print("\nThanks, this task has been added.")

def view_todos(todos):
    if not todos:
        print("There are no tasks to display.")
        return
    choice = input("\nView all or View by priority? (all/priority) > ")
    if choice.lower() == 'all':
        for todo in todos:
            print(f"Task: {todo['task']}, Due by: {todo['due by']}, Priority: {todo['priority']}")
    elif choice.lower() == 'priority':
        priority = input("\nWhich priority tasks to view (High, Medium, Low)? > ")
        for todo in todos:
            if todo['priority'].lower() == priority.lower():
                print(f"Task: {todo['task']}, Due by: {todo['due by']}, Priority: {todo['priority']}")

def edit_todo(todos):
    task_to_edit = input("Enter the task you want to edit: > ")
    for todo in todos:
        if todo['task'].lower() == task_to_edit.lower():
            new_task = input("What is the new task? (Leave blank to keep the same) > ")
            new_due_by = input("What is the new due date? (Leave blank to keep the same) > ")
            new_priority = input("What is the new priority? (Leave blank to keep the same) > ")
            if new_task:
                todo['task'] = new_task
            if new_due_by:
                todo['due by'] = new_due_by
            if new_priority:
                todo['priority'] = new_priority
            print("\nTask updated.")
            return
    print("Task not found.")

def remove_todo(todos):
    task_to_remove = input("\nEnter the task you want to remove: > ")
    initial_count = len(todos)
    todos[:] = [todo for todo in todos if todo['task'].lower() != task_to_remove.lower()]
    if len(todos) < initial_count:
        print("\nTask removed.")
    else:
        print("Task not found.")

def main():
    todos = []
    while True:
        clear_console()
        print("🌟Life Organizer🌟\n")
        choice = input("\nWelcome to the life organizer. Do you want to add, view, edit, or remove a to do?: (quit to exit) > ")
        if choice.lower() == 'add':
            add_todo(todos)
        elif choice.lower() == 'view':
            view_todos(todos)
        elif choice.lower() == 'edit':
            edit_todo(todos)
        elif choice.lower() == 'remove':
            remove_todo(todos)
        elif choice.lower() == 'quit':
            print("\nExiting the Life Organizer. Have a great day!")
            break
        time.sleep(5)  # Pause to let the user see the result.

if __name__ == "__main__":
    main()
