class MyList(list):
    """
MyList class that inherits
from list and provides a method to print sorted list.
"""

    def print_sorted(self):
        trie = sorted(self)
        print(trie)
