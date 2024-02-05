#!/usr/bin/python3
"""
is_kind_of_class:
  True if the object is an instance of, or if the object is an instance 
  of a class that inherited from, the specified class ; otherwise False.
"""


def is_kind_of_class(obj, a_class):
    """
    is_kind_of_class:
      True if the object is an instance of, or if the object is an instance 
      of a class that inherited from, the specified class ; otherwise False.
    parameters:
      - obj: the object to use in this function.
      - a_class: the class the instance could drived from.
    return:
      True or False.
    """
    if isinstance(obj, a_class):
        return True
    return False
