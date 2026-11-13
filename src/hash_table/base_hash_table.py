
# Base interface and shared behavior for linear probing, quadratic probing, and double hashing.

# Node that will store value at idx determined by key, hash function, and collision strategy
class HashNode:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value

class BaseHashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.slot_array = [None] * capacity
        self.deleted_marker = HashNode(-1, -1)
        self.last_probe_count = 0

    # Implemented by subclasses with the appropriate collision resolution strategy
    def _probe_index(self, key, attempt):
        raise NotImplementedError

    def get_load_factor(self):
        return self.size / self.capacity

    # Inserts element into hash table. Calls strategy-specific probe index function if there is a collision
    def insert(self, key, value):

        # Set probe count to 0 so that probes can measured for THIS call alone. Caller needs to read last_probe_count immediately after execution before calling another method
        self.last_probe_count = 0

        # Hash function
        idx = key % self.capacity

        # If there isn't anything at that index, insert the new node there
        if self.slot_array[idx] is None:
            self.last_probe_count += 1
            self.slot_array[idx] = HashNode(key, value)
            self.size += 1
            return True
        else:
            self.last_probe_count += 1
            i = 1

            # For as many possible locations there are, use collision strategy to find next open index and assign there or return False
            while i <= self.capacity:
                candidate_idx = self._probe_index(key, i)
                if self.slot_array[candidate_idx] is None or self.slot_array[candidate_idx] == self.deleted_marker:
                    self.last_probe_count += 1
                    self.slot_array[candidate_idx] = HashNode(key, value)
                    self.size += 1
                    return True
                elif self.slot_array[candidate_idx].key == key:
                    self.last_probe_count += 1
                    self.slot_array[candidate_idx] = HashNode(key, value)
                    return True
                else:
                    self.last_probe_count += 1
                    i += 1
            return False

            

    # Find value from key. Returns HashNode or False if it doesn't exist
    def find(self, key):

        # Set probe count to 0 so that probes can measured for THIS call alone. Caller needs to read last_probe_count immediately after execution before calling another method
        self.last_probe_count = 0
        hash_idx = key % self.capacity

        # Return false immediately if HashNode doesn't exist at the hashed index
        if self.slot_array[hash_idx] == None:
            self.last_probe_count += 1
            return False
        elif self.slot_array[hash_idx].key == key:
            self.last_probe_count += 1
            return self.slot_array[hash_idx]
        else:
            self.last_probe_count += 1
            i = 1
            while i <= self.capacity:
                candidate_idx = self._probe_index(key, i)
                if self.slot_array[candidate_idx] is None:
                    self.last_probe_count += 1
                    return False
                elif self.slot_array[candidate_idx].key == key:
                    self.last_probe_count += 1
                    return self.slot_array[candidate_idx]
                else:
                    self.last_probe_count += 1
                    i += 1
            return False


    # Deletes value from key
    def delete(self, key):

        # Set probe count to 0 so that probes can measured for THIS call alone. Caller needs to read last_probe_count immediately after execution before calling another method
        self.last_probe_count = 0

        hash_idx = key % self.capacity
        if self.slot_array[hash_idx] is None:
            self.last_probe_count += 1
            return False
        elif self.slot_array[hash_idx].key == key:
            self.last_probe_count += 1
            self.slot_array[hash_idx] = self.deleted_marker
            self.size -= 1
            return True
        else:
            self.last_probe_count += 1
            # Use probing strategy to check other indices for key and delete there
            i = 1
            while i <= self.capacity:
                candidate_idx = self._probe_index(key, i)
                if self.slot_array[candidate_idx] is None:
                    self.last_probe_count += 1
                    return False
                elif self.slot_array[candidate_idx].key == key:
                    self.last_probe_count += 1
                    self.slot_array[candidate_idx] = self.deleted_marker
                    self.size -= 1
                    return True
                else:
                    self.last_probe_count += 1
                    i += 1
            return False
            
