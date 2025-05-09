#!/usr/bin/python3
"""Module defining a Rectangle class."""


class Rectangle:
    """Defines a rectangle with width and height."""

    def __init__(self, width=0, height=0):
        """Initialize a Rectangle with optional width and height."""
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    @property
    def width(self):
        """Retrieve the width of the rectangle."""
        return self.__width

    @property
    def height(self):
        """Retrieve the height of the rectangle."""
        return self.__height

    @width.setter
    def width(self, value):
        """Set the width of the rectangle,
        ensuring it's a non-negative integer."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """Set the height of the rectangle,
        ensuring it's a non-negative integer."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
