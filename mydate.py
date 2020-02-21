# mydate.py
import random

def is_valid_month_num(n): 
    return n in range(1,13)

def month_num_to_string(month_num):
    if (not is_valid_month_num(month_num)):
        return None
    month_mapping = {
         1: "January",
         2: "February",
         3: "March",
         4: "April",
         5: "May",
         6: "June",
         7: "July",
         8: "August",
         9: "September",
         10: "October",
         11: "November",
         12: "December",
    }
    return month_mapping.get(month_num)

def date_to_string(date):
    if (len(date) == 3):
        return (month_num_to_string(date[1]) + " " + 
        str(date[2]) + ", " + str(date[0]))
    return (month_num_to_string(date[0]) + " " + 
        str(date[1]))

def dates_to_strings(date_list):
    return [date_to_string(date) for date in date_list]

def remove_years(date_list):
    return [[date[1], date[2]] for date in date_list]

def is_leap_year(year):
    if (year % 4 == 0):
        if (year % 100 == 0):
            if (year % 400 == 0):
                return True
            return False
        return True
    return False

def get_num_days_in_month(month_num, year):
    if (not is_valid_month_num(month_num)):
        return None
    # Handle case when this is febuary 
    if (month_num == 2):
        if is_leap_year(year):
            return 29
        return 28
    # All other cases 
    days_mapping = {
        1: 31,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31,
    }
    return days_mapping.get(month_num)

def generate_date(start_year, end_year):
    year = random.randrange(start_year, end_year + 1)
    month = random.randrange(1, 13)
    day = random.randrange(1, get_num_days_in_month(month, year))
    return [year, month, day]

