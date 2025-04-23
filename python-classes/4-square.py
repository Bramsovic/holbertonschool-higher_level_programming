#!/usr/bin/python3
"""
Module 4-square
Defines a class Square with a private attribute size,
a public method to calculate area,
and properties to access and update size with validation.
"""


class Square:
    """
    Represents a square.
    Attributes:
        __size (int): The size of the square (private).
    """
    def __init__(self, size=0):
        """
        Initializes a square with an optional size.

        Args:
            size (int): The size of the square. Defaults to 0.
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size * self.__size

    @property
    def size(self):
        """
        Getter for size.
        Returns:
            int: The current size of the square.
        """
        return self.__size

    @size.setter
    def size(self, size):
        """
        Setter for size.
        Validates and sets the size of the square.
        Args:
            size (int): The new size of the square.
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        
    def my_print(self):
        """
        Prints the square with the character '#' or a blank line if size is 0.
        """
        if self.__size == 0:
            print("")  
        else:
            for _ in range(self.__size):
                print("#" * self.__size)  
