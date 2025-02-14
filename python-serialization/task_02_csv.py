#!/usr/bin/env python3
"""
Module for converting CSV data to JSON.
This module defines a function to read a CSV file,
convert its content
into a JSON format, and save the output in 'data.json'.
Functions:
- convert_csv_to_json(csv_filename): Converts a CSV
file into a JSON file.
"""


import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Convert a CSV file to a JSON file.
    Reads a CSV file, converts its rows into a list of dictionaries,
    and writes the data to 'data.json' in a structured JSON format.
    Args:
        csv_filename (str): The name of the CSV file to read.
    Returns:
        bool: True if conversion was successful,
        False if the file was not found.
    """
    try:
        with open(csv_filename, mode="r", newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            data = list(reader)

        with open("data.json", mode="w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

        return True

    except FileNotFoundError:
        return False
