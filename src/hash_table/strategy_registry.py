"""Choose which collision strategy to use for a hash table."""

from .linear_probing import LinearProbingHashTable
from .quadratic_probing import QuadraticProbingHashTable
from .double_hashing import DoubleHashingHashTable


# Each name points to the class that implements that strategy.
STRATEGIES = {
    "linear": LinearProbingHashTable,
    "quadratic": QuadraticProbingHashTable,
    "double": DoubleHashingHashTable,
}


def list_strategies():
    """Return the names of the available collision strategies."""
    return list(STRATEGIES.keys())


def get_strategy(strategy_name):
    """Find the hash table class that matches a strategy name."""
    if not isinstance(strategy_name, str):
        raise ValueError("Strategy name must be a string")

    strategy_name = strategy_name.strip().lower()

    if strategy_name not in STRATEGIES:
        raise ValueError("Unknown strategy. Choose linear, quadratic, or double")

    return STRATEGIES[strategy_name]


def create_hash_table(strategy_name, capacity):
    """Create an empty hash table using the selected strategy."""
    if type(capacity) is not int or capacity < 2:
        raise ValueError("Table capacity must be an integer greater than 1")

    table_class = get_strategy(strategy_name)
    return table_class(capacity)
