"""Generate a workload with approximately uniform starting hash slots."""

import random

from .generator import check_inputs, make_keys, workload_info


def generate_uniform_keys(table_size, num_keys, seed=42,
                          return_metadata=False):
    """Return unique keys whose starting slots are chosen uniformly.

    Slots are selected with replacement, so normal random collisions
    can still happen. Using the same seed gives the same keys again.
    """
    check_inputs(table_size, num_keys)
    rng = random.Random(seed)

    slots = []
    for _ in range(num_keys):
        slots.append(rng.randrange(table_size))

    keys = make_keys(slots, table_size, rng)

    if return_metadata:
        info = workload_info(keys, table_size)
        info["workload_type"] = "uniform"
        info["seed"] = seed
        return keys, info

    return keys
