import datetime

def event_countdown_timer():
    print("🌟 Event Countdown Timer 🌟\n")
    event_name = input("\nInput the event > ")
    year = int(input("\nInput the year > "))
    month = int(input("\nInput the month > "))
    day = int(input("\nInput the day > "))

    today = datetime.date.today()
    event_date = datetime.date(year, month, day)
    days_difference = (event_date - today).days

    if days_difference == 0:
        print(f"\n🎉🎉{event_name} is today! 🎉🎉")
    elif days_difference > 0:
        print(f"\n{event_name} is in {days_difference} days.")
    else:
        print(f"\n😢{event_name} was {-days_difference} days ago.😢")

event_countdown_timer()
