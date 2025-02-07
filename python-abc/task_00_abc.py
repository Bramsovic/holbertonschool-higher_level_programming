#!/usr/bin/env python3

from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Abstract class representing an animal.
    Enforces the implementation of the
    `sound()` method in subclasses.
    """

    @abstractmethod
    def sound(self):
        """Must be implemented by subclasses to
        return the animal's sound."""
        pass


class Dog(Animal):
    """Dog class implementing
    the `sound()` method."""

    def sound(self):
        """Returns 'Bark'."""
        return "Bark"


class Cat(Animal):
    """Cat class implementing the `sound()` method."""

    def sound(self):
        """Returns 'Meow'."""
        return "Meow"
