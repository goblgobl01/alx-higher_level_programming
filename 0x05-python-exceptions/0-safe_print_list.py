#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    count = 0

    for i in my_list:
        if count == x:
            break
        else:
            try:
                print("{:d}".format(i))
                count += 1
            except:
                print("unknown error")

