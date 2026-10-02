# not to forget, strings are immutable
# all the methods deliver a new string output and dont alter the input
# if the output is not used in any way(assigning to a variable, or passed to a function/method), it will disappear
# methods dont have to be invoked from within variables only
# they can be invoked directly from within string literals

# capitalize()
    # if the first character index[0] is a letter it will be converted to upper-case
    # and the rest to lower-case
    # print('aBcD'.capitalize())    # Abcd
    # print('123'.capitalize())     # 123
    # print("αβγδ".capitalize())    # Αβγδ

# center()
    # tries to center the copy of the string inside a field of a specified width
    # adds some spaces before and after the string
    # print('[' + 'alpha'.center(10) + ']')
    # print('[' + 'Beta'.center(2) + ']')
    # print('[' + 'Beta'.center(4) + ']')
    # print('[' + 'Beta'.center(6) + ']')
    # print('[' + 'gamma'.center(20, '*') + ']')  # 2nd parameter replaces spaces with the given char

# endswith()
    # the method checks the end of the given string and returns True or False
    # the substring can only be the last characters and not near the end
    # if "epsilon".endswith("on"):
    #     print("yes")
    # else:
    #     print("no")
    # t = "zeta"
    # print(t.endswith("a"))
    # print(t.endswith("A"))
    # print(t.endswith("et"))
    # print(t.endswith("eta"))

# find()
    # this method is similar to index() (looks for a substring and returns the index of the first occurence)
    # but, it is safer
    # it doesnt generate an error if the substring is not found, rather it returns -1
    # for a single char use in, as it is significantly faster
    # works with strings only
    # print("Eta".find("ta"))     # 1
    # print("Eta".find("mma"))    # -1
    # t = 'theta'
    # print(t.find('eta'))
    # print(t.find('et'))
    # print(t.find('the'))
    # print(t.find('ha'))
    # print('kappa'.find('a', 2))     # the second parameter gives the index to start with
    # can also be used to find all the occurences of a substring like this:
    # the_text = """A variation of the ordinary lorem ipsum
    # text has been used in typesetting since the 1960s 
    # or earlier, when it was popularized by advertisements 
    # for Letraset transfer sheets. It was introduced to 
    # the Information Age in the mid-1980s by the Aldus Corporation, 
    # which employed it in graphics and word-processing templates
    # for its desktop publishing program PageMaker (from Wikipedia)"""
    # fnd = the_text.find('the')
    # while fnd != -1:
    #     print(fnd)
    #     fnd = the_text.find('the', fnd + 1)
    # also has a 3rd parameter which defines the stopping index(will not be included)
    # print('kappa'.find('a', 1, 4))
    # print('kappa'.find('a', 2, 4))

# isalnum()
    # check if the string contains only alphabets and numbers. any other character will make it return False, otherwise true

# isalpha()
    # checks if the string contains only alphabets

# isdigit()
    # checks if the string contains only digits

# islower()
    # checks if all the alphabets are lower-case

# isspace()
    # checks if the string only contains whitespaces

# isupper()
    # checks if all the alphabets are upper-case

# join()
    # expects one argument as a list, and all the list's elements should be string.
        # other TypeError exception
    # all the elements will be joined into one string, but the strings from which the method has been invoked,
        # is used as a separator, put among the strings
    # print(",".join(["omicron", "pi", "rho"]))   # omicron,pi,rho

# lower()
    # returns a new string with all upper-case replaced with lower-case letters
    # print("SiGmA=60".lower())   # sigma=60

# lstrip()  (leftstrip)
    # returns a new string by removing all leading whitespaces
    # print("[" + " tau ".lstrip() + "]") # [tau ]
    # the one-parameter version, additionaly removes all the characters enlisted in the arguments
    # print("www.cisco.com".lstrip("w.")) # cisco.com
    # only the leading character and whitespaces
    # print("pythoninstitute.org".lstrip(".org")) # pythoninstitute.org
    # print("pythoninstitute.org".lstrip("python"))   # institute.org

# replace()
    # takes two arguments
    # returns a new string in which all the occurences of the first arg are replaced with the second arg
    # print("www.netacad.com".replace("netacad.com", "pythoninstitute.org"))  # www.pythoninstitute.org
    # print("This is it!".replace("is", "are"))   # Thare are it!
    # print("Apple juice".replace("juice", ""))   # Apple
    # print("Apple juice".replace("", "juice"))   # juiceAjuicepjuicepjuiceljuiceejuice juicejjuiceujuiceijuicecjuiceejuice
    # print("Apple juice".replace(" ", "juice"))  # Applejuicejuice
# the three parameter version uses third argument to limit the num of replacements
    # print("This is it!".replace("is", "are", 1))    # Thare is it!
    # print("This is it!".replace("is", "are", 2))    # Thare are it!

# rfind()
    # it starts the searches from the right to left, thats why r
    # print("tau tau tau".rfind("ta"))        # index 9
    # print("tau tau tau".rfind("ta", 9))     # -1 (when not found)
    # print("tau tau tau".rfind("ta", 3, 9))  # index 4
        # s[3:9]: " tau t" (indices 3, 4, 5, 6, 7, 8), doesnt include the end index, 9 in this case

# rstrip()  (the opposite of lstrip > rightstrip)
    # print("[" + " upsilon ".rstrip() + "]") # [ upsilon]
    # print("cisco.com".rstrip(".com"))
        # The .rstrip() method treats its argument as a set of individual characters to strip, 
        # not as a literal word or substring sequence. When you pass ".com" to .rstrip(), 
        # Python interprets it as: "Keep removing any character from the right end as long as it matches '.', 'c', 'o', or 'm'."
        # 's' doesnt match so it stops at s and returns cis

# split()
    # splits the string and builds a list of detected substrings.
    # uses whitespace as delimiter but doesnt include them
    # if the string is empty, it returns an empty list
    # print("phi       chi\npsi".split()) # ['phi', 'chi', 'psi']

# startswith()
    # opposite of endswith()
    # checks if the string starts with the specified substring
    # print("omega".startswith("meg"))    # False
    # print("omega".startswith("om"))     # True

# strip()
    # combination of lstrip() and rstrip()
    # makes a new string lacking all leading and trailing whitespaces
    # print("[" + "   aleph   ".strip() + "]")    # [aleph]

# swapcase()
    # returns a new string swapping the cases of all the letters
    # lower to upper and vice versa
    # other characters remain untouched
    # print("I know that I know nothing.".swapcase())   # i KNOW THAT i KNOW NOTHING.

# title()
    # changes every words first letter to upper-case
    # and all the other ones to lower-case
    # print("I knoW thAT I knOW nothINg. Part 1.".title())    # I Know That I Know Nothing. Part 1.

# upper()
    # returns a new string with all upper-case replacements
    # print("I know that I know nothing. Part 2.".upper())

# Quiz 2
    # s1 = 'Where are the snows of yesteryear?'
    # s2 = s1.split()
    # print(s2)
    # print(s2[-2])

# Quiz 4
    # s = 'It is either easy or impossible'
    # s = s.replace('easy', 'hard').replace('im', '')
    # print(s)

