#!/usr/bin/python3
"""
Module 6-square
Defines a class Square that represents a square with a given size and position.
"""


class Square:
    """
    Represents a square.
    Attributes:
        __size (int): The size of the square (private).
        __position (tuple): The position of the square (private),
        represented as (x, y).
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a square with a given size and position.
        Args:
            size (int): The size of the square. Defaults to 0.
            position (tuple): The position of the square as (x, y).
            Defaults to (0, 0).
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
            TypeError: If position is not a tuple of 2 positive integers.
        """
        self.size = size
        self.position = position
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Calculates and returns the area of the square.
        Returns:
            int: The area of the square.
        """
        return self.__size * self.__size

    @property
    def size(self):
        """
        Getter for the size attribute.
        Returns:
            int: The size of the square.
        """
        return self.__size

    @property
    def position(self):
        """
        Getter for the position attribute.
        Returns:
            tuple: The position of the square as (x, y).
        """
        return self.__position

    @size.setter
    def size(self, size):
        """
        Setter for the size attribute.
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

    @position.setter
    def position(self, position):
        """
        Setter for the position attribute.
        Args:
            position (tuple): The new position as (x, y).
        Raises:
            TypeError: If position is not a tuple of 2 positive integers.
        """
        if not isinstance(position, tuple) or len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(isinstance(n, int) and n >= 0 for n in position):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    def my_print(self):
        """
        Prints the square using the character '#'.
        If size is 0, it prints an empty line.
        The square is printed with the offset defined by position.
        """
        if self.size == 0:
            print("")
            return

        # Print empty lines defined by position[1]
        for _ in range(self.position[1]):
            print("")

        # Print the square with spaces and '#' characters
        for _ in range(self.size):
            print(" " * self.position[0] + "#" * self.size)
