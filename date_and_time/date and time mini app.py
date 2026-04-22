from datetime_utils import *

def line():
    print("=" * 40)

while True:
    line()
    print("📅 DATE & TIME MINI APP")
    line()
    print("1. Current Date & Time")
    print("2. Format Date & Time")
    print("3. Days Between Dates")
    print("4. Add Days")
    print("5. Day Name")
    print("6. Age Calculator")
    print("7. Exit")
    line()

    choice = input("👉 Enter your choice: ")

    line()

    if choice == "1":
        print("Current Date & Time:", get_current_datetime())

    elif choice == "2":
        d, t = format_date_time()
        print("Formatted Date:", d)
        print("Formatted Time:", t)

    elif choice == "3":
        d1 = input("Enter first date (YYYY-MM-DD): ")
        d2 = input("Enter second date (YYYY-MM-DD): ")
        result = days_between_dates(d1, d2)
        print("Days Difference:", result)

    elif choice == "4":
        date_input = input("Enter date (YYYY-MM-DD): ")
        days = int(input("Enter days to add: "))
        print("New Date:", add_days(date_input, days))

    elif choice == "5":
        date_input = input("Enter date (YYYY-MM-DD): ")
        print("Day:", get_day_name(date_input))

    elif choice == "6":
        y = int(input("Enter birth year: "))
        m = int(input("Enter birth month: "))
        d = int(input("Enter birth day: "))

        age = calculate_age(y, m, d)
        print("Your Age:", age)
        print("Category:", age_category(age))

    elif choice == "7":
        print("🚪 Exiting...")
        break

    else:
        print("❌ Invalid choice")

    input("\nPress Enter to continue...")