# Implementation of double hashing hash table

from .base_hash_table import BaseHashTable

class DoubleHashingHashTable(BaseHashTable):

    def is_prime(self, n):
        if n < 2:
            return False
        for i in range(2, n):
            if n % i == 0:
                return False
        return True 

    def __init__(self, capacity):
        super().__init__(capacity)

        # Make sure table capacity is prime because that helps with reducing repeated patterns when probing
        if self.is_prime(capacity) != True:
            raise ValueError("Table capacity must be a prime number")

    # Method implemented by each collision resolution strategy individually to calculate next candidate index after collision
    def _probe_index(self, key, attempt):

        initial_index = key % self.capacity

        # Number of indices after the initial one that the calculation will skip to based on the key
        step_size = 1 + (key % (self.capacity - 1))

        # New candidate index based on step size, initial index, capacity, and attempt number
        secondary_hash_index = (initial_index + attempt * step_size) % self.capacity

        return secondary_hash_index

    def insert(self, key, value):
        if self.get_load_factor() > 0.5:
            raise ValueError("Table is already at 50% load factor")
        else:
            return super().insert(key, value)
    