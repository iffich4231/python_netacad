def isPrime(num):
    if(num < 2):
        return False
    for i in range(2, num):
        if(num % i == 0):
            return False
    return True                 # it should stay outside, else 9 % 2 != 0 will execute the else statement
print(isPrime(10000919))

# for i in range(1, 30):
#     if isPrime(i + 1):
#         print(i + 1, end=" ")
# print()