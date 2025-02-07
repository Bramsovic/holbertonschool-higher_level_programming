#!/usr/bin/env python3

class CountedIterator(object):
    """
    Iterator wrapper that counts the
    number of items iterated.
    """

    def __init__(self, data):
        """
        Initializes the iterator and the count tracker.
        """
        self.iterator = iter(data)
        self.count = 0

    def __next__(self):
        """
        Returns the next item and increments the count.
        """
        try:
            result = next(self.iterator)
            self.count += 1
            return result
        except StopIteration:
            raise StopIteration

    def get_count(self):
        """
        Returns the number of items iterated.
        """
        return self.count
