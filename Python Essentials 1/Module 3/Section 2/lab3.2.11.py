# PRETTY VOWEL EATER

string = input("Enter a word: ")
string = string.lower()
new_string = ""

for char in string:    
    if char == "a": continue
    elif char == "e": continue
    elif char == "i": continue
    elif char == "o": continue
    elif char == "u": continue
    else: new_string += char.upper()

print(new_string)