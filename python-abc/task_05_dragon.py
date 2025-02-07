#!/usr/bin/python3
"""
Module defining a Dragon class using mixins for swimming and flying.
"""


class SwimMixin:
    """
    Mixin that provides swimming ability.
    """
    def swim(self):
        """
        Prints a message indicating the creature is swimming.
        """
        print("The creature swims!")


class FlyMixin:
    """
    Mixin that provides flying ability.
    """
    def fly(self):
        """
        Prints a message indicating the creature is flying.
        """
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
    A Dragon class that can swim, fly, and roar.
    """
    def roar(self):
        """
        Prints a message indicating the dragon is roaring.
        """
        print("The dragon roars!")
