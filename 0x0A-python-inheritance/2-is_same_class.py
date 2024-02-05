#!/usr/bin/python3
"""
is_same_class:
  Returns True if the object is exactly an instance
  of the specified class ; otherwise False.
"""


def is_same_class(obj, a_class):
    """
    is_same_class:
      A function that returns True if the object is exactly
      an instance of the specified class ; otherwise False..
    parameters:
      - obj: the object to use in this function.
      - a_class: the class the instance could drived from.
    return:
      True or False.
    """
    return type(obj) is a_class
