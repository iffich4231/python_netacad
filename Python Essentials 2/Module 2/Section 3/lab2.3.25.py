
def mysplit(str):
    if str == "" or str.isspace():
        return
    lst = []
    word = ""
    for char in str:
        if char == " ":
            if word:
                lst.append(word)
                word = ""
        else:
            word += char
    if word:
        lst.append(word)
    return lst

print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))