#!/usr/bin/python3
"""
Module defining the MyList class.
"""


class MyList(list):
    """
    A class that inherits from list and provides a
    method to print the list in sorted order.
    """
    def print_sorted(self):
        """
        Prints the list in ascending order without
        modifying the original list.
        """
        trie = sorted(self)
        print(trie)
