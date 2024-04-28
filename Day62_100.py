import datetime
import sys

print("=_= PRIVATE DIARY =_= ✍\n")

def main():
    diary = {}
    correct_password = "secret123"  # Example password

    password_entered = input("Enter your password: ")
    if password_entered != correct_password:
        print("\nIncorrect password. Exiting.")
        sys.exit()

    while True:
        print("\nMain Menu:")
        print("\n1. Add Entry")
        print("2. View Entries")
        print("3. View Entry from Specific Date")
        print("4. Exit\n")
        choice = input("Choose an option: ")

        if choice == "1":
            entry = input("\nType your diary entry: ")
            timestamp = datetime.datetime.now()
            diary[timestamp] = entry
            print("Entry added.")

        elif choice == "2":
            if not diary:
                print("\nNo entries to display.")
                continue
            for date in sorted(diary.keys(), reverse=True):
                print(f"\nEntry from {date.strftime('%Y-%m-%d %H:%M:%S')}:")
                print(diary[date])
                if input("\nType 'next' to view the next entry or 'menu' to return to the main menu: ") == 'menu':
                    break

        elif choice == "3":
            date_str = input("Enter the date (YYYY-MM-DD): ")
            try:
                date_requested = datetime.datetime.strptime(date_str, '%Y-%m-%d')
                entries = {date: diary[date] for date in diary if date.date() == date_requested.date()}
                if entries:
                    for date in sorted(entries.keys(), reverse=True):
                        print(f"\nEntry from {date.strftime('%Y-%m-%d %H:%M:%S')}:")
                        print(entries[date])
                else:
                    print("\nNo entries found for that date.")
            except ValueError:
                print("Invalid date format.")

        elif choice == "4":
            print("Exiting.")
            break
        else:
            print("\nInvalid option. Please choose again.")

if __name__ == "__main__":
    main()
