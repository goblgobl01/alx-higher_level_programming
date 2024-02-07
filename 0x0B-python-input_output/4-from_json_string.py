#!/usr/bin/python3
"""4-from_json... python module."""


def from_json_string(my_str):
    """a function that turn a sting to its true data form."""
    import json
    return json.loads(my_str)
