#!/usr/bin/python3
"""0-read_file.py module"""


def read_file(filename=""):
    """a function that read a file and print it to stdout."""
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            print(line, end="")
