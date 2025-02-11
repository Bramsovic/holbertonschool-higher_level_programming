#!/usr/bin/python3
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
