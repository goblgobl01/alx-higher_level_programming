#!/usr/bin/python3
"""6-load_from_json_file.py python module."""


def load_from_json_file(filename):
    """a function that turn text file data to its orginal form."""
    with open(filename, "r", encoding="utf-8") as file:
        import json
        return json.load(file)
