# Experiment runner for the benchmark workflow

from src.benchmark.metrics import (
    measure_insertions,
    measure_lookups
    )
from src.benchmark.result_record import ResultRecord
from src.hash_table.strategy_registry import create_hash_table
from src.workloads.generator import generate_workload
from src.config import STRATEGIES, WORKLOAD_TYPES, TABLE_SIZES, LOAD_FACTORS, NUM_TRIALS, RANDOM_SEED, SKEW_STRENGTH, HOT_FRACTION

def run_trial(
    table,
    insertion_keys,
    lookup_keys,
    strategy_name,
    workload_type,
    table_size,
    load_factor,
    trial_number
):

    insert_metrics = measure_insertions(
        table,
        insertion_keys
    )


    lookup_metrics = measure_lookups(
        table,
        lookup_keys
    )

    result = ResultRecord(
        strategy_name=strategy_name,
        workload_type=workload_type,

        table_size=table_size,
        load_factor=load_factor,

        trial_number=trial_number,

        insertion_time=insert_metrics[
            "insertion_time"
        ],

        lookup_time=lookup_metrics[
            "lookup_time"
        ],

        total_insert_probes=insert_metrics[
            "total_insert_probes"
        ],

        total_lookup_probes=lookup_metrics[
            "total_lookup_probes"
        ],

        average_insert_probes=insert_metrics[
            "average_insert_probes"
        ],

        average_lookup_probes=lookup_metrics[
            "average_lookup_probes"
        ],

        max_insert_probes=insert_metrics[
            "max_insert_probes"
        ],

        max_lookup_probes=lookup_metrics[
            "max_lookup_probes"
        ],

        successful_lookups=lookup_metrics[
            "successful_lookups"
        ],

        unsuccessful_lookups=lookup_metrics[
            "unsuccessful_lookups"
        ],

        num_keys=len(insertion_keys)
    )

    return result

def run_all_trials():
    results = []

    for workload_type in WORKLOAD_TYPES:
        for table_size in TABLE_SIZES:
            for load_factor in LOAD_FACTORS:

                # Compute num keys here because it only depends on load factor and table size
                num_keys = round(load_factor * table_size)

                for trial_number in range(NUM_TRIALS):
                    trial_seed = RANDOM_SEED + trial_number
                    keys = generate_workload(workload_type, table_size, num_keys, seed=trial_seed, skew_strength=SKEW_STRENGTH, hot_fraction=HOT_FRACTION)
                    print(f'Workload type: {workload_type}\n Table size: {table_size}\n Load factor: {load_factor}\n Trial number: {trial_number}')
                    for strategy in STRATEGIES:
                        table = create_hash_table(strategy, table_size)
                        result_record = run_trial(table, keys, keys, strategy, workload_type, table_size, load_factor, trial_number)
                        results.append(result_record)

    return results
