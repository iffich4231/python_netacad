# ls = []
# swapped = True
# num = int(input("How many elements should the list contain: "))

# for i in range(num):
#     val = float(input("Enter an element: "))
#     ls.append(val)

# while swapped:
#     swapped = False
#     for i in range(len(ls) - 1):
#         if ls[i] > ls[i + 1]:
#             swapped = True
#             ls[i], ls[i + 1] = ls[i + 1], ls[i]

# print(ls)

ls = [5, 3, 1, 2, 4]
print(ls)
# ls.sort()
# print(ls)
ls.reverse()
print(ls)