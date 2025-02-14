#!/usr/bin/env python3
"""
Module for serializing and deserializing a custom Python object.
This module defines the CustomObject class, which includes:
- Serialization of an instance to a file using pickle.
- Deserialization of an instance from a file.
- A display method to print the object's attributes.
"""


import pickle


class CustomObject:
    """Represents a custom object with name, age,
    and student status."""

    def __init__(self, name, age, is_student):
        """
        Initialize a CustomObject instance.

        Args:
            name (str): The name of the person.
            age (int): The age of the person.
            is_student (bool): Whether the person is a student.
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def serialize(self, filename):
        """
        Serialize the object and save it to a file.
        Args:
            filename (str): The file where the object will be stored.
        """
        with open(filename, "wb") as f:
            pickle.dump(self, f)

    @classmethod
    def deserialize(cls, filename):
        """
        Deserialize an object from a file.
        Args:
            filename (str): The file to load the object from.
        Returns:
            CustomObject: The deserialized object.
        """
        with open(filename, "rb") as f:
            return pickle.load(f)

    def display(self):
        """Print the object's attributes."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")
