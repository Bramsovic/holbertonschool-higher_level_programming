#!/usr/bin/python3
"""
    Module to read file
"""


def read_file(filename=""):
    """Reads a text file (UTF-8) and prints its content to stdout.

    Args:
        filename (str): The path of the file to read.
        Defaults to an empty string.
    """
    with open(filename, "r", encoding="utf-8") as f:
        contenu = f.read()
        print(contenu, end="")
