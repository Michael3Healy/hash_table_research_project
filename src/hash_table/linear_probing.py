"""Linear probing implementation module.

Planned contents for this file:
- class representing the linear probing hash table
- insertion method that resolves collisions by stepping through successive slots
- lookup method that follows the same probe sequence
- probe counting logic for each access
- any strategy-specific state needed for correct rehashing or occupancy tracking

This file should only implement the behavior unique to linear probing.
"""

# File outline only: no implementation code.
# 1. LinearProbingHashTable class
# 2. probe sequence behavior
# 3. insert and lookup methods
# 4. statistics collection for the strategy
# 5. strategy-specific validation

from src.hash_table.base_hash_table import BaseHashTable

class LinearProbingHashTable(BaseHashTable):
    """
    OPEN ADDRESSING HASH TABLER USING LINEEAR PROBING.
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
    