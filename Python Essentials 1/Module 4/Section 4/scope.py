def break_the_link(my_list):
    my_list = [100, 200, 300]
    print(my_list)
numbers = [1, 2, 3]
break_the_link(numbers)
print(numbers)





a = 1
def fun():
    global a
    a = 2
    print(a)
 
a = 3
fun()
print(a)