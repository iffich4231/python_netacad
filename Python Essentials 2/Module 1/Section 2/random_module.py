# the random module delivers mechanisms allowing to operate with psuedorandom numbers
# pseudo : the numbers generated may look random but are very refined algorithms
# algorithms arent random, they are deterministic and predictable
# the random generator takes a value called a seed, as an input to calculate the next "random" number 
# which in turn becomes the new seed value
# the length of the cycle where the values are unique may be long but not infinite and 
# repeat sooner or later, its a feature, not a bug
# the random factor (first seed value) may be augmented with a number taken from the current time
# which ensures each program launch is different
# such an initialization is done by Python during module import
# seed() func sets the seed with the current time
# seed(int) func sets the seed with the integer value, it ensures the sequence of generated values is always the same

# from random import random, seed
# seed(0)
# for i in range(5):
#     print(random())

# randrange(end)    # wont include the end integer (end - 1)
# randrange(beg, end)
# randrange(beg, end, step)
# the above 3 will generate integer psuedorandomly from the given range. with right-sided exclusion! as in range()
# randint(left, right)  randint is Inclusive right-side. 1-10 will include 10

# from random import randrange, randint
# print(randrange(1), end=' ')
# print(randrange(0, 1), end=' ')
# print(randrange(0, 1, 1), end=' ')
# print(randint(0, 1))    

from random import choice, sample
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# their output is not predictable
print(choice(my_list))          # chooses one element from the given sequence
print(sample(my_list, 5))       # it generates a new list of given num of elements from the given list, here it takes 5 elements
print(sample(my_list, 10))      # here it takes 10 elements