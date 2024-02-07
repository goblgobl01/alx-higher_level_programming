#!/usr/bin/python3
"""9-student.py python module"""


class Student:
    """A class that defines a student."""

    def __init__(self, first_name, last_name, age):
        """The class constructor."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Return a dictionary representation of the
        attributes of this class with considration for attrs.
        """
        if attrs is None:
            return {'first_name': self.first_name,
                    'last_name': self.last_name, 'age': self.age}
        else:
            dict = {}
            for attributes in attrs:
                if attributes not in self.__dict__:
                    continue
                dict[attributes] = getattr(self, attributes)
            return dict

    def reload_from_json(self, json):
        """
        a simple way desirialize json data.
        """
        for key, value in json.items():
            setattr(self, key, value)
