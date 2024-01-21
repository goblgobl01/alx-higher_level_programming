#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    variable = sys.argv
    if len(variable) == 1:
        print("{} arguments.".format(len(variable) - 1))
    elif len(variable) == 2:
        print("{} arguments:".format(len(variable) - 1))
        print("{}: {}".format(1, variable[1]))
    else:
        print("{} arguments:".format(len(variable) - 1))
        for i in range(1, len(variable)):
            print("{}: {}".format(i, variable[i]))
