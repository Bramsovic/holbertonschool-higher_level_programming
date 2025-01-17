#!/usr/bin/python3

from sys import argv

if __name__ == "__main__":
    argv = argv[1:]
    argc = len(argv)
    count = 0

    if argc == 0:
        print("{}".format(0))
    else:
        for arg in argv:
            count += int(arg)
        print("{}".format(count))
