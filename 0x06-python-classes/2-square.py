#!/usr/bin/python3
"""A module for square"""


class Square:
    """this is the square class documentation """
    def __init__(self, size=0):
        """this si the constructor part of the class we
        Args:
            __size: a private attribute of a instance
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
