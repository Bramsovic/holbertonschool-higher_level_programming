#!/usr/bin/python3

if __name__ == "__main__":

    from sys import argv

    argv = argv[1:]
    argc = len(argv)

    if argc == 0:
        print("{} arguments.".format(argc))
    elif argc == 1:
        print("{} argument:".format(argc))
    else:
        print("{} arguments:".format(argc))

    count = 1
    for arg in argv:
        print("{}: {}".format(count, arg))
        count += 1
