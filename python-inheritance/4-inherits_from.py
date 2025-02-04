#!/usr/bin/python3
def inherits_from(obj, a_class):

    """
    Returns True if obj is an instance of a subclass of a_class, else False.
    """
    recup = type(obj)
    if (
        isinstance(obj, a_class) and
        issubclass(recup, a_class) and
        type(obj) is not a_class
    ):
        return True
    else:
        return False
