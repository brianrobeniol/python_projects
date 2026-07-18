"""
"Python Programming Essentials: datetime_project"
Collection of functions to process dates.
"""

import datetime

def days_in_month(year, month):
    """
    Inputs:
      year  - an integer between datetime.MINYEAR and datetime.MAXYEAR
              representing the year
      month - an integer between 1 and 12 representing the month

    Returns:
      The number of days in the input month.
    """
    
    #Create a date for the first day of the current month.
    current_month = datetime.date(year, month, 1)

    #Create a date for the first day of the next month.
    if month == 12:
        next_month = datetime.date(year +1, 1, 1)
    else:
        next_month = datetime.date(year, month +1, 1)
    
    #The difference in days is the length of the current month.
    days = next_month - current_month
    
    return days.days

#Tests for days_in_month.
print(days_in_month(2027, 1))   # 31
print(days_in_month(2026, 2))   # 28
print(days_in_month(2020, 2))   # 29
print(days_in_month(2025, 12))  # 31

def is_valid_date(year, month, day):
    """
    Inputs:
      year  - an integer representing the year
      month - an integer representing the month
      day   - an integer representing the day

    Returns:
      True if year-month-day is a valid date and
      False otherwise
    """
    
    #Check that the year is a valid year.
    if year < datetime.MINYEAR or year > datetime.MAXYEAR:
        return False
    
    #Check that the month is a valid month.
    if month < 1 or month > 12:
        return False	
    
    #Check that the day is a valid day.
    if day < 1 or day > days_in_month(year, month):
        return False
    
    return True
    
#Tests for is_valid_date.
print(is_valid_date(2020, 2, 29))   # True
print(is_valid_date(2025, 2, 29))   # False
print(is_valid_date(2027, 13, 1))   # False
print(is_valid_date(2021, 4, 31))   # False

def days_between(year1, month1, day1, year2, month2, day2):
    """
    Inputs:
      year1  - an integer representing the year of the first date
      month1 - an integer representing the month of the first date
      day1   - an integer representing the day of the first date
      year2  - an integer representing the year of the second date
      month2 - an integer representing the month of the second date
      day2   - an integer representing the day of the second date

    Returns:
      The number of days from the first date to the second date.
      Returns 0 if either date is invalid or the second date is
      before the first date.
    """
    
    #Confirm that the dates are valid.
    if not is_valid_date(year1, month1, day1):
        return 0
    
    if not is_valid_date(year2, month2, day2):
        return 0
    
    #Create date objects
    first_date = datetime.date(year1, month1, day1)
    second_date = datetime.date(year2, month2, day2)
    
    #Make sure that the second date is not before the first date.
    if first_date > second_date:
        return 0
    
    #Return the difference between the dates in days.
    difference = second_date - first_date
    
    return difference.days

#Tests for is_valid_date.
print(days_between(2026, 7, 1, 2026, 7, 2))    # 1
print(days_between(2026, 7, 2, 2026, 7, 1))    # 0
print(days_between(2024, 2, 28, 2024, 3, 1))   # 2
print(days_between(2025, 12, 31, 2026, 1, 1))  # 1
print(days_between(2020, 1, 1, 2021, 1, 1))    # 366

def age_in_days(year, month, day):
    """
    Inputs:
      year  - an integer representing the birthday year
      month - an integer representing the birthday month
      day   - an integer representing the birthday day

    Returns:
      The age of a person with the input birthday as of today.
      Returns 0 if the input date is invalid or if the input
      date is in the future.
    """
    
    #Check that the birthday is valid.
    if not is_valid_date(year, month, day):
        return 0
    
    #Confirm today's day.
    today = datetime.date.today()
    
    #calculate the person's age in days.
    age = days_between(year, month, day, today.year, today.month, today.day)

    return age

#Tests for the birthday age checker.
print(age_in_days(2026, 7, 15))   # 0
print(age_in_days(2026, 2, 30))   # 0
print(age_in_days(2030, 1, 1))    # 0
print(age_in_days(2000, 1, 1))    # (Like, thousands of days)
    
