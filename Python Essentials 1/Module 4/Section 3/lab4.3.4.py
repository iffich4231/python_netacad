def isLeapYear(year):
    if year < 1582:
        return False
    return(year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

test_data = [1900, 2000, 2016, 1988]
test_results = [False, True, True, False]
for i in range(len(test_data)):
    yr = test_data[i]
    print(yr,"-> ",end="")
    result = isLeapYear(yr)
    if result == test_results[i]:
        print("OK")
    else:
        print("Failed")