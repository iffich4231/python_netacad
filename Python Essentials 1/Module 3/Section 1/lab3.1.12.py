year = int(input("Enter a year: "))
msg = ""

if year < 1582:
	msg = "Not within the Gregorian calendar period"
else:
    if (year % 4 != 0): msg = "Common Year"
    elif (year % 100 != 0): msg = "Leap Year"
    elif (year % 400 != 0): msg = "Common Year"
    else: msg = "Leap Year"

print(msg)