#!/usr/bin/python3
"""square python module."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """a class that define a square."""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        self

    def __str__(self):
        """return a simple string"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """return the size"""
        return self.width

    @size.setter
    def size(self, value):
        """set the size"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value
