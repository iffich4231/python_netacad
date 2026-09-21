# def liters_100km_to_miles_gallon(litres):
#     return 235.215 / litres

# def miles_gallon_to_liters_100km(miles):
#     return 235.215 / miles

MILE_IN_KM = 1.609344
GALLON_IN_LITERS = 3.785411784
def liters_100km_to_miles_gallon(litres):
    return (GALLON_IN_LITERS / litres) * (100 / MILE_IN_KM)

def miles_gallon_to_liters_100km(miles):
    return (100 * GALLON_IN_LITERS) / (MILE_IN_KM * miles)

print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))