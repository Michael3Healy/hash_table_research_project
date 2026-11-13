"""Common helpers for generating hash table workloads.

Our hash tables use key % table_size for the starting position.
Both workloads use the helpers in this file so the experiments
can use the same settings and output format.
"""



def check_inputs(table_size, num_keys):
    """Check that the requested workload can fit in the table."""
    if type(table_size) is not int or table_size < 1:
        raise ValueError("table_size must be a positive integer")

    if type(num_keys) is not int or num_keys < 0:
        raise ValueError("num_keys must be a non-negative integer")

    if num_keys > table_size:
        raise ValueError("num_keys cannot be larger than table_size")


def make_keys(slots, table_size, rng):
    """Make unique integer keys that hash to the requested starting slots."""
    # If key = slot + multiple * table_size, then key % table_size = slot.
    # Each key gets a different multiple so duplicate slots still give
    # different keys. This lets us create collisions on purpose.
    multiples = rng.sample(range(1, len(slots) * 10 + 1), len(slots))
    keys = []

    for i in range(len(slots)):
        key = slots[i] + multiples[i] * table_size
        keys.append(key)

    return keys


def workload_info(keys, table_size):
    """Count how many keys start at each hash table slot."""
    counts = [0] * table_size

    for key in keys:
        counts[key % table_size] += 1

    used_slots = sum(1 for count in counts if count > 0)

    return {
        "table_size": table_size,
        "num_keys": len(keys),
        "load_factor": len(keys) / table_size,
        "used_starting_slots": used_slots,
        "initial_collisions": len(keys) - used_slots,
        "slot_counts": counts,
    }


def generate_workload(workload_type, table_size, num_keys, seed=42,
                      skew_strength=0.75, hot_fraction=0.20,
                      return_metadata=False):
    """Generate either workload using one function.

    Returns a list of keys by default. If return_metadata is True,
    returns (keys, information_dictionary).
    """
    if workload_type == "uniform":
        from .uniform_workload import generate_uniform_keys

        return generate_uniform_keys(table_size, num_keys, seed=seed,
                                     return_metadata=return_metadata)

    if workload_type == "skewed":
        from .skewed_workload import generate_skewed_keys

        return generate_skewed_keys(table_size, num_keys, seed=seed,
                                    skew_strength=skew_strength,
                                    hot_fraction=hot_fraction,
                                    return_metadata=return_metadata)

    raise ValueError("workload_type must be 'uniform' or 'skewed'")
