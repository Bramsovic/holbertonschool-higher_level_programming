#!/usr/bin/env python3
"""
Module for basic JSON serialization and deserialization.
Provides functions to save a Python dictionary as a JSON file
and to load a dictionary from a JSON file.
"""


import json


def serialize_and_save_to_file(data, filename):
    """
    Save a dictionary as a JSON file.
    Args:
        data (dict): Dictionary to serialize.
        filename (str): Output JSON file.
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


def load_and_deserialize(filename):
    """
    Load a dictionary from a JSON file.
    Args:
        filename (str): JSON file to read.
    Returns:
        dict: Deserialized dictionary.
    """
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
