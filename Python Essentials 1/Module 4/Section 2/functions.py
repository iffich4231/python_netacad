# def intro(firstName, lastName):
#     print("Hello, I'm", firstName, lastName)
# intro("Iffi", "Ch")
# intro("Ch", "Iffi")
# intro(lastName = "Bond", firstName = "James")

# def adding(a, b, c):
#     print(a, "+", b, "+", c, "=", a + b + c)
# adding(1, a = 3, b = 2)

def intro(firstName = "Iffi", lastName = "Ch"):
    print("Hello, I'm", firstName, lastName)
intro("Iffi", "Ch")
intro("Iffi")
intro()
intro(lastName = "Bond", firstName = "James")
intro(firstName = "James")