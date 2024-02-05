#!/usr/bin/python3
"""a empty class."""


class BaseGeometry:
    """a empty class"""
    def area(self):
        """raise a exeption."""
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        """valide Value."""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
