class VerboseList(list):
    """A custom list that prints notifications when modified."""

    def append(self, item):
        """Adds an item and prints a notification."""
        print(f"Added [{item}] to the list.")
        super().append(item)

    def extend(self, iterable):
        """Extends the list and prints a notification."""
        super().extend(iterable)
        print(f"Extended the list with [{len(iterable)}] items.")

    def remove(self, item):
        """Removes an item and prints a notification."""
        super().remove(item)
        print(f"Removed [{item}] from the list.")

    def pop(self, index=-1):
        """Pops an item and prints a notification."""
        item = super().pop(index)
        print(f"Popped [{item}] from the list.")
        return item
