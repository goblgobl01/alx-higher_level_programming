#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    list = sorted(a_dictionary)
    for i in list:
        print("{0}: {1}".format(i, a_dictionary[i]))
