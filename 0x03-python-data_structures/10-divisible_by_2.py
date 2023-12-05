#!/usr/bin/python3

def divisible_by_2(my_list=None):
    if my_list is None:
        my_list = []

    bool_list = my_list[:]
    for count, i in enumerate(my_list):
        bool_list[count] = i % 2 == 0
    return bool_list

def delete_at(my_list=None, idx=0):
    if my_list is None:
        my_list = []

    if 0 <= idx < len(my_list):
        del my_list[idx]

    return my_list

