#!/usr/bin/python3
"""A module for square"""


class Square:
    """this is the square class documentation """
    def __init__(self, size=0):
        """this si the constructor part of the class we
        Args:
            size: the value to assign to the private attribute
            __size: a private attribute of a instance
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """this is Method that return the private value
        Return: the area of the square
        """
        return self.__size*self.__size

    @property
    def size(self):
        """this is Method that return the private value
        Return: the size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """this is Method that return the private value
        Args:
            value: is the new value to assign to the private size
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        """print the square with the # character"""
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print("")
