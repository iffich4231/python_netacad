# ls1 = [1]
# ls2 = ls1
# ls1[0] = 2
# print(ls2)

# slicing (duplicating / copying the contents only and not the name)

ls1 = [1, 2, 3, 4, 5]
# ls2 = ls1[0:3]
# ls1[0] = 2
# print(ls2)

# del ls1[1:3]
# print(ls1)
# del ls1[:]  # deletes the contents only and returns an empty list
# print(ls1)
# del ls1   # deletes the entire list
# print(ls1)

print(1 in ls1)
print(2 not in ls1)
