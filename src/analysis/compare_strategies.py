
# Helps with interpreting the benchmark results

from src.models.experiment_result import ExperimentResult
from src.config import STRATEGIES, LOAD_FACTORS


def summarize_experiments(records):
    grouped = {}
    for record in records:
        key = (record.strategy_name, record.workload_type, record.table_size, record.load_factor)
        grouped.setdefault(key, []).append(record)

    summary = {key : ExperimentResult.from_records(value) for key, value in grouped.items()}

    return summary

def rank_strategies(summary, workload_type, table_size, load_factor, metric):
    ranked = []
    for strategy in STRATEGIES:

        # Can use this key to look up record in experiment summary
        key = (strategy, workload_type, table_size, load_factor)
        result = summary[key]
        ranked.append((strategy, getattr(result, metric)))

    # Sorts "ranked" list by second element in pair, which is the comparison value
    sorted_ranks = sorted(ranked, key=lambda pair: pair[1])
    return sorted_ranks

def compare_uniform_vs_skewed(summary, strategy_name, table_size, load_factor, metric):
    uniform_key = (strategy_name, "uniform", table_size, load_factor)
    skewed_key = (strategy_name, "skewed", table_size, load_factor)
    uniform_result = summary[uniform_key]
    skewed_result = summary[skewed_key]

    uniform_value = getattr(uniform_result, metric)
    skewed_value = getattr(skewed_result, metric)

    return skewed_value / uniform_value

def skew_sensitivity_by_load_factor(summary, strategy_name, table_size, metric):
    sensitivity = []
    for load_factor in LOAD_FACTORS:
        ratio = compare_uniform_vs_skewed(summary, strategy_name, table_size, load_factor, metric)
        sensitivity.append((load_factor, ratio))

    return sensitivity

def most_skew_sensitive_strategy(summary, table_size, load_factor, metric):
    ratios = []
    for strategy in STRATEGIES:
        skewed_to_uniform_ratio = compare_uniform_vs_skewed(summary, strategy, table_size, load_factor, metric)
        ratios.append((strategy, skewed_to_uniform_ratio))

    # Find strategy with max ratio of skewed to uniform discrepancy
    strategy_name, ratio = max(ratios, key=lambda pair: pair[1])
    return (strategy_name, ratio)
