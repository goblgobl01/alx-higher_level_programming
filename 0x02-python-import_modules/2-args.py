#!/usr/bin/python3

if __name__ == "__main__":
    """Print the number of and list of arguments."""
    import sys
    variable = sys.argv
    if len(variable) == 1:
        print("{} arguments.".format(len(variable) - 1))

    else:
        print("{} arguments:".format(len(variable) - 1))
        for i in range(1, len(variable)):
            print("{}: {}".format(i, variable[i]))
