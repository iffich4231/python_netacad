ls = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]

# new = []
# for i in ls:
#     if i not in new:
#         new.append(i)
# print(new)

# for i in range(len(ls) - 1, -1, -1):
#     if ls.count(ls[i]) > 1:
#         del ls[i]
# print(ls)

list_1 = ["A", "B", "C"]
list_2 = list_1
list_3 = list_2

del list_1[0]
del list_1

print(list_3)
