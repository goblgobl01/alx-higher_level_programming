#!/usr/bin/python3
""" a class that define a rectangle """


class Rectangle:
    """a class that define a rectangle"""
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """return the width"""
        return self.__width

    @property
    def height(self):
        """return the height"""
        return self.__height

    @width.setter
    def width(self, value):
        """this is a setter for the private attribute __width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """this is a setter for the private attribute __height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
