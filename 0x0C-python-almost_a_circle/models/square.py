#!/usr/bin/python3
"""square python module."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """a class that define a square."""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """return a simple string"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
