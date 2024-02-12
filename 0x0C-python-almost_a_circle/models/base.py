#!/usr/bin/python3
"""base python module."""


class Base:
    """base class i dont know what its for but ok"""
    __nb_objects = 0

    def __init__(self, id=None):
        """base constructor."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
