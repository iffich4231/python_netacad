# in python strings are immutable sequences
    # concatenation, replication and reassignments are legal as python creates a new object
    # in reassignment (s = s + "new_string/char") doesnt overwrite the s, rather builds a new object and assigns the s
    # to this new value. The older value is collected by pythons garbage collector if no longer referenced
    # strings have length (number of characters)
    # string can be empty and the length will be 0
    # a backslash to escape a character in not included in the length

    # # Example 1
    # word = 'by'
    # print(len(word))    # 2
    # # Example 2
    # empty = ''
    # print(len(empty))   # 0
    # # Example 3
    # i_am = 'I\'m'
    # print(len(i_am))    # 3

# Multi-line Strings
    # need 3 apostrophes or 3 quotes (trigraphs)
    # multiline = """Line #1
    # Line #2"""
    # multiline = '''Line #1
    # Line #2'''
    # print(len(multiline))   # 15 counts the whitespaces too, in this that is \n (new line char)
    # print(multiline)

# Operations on Strings
    # have their own set of permissible operations, although they are rather limited compared to numbers
    # in general can be concatenated(joined)(+) and replicated (*(not multiplication))
    # they always return a new string
    # The ability to use the same operator against completely different kinds of data (like numbers vs. strings)
    # is called overloading (as such an operator is overloaded with different duties).
    # += and *= also work on strings
    # str1 = 'a'
    # str2 = 'b'
    # # concatenation
    # print(str1 + str2)
    # print(str2 + str1)
    # # replication
    # print(5 * 'a')
    # print('b' * 4)

# ord()
    # ordinal, used to know a specific chars ASCII / Unicode code point value
    # char_1 = 'a'
    # char_2 = ' '  # space
    # print(ord(char_1))
    # print(ord(char_2))

# chr()
    # character, takes a code point and returs its char
    # print(chr(97))
    # print(chr(945))

# chr(ord(x)) == x
# ord(chr(x)) == x

# String as sequences
    # they arent lists, but can be treated like them in many particular cases
    # we can use indexing to access any of the strings chars
# Indexing strings.
    # the_string = 'silly walks'
    # for ix in range(len(the_string)):
    #     print(the_string[ix], end=' ')
    # print()
# Iterating strings
    # the_string = 'silly walks'
    # for character in the_string:
    #     print(character, end=' ')
    # print()

# Slices
    # alpha = "abdefg"
    # print(alpha[1:3])
    # print(alpha[3:])
    # print(alpha[:3])
    # print(alpha[3:-2])
    # print(alpha[-3:4])
    # print(alpha[::2])
    # print(alpha[1::2])

# in and not in operators
    # alphabet = "abcdefghijklmnopqrstuvwxyz"
    # print("f" in alphabet)
    # print("F" in alphabet)
    # print("1" in alphabet)
    # print("ghi" in alphabet)
    # print("Xyz" in alphabet)

    # print("f" not in alphabet)
    # print("F" not in alphabet)
    # print("1" not in alphabet)
    # print("ghi" not in alphabet)
    # print("Xyz" not in alphabet)

# we can use del on strings but it can only delete the string as a whole and wont work as del[index]
    # alphabet = "abcdefghijklmnopqrstuvwxyz"
    # del alphabet
    # print(alphabet)
# no appending
# no inserting
# this is acceptable
    # alphabet = "bcdefghijklmnopqrstuvwxy"
    # alphabet = "a" + alphabet
    # alphabet = alphabet + "z"
    # print(alphabet)

# verification that + , * and reassignment are legal and create new objects each time
# the id func reveals the memory address of an object
# s = "py"
# print(id(s))    # 140704272557608
# s = s + "thon"
# print(id(s))    # 1964089236080

# min()
    # finds the minimum element of the sequence (doesnt matter if string or list)
    # the sequence should not be empty
    # # Demonstrating min() - Example 1:
    # print(min("aAbByYzZ"))      # A because A has a lower ASCII code point
    # # Demonstrating min() - Examples 2 & 3:
    # t = 'The Knights Who Say "Ni!"'
    # print('[' + min(t) + ']')   # used square brackets to show space character
    # t = [0, 1, 2]               # 0
    # print(min(t)) 

# # max()
    #     # finds the maximum element
    # # Demonstrating max() - Example 1:
    # print(max("aAbByYzZ"))      # z
    # # Demonstrating max() - Examples 2 & 3:
    # t = 'The Knights Who Say "Ni!"' 
    # print('[' + max(t) + ']')   # y
    # t = [0, 1, 2]               # 2
    # print(max(t))

# the index() method
    # not a function rather a method
    # always returns the first occurence it encounters
    # gives ValueError if no match
    # string.index(substring, start_index, end_index)
    # # Demonstrating the index() method:
    # print("aAbByYzZaA".index("b"))    # 2
    # print("aAbByYzZaA".index("Z"))    # 7
    # print("aAbByYzZaA".index("A"))    # 1
    # can also take a substring
        # text = "python programming"
        # print(text.index("gram"))  # Output: 10 (index of the FIRST character 'g')

# list()
    # takes a string and creates a list containing all the strings chars, one per element
    # print(list("abcabx"))

# count()
    # a method
    # counts all occurences of the element(char) inside the sequence
    # print("abcabc".count("b"))  # 2
    # print('abcabc'.count("d"))  # 0

for ch in "abc":
    print(chr(ord(ch) + 1), end='')