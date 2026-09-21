# not a sequence type but can easily be adapted to sequence processing
# is mutable (can assign new values to keys)
# is not a list
# it holds key-value pairs (each key must be unique) (cannot be a list rather integer, float or string)
# each pair is a single element
# keys are case-sensitive
# both value and key can either be strings, string: integer, integer: string, or integers
# can only be looked through using keys but not values
# dictionaries are not lists and dont preserve the order but in Python 3.6 and above they have become ordered collections
# for loop is useless with it as it is not a sequence type
# but can be adapted to for loop requirements using tools (in other words, building an intermediate link between the dictionary and a temporary sequence entity)
# .clear() method removes all the elements
# .copy method to copy it whole

dictionary = {          # hanging indent
    "cat": "chat",
    "dog": "chien", 
    "horse": "cheval"
    }
phone_numbers = {'boss': 5551234567, 'Suzy': 22657854310}
empty_dictionary = {}
 
# print(dictionary)
# print(len(dictionary))
# print(phone_numbers)
# print(empty_dictionary)
# print(dictionary["cat"])
# print(phone_numbers["Suzy"])

# words = ['cat', 'lion', 'horse']
 
# for word in words:
#     if word in dictionary:
#         print(word, "->", dictionary[word])
#     else:
#         print(word, "is not in dictionary")

# to iterate we can use .keys() method which returns an iterable object consisting all the keys of the dictionary

# for key in dictionary.keys():
#     print(key)
#     print(key, "->", dictionary[key])

# the items() method returns tuples of key value pairs
# for eng, fren in dictionary.items():
#     print(eng, "->", fren)
# for item in dictionary.items():
#     print(item)
#     print(type(item))

# assigning new value to a key
# dictionary["cat"] = "minou"
# print(dictionary)

# can be sorted like this
# for key in sorted(dictionary.keys()):
#   print(key, "->", dictionary[key])

# to print only the values
# as the dictionary is not able to automatically find a key for a given value, the role of this method is rather limited.
# for fren in dictionary.values():
#     print(fren)

# adding new key-value pair
# dictionary["swan"] = "cygne"
# dictionary.update({"duck": "canard"})
# print(dictionary)

# removing a key (will also delete the corresponding value)
# del dictionary["dog"]
# print(dictionary)
# to remove the last item in a dictionary, use popitem()
dictionary.popitem()
print(dictionary)
print(dictionary.get("dog"))