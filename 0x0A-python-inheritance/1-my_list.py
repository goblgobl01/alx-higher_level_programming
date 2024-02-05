#!/usr/bin/python3
"""a class that inherit from the list class."""


class MyList(list):
    """the list class sub class."""
    def print_sorted(self):
        """print a list in ascending order."""
        print(sorted(self))
