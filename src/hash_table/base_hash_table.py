"""Base interface and shared behavior for all open-addressing hash table variants.

Planned contents for this file:
- shared constructor for table capacity, load factor, and collision metadata
- common helper methods for hashing and slot validation
- abstract or base methods for insert, lookup, and delete if needed
- probe counting and statistics tracking
- support for table occupancy calculations and resizing safeguards
- common validation rules shared across implementations

This module should define the contract each strategy follows, without implementing any specific collision strategy.
"""

# 1. BaseHashTable class definition
# 2. table state and slot representation
# 3. hash function interface
# 4. insert and lookup contract
# 5. probe statistics tracking
# 6. validation and occupancy helpers

# References: https://www.geeksforgeeks.org/dsa/program-to-implement-hash-table-using-open-addressing/


class HashNode:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value

# Constants
capacity = 20
size = 0

# Array for HashNode
arr = [None] * capacity

# Dummy node
dummy = HashNode(-1, -1)

# Function to add key value pair
def insert(key: int, value: int):
    global size
    temp = HashNode(key, value)

    # Apply hash function to find index for given key
    hash_index = key % capacity
    
    # Find next free space
    while arr[hash_index] is not None and arr[hash_index].key != key and arr[hash_index].key != -1:
        hash_index += 1
        hash_index %= capacity
    
    # If new node to be inserted increase the current size
    if arr[hash_index] is None or arr[hash_index].key == -1:
        size += 1
    
    arr[hash_index] = temp

# Function to delete a key value pair
def delete_key(key: int):
    global size
    hash_index = key % capacity

    # Finding the node with given key
    while arr[hash_index] is not None:
        # if node found
        if arr[hash_index].key == key:
            # Insert dummy node here for further use
            arr[hash_index] = dummy
            
            # Reduce size
            size -= 1
            
            # Return the value of the key
            return 1
        hash_index += 1
        hash_index %= capacity
    
    # If not found return null
    return 0

# Function to search the value for a given key
def find(key: int):
    global size
    hash_index = key % capacity
    counter = 0
    
    # Find the node with given key
    while arr[hash_index] is not None:
        if counter > capacity:
            break
        
        # If node found return its value
        if arr[hash_index].key == key:
            return arr[hash_index].value
        
        hash_index += 1
        hash_index %= capacity
        counter += 1
    
    # If not found return -1
    return -1

# Driver code
if __name__ == "__main__":
    # Space allocation
    insert(1, 5)
    insert(2, 15)
    insert(3, 20)
    insert(4, 7)
    if find(4) != -1:
        print("Value of Key 4 = ", find(4))
    else:
        print("Key 4 does not exists")
    
    if delete_key(4):
        print("Node value of key 4 is deleted successfully")
    else:
        print("Key does not exists")
    
    if find(4) != -1:
        print("Value of Key 4 = ", find(4))
    else:
        print("Key 4 does not exists")

