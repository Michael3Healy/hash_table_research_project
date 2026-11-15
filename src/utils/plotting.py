# Plotting helpers for benchmark output


from pathlib import Path
import matplotlib.pyplot as plt
import pandas as pd

def results_dataframe(results):
    return pd.DataFrame(
        [result.to_dict() for result in results]        
        )
def ag_trail_results(df):
    numeric_columns = [
        "insertion_time",
        "lookup_time",
        "average_insert_probes",
        "average_lookup_probes",
        "total_insert_probes",
        "total_lookup_probes",
        "successful_lookups",
        "unsuccessful_lookups",
        "num_keys"
        ]
    grouped = (
        df.groupby(
        [
            "strategy_name",
            "workload_type",
            "table_size",
            "load_factor"
        ]
            )[numeric_columns]
        .mean()
        .reset_index()
        
    )
    
    return grouped
def create_output_directory(directory): 
    Path(directory).mkdir(
        parents = True,
        exist_ok = True
    )
def plot_metric(
        df,
        workload_type,
        metric,
        title,
        ylabel,
        save_path = None
 ):

    plt.figure(figsize = (8,5))
    subset = df[
        df["workload_type"] == workload_type
    ]
    for strategy in sorted(
            subset[ "strategy_name" ].unique()
            ):
        strategy_df = subset[
            subset[ "strategy_name" ] == strategy
            ]
        
        strategy_df = strategy_df.sort_values(
            "load_factor"
        )

        plt.plot(
            strategy_df["load_factor"],
            strategy_df[metric],
            marker="o",
            linewidth=2,
            label=strategy.capitalize()
        )

    plt.title(title)
    plt.xlabel("Load Factor")
    plt.ylabel(ylabel)

    plt.grid(True, alpha = 0.3)
    plt.legend()

    if save_path:
        create_output_directory(
            Path(save_path).parent
        )

        plt.savefig(
            save_path,
            dpi=300,
            bbox_inches = "tight"
        )
    plt.tight_layout()
    plt.close()
def generate_probe_plots(
    results_df,
    charts_dir
):


    for workload in results_df[
        "workload_type"
    ].unique():

        plot_metric(
            results_df,
            workload,
            "average_insert_probes",
            f"{workload.title()} Workload: Average Insert Probes",
            "Average Insert Probes",
            f"{charts_dir}/{workload}_insert_probes.png"
        )

        plot_metric(
            results_df,
            workload,
            "average_lookup_probes",
            f"{workload.title()} Workload: Average Lookup Probes",
            "Average Lookup Probes",
            f"{charts_dir}/{workload}_lookup_probes.png"
        )

def generate_timing_plots(
    results_df,
    charts_dir
):
    for workload in results_df[
        "workload_type"
    ].unique():

        plot_metric(
            results_df,
            workload,
            "insertion_time",
            f"{workload.title()} Workload: Insertion Time",
            "Insertion Time (seconds)",
            f"{charts_dir}/{workload}_insert_time.png"
        )

        plot_metric(
            results_df,
            workload,
            "lookup_time",
            f"{workload.title()} Workload: Lookup Time",
            "Lookup Time (seconds)",
            f"{charts_dir}/{workload}_lookup_time.png"
        )
def generate_all_plots(
    result_records,
    charts_dir
):
    df = results_dataframe(
        result_records
        )
    df = ag_trail_results(df)
    generate_probe_plots(
        df,
        charts_dir
    )
    generate_timing_plots(
        df,
        charts_dir
    )
    return df
