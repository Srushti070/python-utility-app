from datetime_utils import *

print("Now:", get_current_datetime())

year, month, day = get_date_parts()
print("Date Parts:", year, month, day)

print("Custom Date:", create_date(2026, 5, 20))
print("Custom Time:", create_time(10, 44, 59))

print("Formatted:", format_date_time())

print("Converted:", convert_string_to_date("2026-03-12"))

print("Future Date:", get_future_date(20))

d1 = create_date(2026, 4, 1)
d2 = create_date(2026, 9, 20)
print("Difference:", date_difference(d1, d2))

print("Day Name:", get_day_name())

age = calculate_age(2006, 9, 7)
print("Age:", age)
print("Category:", age_category(age))