# Helps with generating report of results
from src.config import STRATEGIES
import pandas as pd
from pathlib import Path
from src.config import TABLES_DIR, SUMMARIES_DIR, STRATEGIES, LOAD_FACTORS, TABLE_SIZES
from src.analysis.compare_strategies import summarize_experiments, skew_sensitivity_by_load_factor, most_skew_sensitive_strategy
from src.utils.plotting import create_output_directory

def build_results_table(summary):
    return pd.DataFrame([result.to_dict() for result in summary.values()])



def build_sensitivity_table(summary, metric="average_lookup_probes"):
    table_size = TABLE_SIZES[0]
    rows = []
    for strategy in STRATEGIES:
        load_factor_and_ratio = skew_sensitivity_by_load_factor(summary, strategy, table_size, metric)
        for load_factor, ratio in load_factor_and_ratio:
            rows.append({"strategy_name": strategy, "load_factor": load_factor, "ratio": ratio})
    return pd.DataFrame(rows)

def save_table(df, filename):
    path = Path(TABLES_DIR) / filename
    create_output_directory(path.parent)
    df.to_csv(path, index=False)
    return path

def generate_narrative_summary(summary, metric="average_lookup_probes"):
    table_size = TABLE_SIZES[0]
    lines = []
    for load_factor in LOAD_FACTORS:
        strategy_name, ratio = most_skew_sensitive_strategy(summary, table_size, load_factor, metric)
        lines.append(f'At a load factor of {load_factor:.2f}, {strategy_name} was the most skew-sensitive strategy, with {ratio:.2f}x more {metric.replace('_', ' ')} under skew than uniform.')

    return "\n".join(lines)

def save_summary(text, filename):
    path = Path(SUMMARIES_DIR) / filename
    create_output_directory(path.parent)
    path.write_text(text)
    return path

def generate_report(records):
    summary = summarize_experiments(records)
    results_table = build_results_table(summary)
    save_table(results_table, "results_table.csv")
    sensitivity_table = build_sensitivity_table(summary)
    save_table(sensitivity_table, "sensitivity_table.csv")
    narrative = generate_narrative_summary(summary)
    save_summary(narrative, "narrative_summary.txt")
    return {"results_table": results_table, "sensitivity_table": sensitivity_table, "narrative": narrative}