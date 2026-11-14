"""Settings used when running the hash table experiments."""

# Both quadratic probing and double hashing require prime table sizes.
TABLE_SIZES = [101, 1009]

# Keep the highest load at 50% for the current probing implementations.
LOAD_FACTORS = [0.20, 0.35, 0.50]

STRATEGIES = ["linear", "quadratic", "double"]
WORKLOAD_TYPES = ["uniform", "skewed"]

# Repeat each test with a different seed so the results can be averaged.
NUM_TRIALS = 5
RANDOM_SEED = 42

# Skewed workload settings: 75% of the keys favor 20% of the slots.
SKEW_STRENGTH = 0.75
HOT_FRACTION = 0.20

# Folders where the finished benchmark can save results.
RESULTS_DIR = "results"
TABLES_DIR = "results/tables"
CHARTS_DIR = "results/charts"
SUMMARIES_DIR = "results/summaries"
