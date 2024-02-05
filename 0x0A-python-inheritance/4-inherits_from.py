#!/usr/bin/python3
"""
inherits_from:
  True if the object is an instance of, or if the object is an instance
  of a class that inherited from, the specified class ; otherwise False.
"""


def inherits_from(obj, a_class):
    """
    inherits_from:
      True if the object is an instance of, or if the object is an instance
      of a class that inherited from, the specified class ; otherwise False.
    parameters:
      - obj: the object to use in this function.
      - a_class: the class the instance could drived from.
    return:
      True or False.
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class

