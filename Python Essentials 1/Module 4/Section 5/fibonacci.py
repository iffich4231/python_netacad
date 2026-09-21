def fib(n):
    if n < 1:
        return None
    if n < 3:
        return 1

    elem_1 = elem_2 = 1
    sum = 0
    for i in range(3, n + 1): # i = 3, 4, 5 & 6
        sum = elem_1 + elem_2
        elem_1, elem_2 = elem_2, sum # first pass: 1 & 2, 2nd pass: 2 & 3, 3rd pass: 3 & 5, 4th pass: 5 & 8
    return sum

print(fib(30))
