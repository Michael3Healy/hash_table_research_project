# Implementation of quadratic probing hash table

from .base_hash_table import BaseHashTable

class QuadraticProbingHashTable(BaseHashTable):

    def is_prime(self, n):
        if n < 2:
            return False
        for i in range(2, n):
            if n % i == 0:
                return False
        return True 

    def __init__(self, capacity):
        super().__init__(capacity)
        if self.is_prime(capacity) != True:
            raise ValueError("Table capacity must be a prime number")

    def _probe_index(self, key, attempt):

        # Returns new index to try by adding the initial hashed index to the squared number of attempts and using modulo division on it using the table capacity
        initial_index = key % self.capacity
        return (initial_index + attempt ** 2) % self.capacity

    def insert(self, key, value):
        if self.get_load_factor() > 0.5:
            raise ValueError("Table is already at 50% load factor")
        else:
            return super().insert(key, value)
    