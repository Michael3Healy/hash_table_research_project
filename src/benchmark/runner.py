"""Experiment runner for the benchmark workflow.

Planned contents for this file:
- loop over workload types
- loop over occupancy levels and trial counts
- selection of strategy implementation
- execution of insertion and lookup benchmark tasks
- collection of raw timing and probe-count data
- preparation of results for analysis and reporting

This file defines the experiment matrix and manages the benchmark execution flow.
"""

# File outline only: no implementation code.
# 1. run_experiment() orchestration function
# 2. workload and occupancy iteration
# 3. strategy execution loop
# 4. raw metric capture
# 5. result packaging for analysis



from scr.benchmark.metrics import (
    measure_insertions,
    measure_lookups
    )
from scr.benchmark.results_record import ResultsRecord


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
