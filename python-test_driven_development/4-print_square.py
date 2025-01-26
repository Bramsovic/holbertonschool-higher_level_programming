#!/usr/bin/python3
def print_square(size):
    """
    Print a square with the character #.

    Args:
        size (int): The size of the square (must be >= 0).

    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if isinstance(size, int) and size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float):
        raise TypeError("size must be an integer")
    for _ in range(size):
        print("#" * size)
