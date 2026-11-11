"""Result record structure for benchmark runs.

Planned contents for this file:
- a structured record for one trial of one workload under one strategy
- fields for workload type, strategy name, load factor, table size, and trial number
- timing values for insertion and lookup
- average probes and total probes for the test case
- metadata needed for fair comparison across conditions

This file should define the record format used by the benchmark runner and later analysis.
"""

# File outline only: no implementation code.
# 1. result record schema
# 2. required benchmark fields
# 3. aggregated summary values
# 4. optional serialization helpers
