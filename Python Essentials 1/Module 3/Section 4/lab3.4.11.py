beatles = []
print("Step 1:", beatles)
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")
print("Step 2:", beatles)
beatles.append(input("Please add \"Stu Sutcliffe\""))
beatles.append(input("Please add \"Pete Best\""))
print("Step 3:", beatles)
for i in range(len(beatles) -1, -1, -1):
    if((beatles[i] == "Stu Sutcliffe") or (beatles[i] == "Pete Best")):
        del(beatles[i])
print("Step 4:", beatles)
beatles.insert(0, "Ringo Starr")
print("Step 5:", beatles)