#!/usr/bin/python3
import json


def load_from_json_file(filename):
    """Reads a JSON file and returns the
    corresponding Python object.
    Args:
        filename (str): The name of the file to read from.
    Returns:
        any: The deserialized Python object.
    """
    with open(filename, "r") as f:
        contenu = f.read()
    convert = json.loads(contenu)
    return convert
