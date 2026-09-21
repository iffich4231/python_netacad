# z = 0
# y = 10
# x = y < z and z > y or y < z and z < y

# print(x)

# # in = 1

# x = 1
# y = 2
# x, y, z = x, x, y   # 1,1,2
# z, y, z = x, y, z   # z = 1, y = 1, z = 2

# print(x, y, z)

# a = 1   # 0001
# b = 0   # 0000
# a = a ^ b   # 0001 , a = 1
# b = a ^ b   # 0001 , b = 1
# a = a ^ b   # 0000 , a = 0
# print(a, b) # (0, 1) 

# def fun(x):
#     if x % 2 == 0:
#         return 1
#     else:
#         return 2
# print(fun(fun(2)))

# nums = [1, 2, 3]
# vals = nums
# del vals[:]
# print(nums)

# x = int(input())    # x = 3
# y = int(input())    # y = 2
# x = x % y           # 3 % 2 = 1, x = 1
# x = x % y           # 1 % 2 = 1, x = 1
# y = y % x           # 2 % 1 = 0, y = 0
# print(y)

# print("a", "b", "c", sep="sep")

# x = 1 // 5 + 1 / 5
# print(x)

# x = float(input())
# y = float(input())
# print(y ** (1 / x))

# dct = {'one': 'two', 'three': 'one', 'two': 'three'}
# v = dct['three']    # one

# for k in range(len(dct)):   # len = 3.
#     v = dct[v]  # 1st iteration v = one , v = two, 2nd iter. v = three, 3rd iter. v = one

# print(v)

# lst = [i for i in range(-1, -2, -1)]
# print(lst)

# def fun(x, y):              # 0, 3 | 0, 2 | 0, 1 | 0, 0
#     if x == y:              
#         return x                                # returns 0
#     else:
#         return fun(x, y-1)  # 0, 2 | 0, 1 | 0, 0
# print(fun(0, 3))

# i = 0     # infinite loop
# while i < i + 2 :
#     i += 1
#     print("*")
# else:
#     print("*")

# tup = (1, 2, 4, 8)
# tup = tup[-2:-1]
# tup = tup[-1]           # returns the element as a variable
# print(tup)

# dd = {"1": "0", "0": "1"}
# for x in dd.vals():             # vals is a wrong attribute. its value()
#     print(x, end="")

# dct = {}
# dct['1'] = (1, 2)
# dct['2'] = (2, 1)

# for x in dct.keys():
#     print(dct[x][1], end="")

# def fun(inp=2, out=3):
#     return inp * out
# print(fun(out=2))

# try:
#     value = input("Enter a value: ")
#     print(int(value)/len(value))        # returns 0.0 as 0 / 1 is completely valid in python and not a zerodivisionerror
# except ValueError:
#     print("Bad input...")
# except ZeroDivisionError:
#     print("Very bad input...")
# except TypeError:
#     print("Very very bad input...")
# except:
#     print("Booo!")

# try:                    # it raises a syntaxerror
#     print(5/0)
#     break       # no break outside a loop, it will be triggered immediately
# except:
#     print("Sorry, something went wrong...")
# except (ValueError, ZeroDivisionError):     # should come before the generic, bare except
#     print("Too bad...")

# foo = (1, 2, 3)
# print(foo.index(0))     # in tuple index(x) takes an element in the tuple and gives back the index otherwise ValueError
# print(type(foo))

# my_list = [1, 2]

# for v in range(2):
#     my_list.insert(-1, my_list[v])     # insert() inserts the element before the specified index
                                        # append(item) puts the item at the very end
# print(my_list)    # [1, 1, 1, 2]



