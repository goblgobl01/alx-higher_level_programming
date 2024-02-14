#!/usr/bin/python3
"""base python module."""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """return the json representation of dictionary."""
        if not list_dictionaries:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
