#!/usr/bin/python3
"""10-square python module."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """the grand child class."""

    def __init__(self, size):
        """construcor of the square class."""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """return the area of the square."""
        return self.__size**2
