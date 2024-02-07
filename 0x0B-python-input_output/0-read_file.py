#!/usr/bin/python3
"""0-read_file.py module"""


def read_file(filename=""):
    """a function that read a file and print it to stdout."""
    with open(filename, encoding="utf-8") as file:
        data = file.read()
        print(data)
