#!/usr/bin/python3
"""
    Module that returns a Python data structure from a JSON string.
"""
import json


def from_json_string(my_str):
    """Converts a JSON string to a Python object.
    Args:
        my_str (str): The JSON string to convert.

    Returns:
        any: The corresponding Python object.
    """
    convert = json.loads(my_str)
    return convert
