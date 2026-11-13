"""Generate keys that mostly hash into one small part of the table."""

import random

from .generator import check_inputs, make_keys, workload_info


def generate_skewed_keys(table_size, num_keys, seed=42,
                         skew_strength=0.75, hot_fraction=0.20,
                         return_metadata=False):
    """Return unique keys with a controllable collision hot spot.

    hot_fraction is the fraction of table slots in the hot region.
    skew_strength is the chance of choosing from that region instead
    of choosing a slot from the entire table. At 0, slots are uniform.
    At 1, every key starts in the hot region.
    """
    check_inputs(table_size, num_keys)

    if not 0 <= skew_strength <= 1:
        raise ValueError("skew_strength must be between 0 and 1")

    if not 0 < hot_fraction <= 1:
        raise ValueError("hot_fraction must be greater than 0 and at most 1")

    rng = random.Random(seed)
    hot_size = max(1, int(table_size * hot_fraction))
    hot_start = rng.randrange(table_size)

    slots = []
    for _ in range(num_keys):
        if rng.random() < skew_strength:
            # The % allows the hot region to wrap around the end.
            slot = (hot_start + rng.randrange(hot_size)) % table_size
        else:
            slot = rng.randrange(table_size)
        slots.append(slot)

    keys = make_keys(slots, table_size, rng)

    if return_metadata:
        info = workload_info(keys, table_size)
        hot_keys = 0
        for key in keys:
            slot = key % table_size
            if (slot - hot_start) % table_size < hot_size:
                hot_keys += 1

        info["workload_type"] = "skewed"
        info["seed"] = seed
        info["skew_strength"] = skew_strength
        info["hot_fraction"] = hot_fraction
        info["hot_start"] = hot_start
        info["hot_size"] = hot_size
        info["hot_key_fraction"] = hot_keys / num_keys if num_keys else 0.0
        return keys, info

    return keys
