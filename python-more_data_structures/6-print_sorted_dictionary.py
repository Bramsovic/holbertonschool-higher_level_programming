#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    key = sorted(a_dictionary.keys())
    for index in key:
        print("{}: {}".format(index, a_dictionary[index]))
