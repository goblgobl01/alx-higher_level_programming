#!/usr/bin/python3

def add_integer(a, b=98):
    """add_integer a funciton that add two integers"""

    if (type(a) != float and type(a) != int):
        raise TypeError("a must be an integer")
    if (type(b) != float and type(b) != int):
        raise TypeError("b must be an integer")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return a + b
