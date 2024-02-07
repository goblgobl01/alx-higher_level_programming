#!/usr/bin/python3
"""5-save_to_json python module"""


def save_to_json_file(my_obj, filename):
    """a funciton that write json representation of data type to a file."""
    with open(filename, "w", encoding="utf-8") as file:
        import json
        json.dump(my_obj, file)
