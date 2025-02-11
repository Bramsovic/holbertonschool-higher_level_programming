#!/usr/bin/python3
"""
    Module appends a string
"""


def append_write(filename="", text=""):
    """Appends a string to a text file (UTF-8)
    and returns the number of characters added.
    Args:
        filename (str): The path of the file to append to.
        Defaults to an empty string.
        text (str): The text to append to the file.
        Defaults to an empty string.
    Returns:
        int: The number of characters added.
    """
    with open(filename, "a", encoding="utf-8") as f:
        nb_characters_added = f.write(text)
        return nb_characters_added
