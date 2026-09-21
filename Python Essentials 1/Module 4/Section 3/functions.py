def happy_new_year(wishes = True):
    print("Three...")
    print("Two...")
    print("One...")
    if not wishes:
        return

    print("Happy New Year!")
# happy_new_year()
# happy_new_year(False)

def boringFunc():
    return 123
x = boringFunc()
# print(x)

def str_lst_func(n):
    lst = []
    for i in range(0, n):
        lst.insert(0, i)
    return lst
print(str_lst_func(5))