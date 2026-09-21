print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")
secret_number = 777
# number = int(input("number: "))

# while number != secret_number:
#     print("Ha ha! You're stuck in my loop!")
#     number = int(input("number: "))
# print("Well done, muggle! You are free now.")

while True:
    number = int(input("number: "))
    if number == secret_number:
        print("Well done, muggle! You are free now.")
        break
    else:
        print("Ha ha! You're stuck in my loop!")