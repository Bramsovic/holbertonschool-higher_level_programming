#!/usr/bin/python3
"""
This module provides a function to add two integers or floats.

The function ensures type validation for the inputs.
If floats are provided, they are truncated to integers
before performing the addition.The result is always an integer.
"""


def add_integer(a, b=98):
    """
    Add two integers or floats as integers.

    Floats are truncated to integers before addition.
    Returns the result as an integer.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return a + b
