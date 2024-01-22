#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    variable = sys.argv[1:]
    result = 0
    for i in variable:
        result = result + int(i)

    print(result)
