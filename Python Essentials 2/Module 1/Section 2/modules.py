# dir() reveals all names(alphabetically sorted) provided through a module
# the module has to be imported as a whole, import names from module is not enough
# if the module is aliased so is alias to be used as the argument

# import math
# # print(dir(math))
# for name in dir(math):
#   print(name, end=" ")


from math import pi, radians, degrees, sin, cos, tan, asin

ad = 90
ar = radians(ad)
ad = degrees(ar)

print(ad == 90.)
print(ar == pi / 2.)
print(sin(ar) / cos(ar) == tan(ar))
print(asin(sin(ar)) == ar)