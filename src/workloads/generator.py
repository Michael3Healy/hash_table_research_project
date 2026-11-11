"""Workload generation utilities.

Planned contents for this file:
- common interface for all workload generators
- helper functions for generating key sets and workload metadata
- optional seed control and reproducibility helpers
- validation checks for key count, table size, and occupancy level
- conversion of generated keys into the format expected by the hash tables

This file should provide shared tooling used by both uniform and skewed workload generators.
"""

# File outline only: no implementation code.
# 1. abstract workload generator interface
# 2. shared key generation helpers
# 3. seed and reproducibility support
# 4. validation of workload size
# 5. output format normalization
