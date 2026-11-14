"""Simple checks to make sure a hash table is working correctly.

The main validation function uses a new, empty hash table and a list
of unique keys from one of the workload generators.
"""


def check_insertions(table, keys):
    """Insert each key and make sure the insert operation succeeds."""
    for key in keys:
        # Using the key as the value makes lookups easy to check later.
        if not table.insert(key, key):
            return False

    return True


def check_lookups(table, keys):
    """Check that every inserted key returns the correct node."""
    for key in keys:
        result = table.find(key)

        # The project's find() method returns False for missing keys.
        if result is False:
            return False

        if result.key != key or result.value != key:
            return False

    return True


def check_missing_key(table, missing_key):
    """A key that was never inserted should not be found."""
    return table.find(missing_key) is False


def check_occupancy(table):
    """Compare the table's size and load factor to its actual contents."""
    if table.capacity <= 0 or len(table.slot_array) != table.capacity:
        return False

    count = 0
    found_keys = set()

    for node in table.slot_array:
        # Empty slots and deleted slots do not count as occupied.
        if node is None or node is table.deleted_marker:
            continue

        if node.key in found_keys:
            return False

        found_keys.add(node.key)
        count += 1

    if count != table.size:
        return False

    expected_load = count / table.capacity
    return abs(table.get_load_factor() - expected_load) < 0.000001


def validate_hash_table(table, keys):
    """Run the basic checks on a new table and return the results.

    The table should be empty before this function is called.
    This function inserts the keys into that table.
    """
    if table.size != 0:
        raise ValueError("The hash table must be empty before validation")

    if len(keys) != len(set(keys)):
        raise ValueError("The test keys must be unique")

    if len(keys) > table.capacity:
        raise ValueError("There are more keys than table slots")

    inserted = check_insertions(table, keys)
    lookups = check_lookups(table, keys)

    # The generated keys are integers, so this key is not in the list.
    missing_key = max(keys, default=0) + 1
    missing = check_missing_key(table, missing_key)

    occupancy = check_occupancy(table) and table.size == len(keys)

    return {
        "insertions": inserted,
        "lookups": lookups,
        "missing_key": missing,
        "occupancy": occupancy,
        "passed": inserted and lookups and missing and occupancy,
    }
