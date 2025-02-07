#!/usr/bin/python3

from abc import ABC, abstractmethod
import math

"""
Module for defining geometric shapes using abstract base classes.
"""


class Shape(ABC):
    """
    Abstract base class for geometric shapes.
    Defines the structure for area and perimeter methods.
    """
    @abstractmethod
    def area(self):
        """
        Computes and returns the area of the shape.
        Must be implemented by subclasses.
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        Computes and returns the perimeter of the shape.
        Must be implemented by subclasses.
        """
        pass


class Circle(Shape):
    """
    Circle class inheriting from Shape.
    Represents a circle with a given radius.
    """
    def __init__(self, radius):
        """
        Initializes a Circle with a given radius.
        Args:
            radius (float): The radius of the circle.
        """
        self.radius = radius

    def area(self):
        """
        Computes and returns the area of the circle.
        Returns:
            float: The area of the circle.
        """
        return math.pi * self.radius ** 2

    def perimeter(self):
        """
        Computes and returns the perimeter (circumference) of the circle.
        Returns:
            float: The perimeter of the circle.
        """
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """
    Rectangle class inheriting from Shape.
    Represents a rectangle with width and height.
    """
    def __init__(self, width, height):
        """
        Initializes a Rectangle with given width and height.
        Args:
            width (float): The width of the rectangle.
            height (float): The height of the rectangle.
        """
        self.width = width
        self.height = height

    def area(self):
        """
        Computes and returns the area of the rectangle.
        Returns:
            float: The area of the rectangle.
        """
        return self.width * self.height

    def perimeter(self):
        """
        Computes and returns the perimeter of the rectangle.
        Returns:
            float: The perimeter of the rectangle.
        """
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Prints the area and perimeter of a given shape using duck typing.
    Args:
        shape (Shape): An instance of a class implementing Shape.
    """
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
