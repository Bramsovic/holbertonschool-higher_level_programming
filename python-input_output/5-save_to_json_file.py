#!/usr/bin/python3
"""
    Module that writes an object to a text file in JSON format
"""
import json


def save_to_json_file(my_obj, filename):
    """Writes an object to a text file using
    JSON representation.
    Args:
        my_obj (any): The object to serialize and save.
        filename (str): The name of the file to write to.
    """
    with open(filename, "w") as f:
        json.dump(my_obj, f)
