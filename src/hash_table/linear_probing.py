# Implementation of linear probing strategy

from src.hash_table.base_hash_table import BaseHashTable

class LinearProbingHashTable(BaseHashTable):
    """
    OPEN ADDRESSING HASH TABLE USING LINEAR PROBING.
    PROBE SEQUENCE:
        H(K)
        H(K) + 1
        H(K) + 2
        H(K) + 3
        ...
        
    MOD TABLE CAPACITY 
    """
    def _probe_index( self, key, attempt ):
        hash_idx = key % self.capacity
        return ( hash_idx + attempt ) % self.capacity
    