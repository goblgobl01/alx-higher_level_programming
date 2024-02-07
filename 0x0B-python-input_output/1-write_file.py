#!/usr/bin/python3
"""1-write_file python module"""


def write_file(filename="", text=""):
    """a function that write to a file."""
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
