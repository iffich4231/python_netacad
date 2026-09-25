# as we imported this module (our own module), python created a subfolder pycache
# when a module is imported for the first time, python translates its contents into a 
# somewhat compiled shape (which is unreadable to humans)
# it doesnt contain machine code, rather internal python semi-compiled code
# this way the execution starts and runs faster as it doesnt require a lots of checks needed for a pure source file
# afterwards every subsequent import goes quicker

# when a module is imported. Its contents are implicitly executed by Python
# The initialization takes place only once, when the first import occurs, so the assignments
# arent repeated unnecessarily

# when a file is imported as a module, its __name__ variable is set to the file's (module's) name
# it is a built-in variable in Python that tells a script how it is currently being run
# was it directly than the variable is set to __main__
# is it imported than the name is changed to the filename that contains the module script
# Allows a script to serve a dual purpose—it can be run standalone as a main program or safely imported as a 
# reusable module without executing test code automatically.

# import module
# print(module.counter)

from module import suml, prodl
import sys

zeroes = [0 for i in range(5)]
ones = [1 for i in range(5)]
# print(suml(zeroes))
# print(prodl(ones))

# Python needs to know where on your comp to look for the imported modules
# sys.path is simply a list of folder paths where Python searches for the modules
# the for statement iterates through the list of search directories stored in 
    # sys.path that python searches sequentially from top to botthom
# python stops searching as soon as it finds the first module name match and ignores the rest
# shadowing danger: any file with name like random.py or math.py in your current directory
    # will be the first match and blocks python from reaching the standard library at position 4 below
# begins from the first directory where your current script is running
    # d:\IT\Git Repositories\python_netacad\Python Essentials 2\Module 1\Section 3
    # C:\Users\iffich\AppData\Local\Programs\Python\Python312\python312.zip
    # C:\Users\iffich\AppData\Local\Programs\Python\Python312\DLLs
    # C:\Users\iffich\AppData\Local\Programs\Python\Python312\Lib
    # C:\Users\iffich\AppData\Local\Programs\Python\Python312
    # C:\Users\iffich\AppData\Local\Programs\Python\Python312\Lib\site-packages

# for p in sys.path:
#     print(p)

# from sys import path
# path.append("..\\modules")    # it appends the relative path to pythons search paths, 
                                # goes one directory up and in the foler "modules", one "\" is an escape character
# import module
# as it is relative, so will no longer work if the main script is moved to somewhere else
# path.append("C:\\Users\user\\py\\modules") or else use an absolute path
# path.append has the lowest priority as it is inserted at the end of the list
# path.insert(0, r"D:\ExtraModules") has the highest priority, gets inserted before your current directory
    # the r is a string literal called Raw String
    # it tells python to treat \ as literal characters rather than escape characters
    # or escape backslashes like "C:\\Users\\folder"
    # or forward slashes like "C:/Users/folder"