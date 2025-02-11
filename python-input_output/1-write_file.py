#!/usr/bin/python3
def write_file(filename="", text=""):
    """Writes a string to a text file (UTF-8) and returns
    the number of characters written.
    Args:
        filename (str): The path of the file to write.
        Defaults to an empty string.
        text (str): The text to write into the file.
        Defaults to an empty string.
    Returns:
        int: The number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        nb_characters = f.write(text)
        return nb_characters
