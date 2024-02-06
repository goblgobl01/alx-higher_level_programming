#!/usr/bin/python3
"""a class that gonna inherit from the base geometry class."""

BaseGeometry = __import__('7-base_geometry').BaseGeometry
class Rectangle(BaseGeometry):
    """a class that gonna inherit from the base geometry class."""
    def __init__(self, width, height):
        """the construnctor that set the width and height."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
