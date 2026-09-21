# no exception can be specified more than once

try:
    value = int(input("Enter a natural number: "))
    print("The reciprocal of ", value, "is", 1/value)
except ValueError:
    print("Not a natural number")
except ZeroDivisionError:
    print("Cant divide zero")
except:                             # this is the default except branch and should always be the last one
    print("Something is wrong")