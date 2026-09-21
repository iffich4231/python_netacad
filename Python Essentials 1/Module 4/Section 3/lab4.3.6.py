def isLeapYear(year):
    if year < 1582:
        return False
    return((year % 4 == 0 and year % 100 != 0) or year % 400 == 0)

def daysInMonth(year, month):
    if(year < 1582) or (month < 1 or month > 12):
        return None
    month_lengths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if (isLeapYear(year) and month == 2):
        return 29
    return month_lengths[month - 1]

def dayOfYear(year, month, day):
    if(year < 1582 or month < 1 or month > 12 or day < 1 or day > daysInMonth(year, month)): # validate max days of the month
        return None
    totalDays = 0       # a variable to keep track
    for m in range(1, month):       # range starting from 1st month till the month before
        totalDays += daysInMonth(year, m)       # totaling the days of previous months
    totalDays += day
    return totalDays

print(dayOfYear(1583, 3, 10))