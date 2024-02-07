#!/usr/bin/python3
"""7-add_item.py python module."""


import sys
import os
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


argument = sys.argv
filename = "add_item.json"


if os.path.isfile(filename):
    old_list = load_from_json_file(filename)
    all_the_arguments = old_list + argument[1:]
    save_to_json_file(all_the_arguments, "add_item.json")
else:
    save_to_json_file(argument[1:], "add_item.json")
