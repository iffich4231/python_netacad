# ls = [17, 3, 11, 5, 1, 9, 7, 15, 131]
# largest = ls[0]

# for i in ls[1:]:
#     if i > largest:
#         largest = i

# print(largest)

# ls = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# find = 19
# found = False

# for i in ls:
#     found = find == i
#     if found:
#         break

# if found: print("Found")
# else: print("absent")

drawn = [5, 110, 9, 402, 30, 491]
bets = [3, 7, 11, 42, 34, 49]
hits = 0

for num in bets:
    if num in drawn:
        hits += 1

print(hits)