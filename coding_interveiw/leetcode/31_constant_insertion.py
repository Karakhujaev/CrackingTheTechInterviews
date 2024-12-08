import random

class RandomizedSet:

    def __init__(self):
        self.table_numbers = {}  # Dictionary to store the index of each value in `numbers`
        self.numbers = []        # List to store the values in the set

    def insert(self, val: int) -> bool:
        if val in self.table_numbers:
            return False
        # Add new value to `numbers` and update `table_numbers` with its index
        self.numbers.append(val)
        self.table_numbers[val] = len(self.numbers) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.table_numbers:
            return False

        # Get index of the element to remove
        index_to_remove = self.table_numbers[val]
        last_element = self.numbers[-1]

        # Move the last element to the position of the element to remove
        self.numbers[index_to_remove] = last_element
        self.table_numbers[last_element] = index_to_remove

        # Remove the last element and update `table_numbers`
        self.numbers.pop()
        del self.table_numbers[val]
        return True

    def getRandom(self) -> int:
        # Randomly select an element from the list
        return random.choice(self.numbers)
