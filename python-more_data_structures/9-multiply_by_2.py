#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    b_dictionary = a_dictionary.copy()
    for index in b_dictionary:
        b_dictionary[index] *= 2
    return b_dictionary
