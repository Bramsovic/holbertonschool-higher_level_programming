#!/usr/bin/python3
"""
Module for BaseGeometry class.
"""


class BaseGeometry:
    """
    Base class for geometric operations.
    """
    def area(self):
        """
        Raises an exception indicating that the method is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that value is a positive integer.
        Args:
            name (str): The name of the value.
            value (int): The value to validate.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """
    Represents a rectangle using BaseGeometry.
    """
    def __init__(self, width, height):
        """
        Initializes a rectangle with validated width and height.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
