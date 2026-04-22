"""
datetime_utils.py

Utility functions for date and time operations using datetime module.
Includes formatting, comparison, future dates, and age calculation.
"""

from datetime import datetime, date, time, timedelta


# -------------------- CURRENT DATE & TIME --------------------

def get_current_datetime():
    """Returns current date and time."""
    return datetime.now()


def get_date_parts():
    """Returns current year, month, day."""
    now = datetime.now()
    return now.year, now.month, now.day


# -------------------- CUSTOM DATE & TIME --------------------

def create_date(year, month, day):
    """Creates a date object."""
    return date(year, month, day)


def create_time(hour, minute, second):
    """Creates a time object."""
    return time(hour, minute, second)


# -------------------- FORMATTING --------------------

def format_date_time():
    """Returns formatted date and time."""
    now = datetime.now()
    return now.strftime('%d-%m-%Y'), now.strftime('%H:%M:%S')


# -------------------- STRING TO DATE --------------------

def convert_string_to_date(date_str):
    """Converts string to datetime object."""
    try:
        return datetime.strptime(date_str, "%Y-%m-%d")
    except:
        return "Error: Invalid format (use YYYY-MM-DD)"


# -------------------- FUTURE DATE --------------------

def get_future_date(days):
    """Returns future date after given days."""
    return datetime.now() + timedelta(days=days)


# -------------------- DATE DIFFERENCE --------------------

def date_difference(d1, d2):
    """Returns difference between two dates."""
    return d2 - d1


# -------------------- DAY NAME --------------------

def get_day_name():
    """Returns current day name."""
    return datetime.now().strftime('%A')


# -------------------- AGE CALCULATOR (FIXED + IF-ELSE) --------------------

def calculate_age(birth_year, birth_month, birth_day):
    """
    Calculates exact age using if-else logic.
    """
    today = date.today()
    birth = date(birth_year, birth_month, birth_day)

    age = today.year - birth.year

    # IF-ELSE adjustment (important logic)
    if (today.month, today.day) < (birth.month, birth.day):
        age -= 1

    return age


# -------------------- AGE CATEGORY (IF-ELSE BONUS) --------------------

def age_category(age):
    """Categorizes age using if-else."""
    if age < 13:
        return "Child"
    elif age < 20:
        return "Teenager"
    elif age < 60:
        return "Adult"
    else:
        return "Senior"