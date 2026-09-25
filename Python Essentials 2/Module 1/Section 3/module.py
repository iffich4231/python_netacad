counter = 0
# in order to know how many times the functions have been invoked, you need a counter 
# initialized to zero when the module is being imported

# print("I am a module.")
# print(__name__)  # by running the file directly, the __name__ variable is set to __main__

# if __name__ == "__main__":
#     print("I prefer to be a module.")
# else:
#     print("I like to be a module.")

#!/usr/bin/env python3      # called shabang, hashpling, poundbang...etc.
    # for unix and unix-like OSs incl. MacOS this line instructs the OS how to execute the contents of the file
    # or what program needs to be launched to interpret the text. In some environments especially those
    # connected with web servers the absence of this line will cause trouble

""" module.py - an example of a Python module """
# a string (maybe a multiline) placed before any module instructions (including imports) is called the doc-string,
# and should briefly explain the purpose and contents of the module
# should use triple standard quotes


__counter = 0   
# a personal/private variable in a module, which the module user may read but should not modify
# unlike other programming lang. python has no means to hide such variables from the users
# preceded with _ or __ (underscores)

def suml(the_list):
    global __counter
    __counter += 1
    the_sum = 0
    for element in the_list:
        the_sum += element
    return the_sum

def prodl(the_list):
  global __counter
  __counter += 1
  prod = 1
  for element in the_list:
   prod *= element
   return prod

if __name__ == "__main__":      # this is to detect when the file runs stand-alone, and we can perform some tests
  print("I prefer to be a module, but I can do some tests for you.")
  my_list = [i+1 for i in range(5)]
  print(suml(my_list) == 15)
  print(prodl(my_list) == 120)