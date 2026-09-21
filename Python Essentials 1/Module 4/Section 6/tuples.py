# cannot be modified in situ (in situ latin for in position, it refers to mutable data that can be freely updated anytime)
# behaves like a list but is immutable
# you cannot modify a tuple but can delete it as a whole (del my_tuple)
# list[]
# tuples () or values separated by commas
# can contain other tuples and lists and other way around
# can use built in tuple() function to convert certain iterables to a tuple and same goes for list using built-in list() function
# tup = 1, 2, 3 | a, b, c = tup | unpacks the elements and assigns to a, b, & c variables
# tup.count(2) gives num of occurences of 2 in the tuple

tuple_1 = (1, 2.3, "book", 4) # each tuple elem be of a different type
tuple_2 = 1, 2, 3, 4

# print(tuple_1)
# print(tuple_2)

empty_tuple = () # () required when creating an empty tuple

one_elem_tuple_1 = (1, ) # comma is required when creating a single value tuple (due to syntax reasons or else you get a variable)
one_elem_tuple_2 = 1.9, 
# print(one_elem_tuple_1)
# print(one_elem_tuple_2)

my_tuple = (1, 10, 100, 1000)
# can use same conventions as in a list
# print(my_tuple[0])
# print(my_tuple[-1])
# print(my_tuple[:2])
# print(my_tuple[1:])
# print(my_tuple[:-2])

# for elem in my_tuple:
#     print(elem)

# tuple doesnt support following
# my_tuple.append(10000)
# del my_tuple[0]
# my_tuple[1] = -10

my_tuple = (1, 10, 100)

# t1 = my_tuple + (1000, 10000) # joining tuples is possible
# t2 = my_tuple * 3 # multiplying tuples is possible

# print(len(t2))
# print(t1)
# print(t2)
# print(10 in my_tuple)
# print(-10 not in my_tuple)

var = 123
 
t1 = (1, )
t2 = (2, )
t3 = (3, var)
 
t1, t2, t3 = t2, t3, t1
 
print(t1, t2, t3)