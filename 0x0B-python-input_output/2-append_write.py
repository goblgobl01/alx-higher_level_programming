#!/usr/bin/python3
"""2-append_write python module."""


def append_write(filename="", text=""):
    """a function that append a string to the file."""
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
