# VOWEL EATER
string = input("Enter a single word: ")
string = string.lower()

for char in string:
    if char == "a": continue
    elif char == "e": continue
    elif char == "i": continue
    elif char == "o": continue
    elif char == "u": continue
    else:
        print(char.upper())