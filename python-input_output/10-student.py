#!/usr/bin/python3
"""
    Module class
"""


class Student:
    """Defines a Student with first name, last name, and age."""

    def __init__(self, first_name, last_name, age):
        """Initializes a Student instance.
        Args:
            first_name (str): The student's first name.
            last_name (str): The student's last name.
            age (int): The student's age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns the dictionary representation of the Student instance.
        If `attrs` is a list of strings, only the specified attributes
        are retrieved. Otherwise, all attributes are included.
        Args:
            attrs (list, optional): List of attribute names to retrieve.
        Returns:
            dict: The dictionary containing the student's attributes.
        """
        if attrs is None:
            return self.__dict__
        elif (
            isinstance(attrs, list)
            and all(isinstance(element, str) for element in attrs)
        ):
            return {
                key: value
                for key, value in self.__dict__.items()
                if key in attrs
            }
