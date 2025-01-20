#!/usr/bin/python3
def no_c(my_string):
    newlist = ""
    for index in my_string:
        if index != "c" and index != "C":
            newlist += index
    return newlist
