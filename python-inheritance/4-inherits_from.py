#!/usr/bin/python3
"""
Module for inherits_from function.
"""


def inherits_from(obj, a_class):
    """
    Checks if obj is an instance of a subclass of a_class.
    """
    recup = type(obj)
    return (isinstance(obj, a_class)
            and issubclass(type(obj), a_class)
            and type(obj) is not a_class)
