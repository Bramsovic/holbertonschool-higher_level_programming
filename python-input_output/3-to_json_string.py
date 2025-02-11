#!/usr/bin/python3
"""
    Module that returns the JSON representation of an object (string):
"""

import json


def to_json_string(my_obj):
    """Converts a Python object to a JSON string.
    Args:
        my_obj (any): The object to convert to JSON.
    Returns:
        str: The JSON string representation of the object.
    """
    convert = json.dumps(my_obj)
    return convert
