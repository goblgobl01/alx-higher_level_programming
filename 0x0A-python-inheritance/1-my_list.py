#!/usr/bin/python3

class MyList(list):
    """
    MyList is a custom subclass of the built-in list class in Python.

    Attributes:
        Inherits all attributes from the list class.

    Methods:
        print_sorted():
            Prints the elements of the list in sorted order.

    Example Usage:
        my_list = MyList([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5])
        my_list.print_sorted()
        # Output: [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]
    """
    def print_sorted(self):
        """
        Print the elements of the list in sorted order.

        Returns:
            None
        """
        print(sorted(self))
