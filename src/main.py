# Project entry point

from src.benchmark.runner import run_all_trials
from src.analysis.report_generator import generate_report
from src.utils.plotting import generate_all_plots
from src.config import CHARTS_DIR

def main():
    records = run_all_trials()
    report = generate_report(records)
    generate_all_plots(records, CHARTS_DIR)
    print(report["narrative"])

if __name__ == "__main__":
    main()

# AI was used in the preparation of this assignment. It was used in the following ways: brainstorming, outlining, troubleshooting for the project code.