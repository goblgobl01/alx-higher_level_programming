#!/usr/bin/python3

def uppercase(str):
    length = len(str)
    new_string = ""
    for i in range(length):
        if ord(str[i]) - 97 >= 0:
            new_string = new_string + (chr((ord(str[i]) - 97) + 65))
        else:
            new_string = new_string + (str[i])

    print(new_string.format(), end = "\n")
