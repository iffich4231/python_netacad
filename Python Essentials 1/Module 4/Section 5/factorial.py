def factorial_num(n):
    if n < 0: return None
    if n < 2: return 1

    product = 1
    for i in range(2, n + 1):
        product *= i
    return product

print(factorial_num(-2))
print(factorial_num(2))
print(factorial_num(0))
print(factorial_num(4))

