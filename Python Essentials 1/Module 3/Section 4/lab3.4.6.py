hat_list = [1, 2, 3, 4, 5]

# # step 1
# hat_list[2] = input("Please enter the replacement for the middle number in the list: ")
# print(hat_list)

# # step 2
# del hat_list[-1]
# print(hat_list)

# # step 3
# print(len(hat_list))

# hat_list.insert(1, 3)
# print(hat_list)

# myList = []
# for i in range(5):
#     myList.insert(0, i + 1)
# print(myList)

myList = [1, 2, 3, 4, 5]
total = 0
# for i in range(len(myList)):
    # total += myList[i]
# for i in myList:
#     total += i

# myList[0], myList[4] = myList[4], myList[0]
# myList[1], myList[3] = myList[3], myList[1]
length = len(myList)
for i in range(length // 2): # //2 because we are iterating only half of the list and it covers odd num as the middle stays in the middle
    myList[i], myList[length - i - 1] = myList[length - i - 1], myList[i] # length - i - 1 gives the corresponding opposite from the right side

print(myList)