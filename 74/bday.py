import calendar


def weekday_of_birth_date(date):
    """Takes a date object and returns the corresponding weekday string"""
    # Split it to year, month and day
    return calendar.day_name[date.weekday()]
