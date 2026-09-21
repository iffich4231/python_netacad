# a module is like a book in a library (python library) it stores the definitions and statements
# modules consists of entities (like chapters in a book) functions, variables, constants, classes, objects

# import math     # import math, sys (also possible but not preferred)
import sys  
from math import sin, pi # this way only the sin and pi entity is being imported and no other entity is imported
# from module import *  # imports all entities from the module convenient but unsafe as you may not be able to avoid name conflicts
# import module is namespace safe as it brings its own namespace and doesnt dump the entities in your global / local namespace. 
# but the upper import imports all names in to the global namespace and you dont need the module prefix like math.sin()

# import module as alias    to give your module an alias to avoid naming conflicts and or shortening the name of module
# import math as m  the math module name is gone and no longer accessible. you use m.sin() m.pi
# from module import name as alias  aliases the entity
# from module import n as a, m as b, o as c     can be repeated for multiple entities, separated with commas

# Definition: A namespace is Python's internal dictionary mapping variable names to their objects to prevent naming conflicts.
# Scope vs. Namespace: A namespace is the actual container holding the names; a scope is the area of code where that namespace is accessible.
# LEGB Lookup Order: Python searches for names in a strict 4-level hierarchy:
# L (Local): Variables created inside the current function.
# E (Enclosing): Variables in outer/parent functions (for nested functions).
# G (Global): Variables defined at the top level of the script file.
# B (Built-in): Predefined Python keywords and functions (like len, print, range).
# Assignment Creates Local: Assigning a value to a variable inside a function automatically creates a local variable by default—it does not modify a global variable with the same name.
# global Keyword: Using global x inside a function forces Python to read and write to the top-level script variable instead of making a new local one.
# Built-in Shadowing: Defining a global variable named after a built-in function (e.g., list = [1, 2]) overrides the built-in function in that script and causes a TypeError when called later.

# print(math.sin(math.pi/2))  # it is compulsory to use the name of the module, . , and than the entity

# def sin(x):
#     if 2 * x == pi:
#         return 0.99999
#     else:
#         return None
# pi = 3.14
# print(sin(pi/2))            # this is how the two namespaces (mine and math module) can coexist
# print(math.sin(math.pi/2))

print(sin(pi/2))    # after sin, pi import

# redifining the sin and pi entities will supersede the imported definitions within the code's namespace
def sin(x):
    if 2 * x == pi:
        return 0.99999
    else:
        return None
pi = 3.14
print(sin(pi/2))    # the imported sin, pi produce 1.0 and our sin, pi 0.99999

from math import sin, pi    # we did the import again and they supersede our previous definitions within the namespace
print(sin(pi/2))    # Output: 1.0