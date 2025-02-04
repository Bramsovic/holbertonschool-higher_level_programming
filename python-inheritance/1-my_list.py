#!/usr/bin/python3
"""
Module for MyList class.
"""


class MyList(list):
    """
    A subclass of list that provides a method to
    print a sorted version of the list.
    """

    def print_sorted(self):
        """
        Prints the list in ascending sorted order
        without modifying the original list.
        """
        print(sorted(self))
