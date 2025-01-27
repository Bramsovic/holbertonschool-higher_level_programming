#!/usr/bin/python3
"""
Module 1-square
Defines a class Square with a private instance attribute 'size'.
"""


class Square:
    """
    Represents a square.
    Attributes:
        __size (int): The size of the square (private).
    """

    def __init__(self, size):
        """
        Initializes a square with a given size.
        Args:
            size (int): The size of the square.
        """
        self.__size = size
