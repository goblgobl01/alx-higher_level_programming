#!/usr/bin/python3

if __name__ == "__main__":
    """this is a function that list the argument passed to it"""
    import sys
    variable = sys.argv
    if len(variable) == 1:
        print("{} arguments.".format(len(variable) - 1))

    else:
        print("{} arguments:".format(len(variable) - 1))
        for i in range(1, len(variable)):
            print("{}: {}".format(i, variable[i]))
