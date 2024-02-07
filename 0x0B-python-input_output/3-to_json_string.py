#!/usr/bin/python3
"""3-to_json... python module."""


def to_json_string(my_obj):
    """a function that return json representation of an object."""
    import json
    return json.dumps(my_obj)
