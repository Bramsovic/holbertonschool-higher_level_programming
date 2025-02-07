#!/usr/bin/env python3


class Fish:
    """
    Represents a fish with swimming ability and water habitat.
    """

    def swim(self):
        """
        Prints a message indicating the fish is swimming.
        """
        print("The fish is swimming")

    def habitat(self):
        """
        Prints the habitat of the fish.
        """
        print("The fish lives in water")


class Bird:
    """
    Represents a bird with flying ability and sky habitat.
    """

    def fly(self):
        """
        Prints a message indicating the bird is flying.
        """
        print("The bird is flying")

    def habitat(self):
        """
        Prints the habitat of the bird.
        """
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """
    A fish that can both swim and fly, inheriting from Fish and Bird.
    """

    def swim(self):
        """
        Prints a message indicating the flying fish is swimming.
        """
        print("The flying fish is swimming!")

    def fly(self):
        """
        Prints a message indicating the flying fish is soaring.
        """
        print("The flying fish is soaring!")

    def habitat(self):
        """
        Prints the habitat of the flying fish.
        """
        print("The flying fish lives both in water and the sky!")
