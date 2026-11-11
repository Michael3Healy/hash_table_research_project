# Hash Table Research Project Context

## Project title

Evaluating Open-Addressing Collision Resolution Under Uniform and Skewed Workloads

## Source proposal

This project brief was synthesized from the project proposal PDF in this repository: Project_Proposal_Final.pdf.

## Team

- Michael Healy
- Sean Gillette
- Joseph Morgan

## Research goal

The project investigates how workload distribution affects the performance of open-addressed hash tables that use different collision-resolution strategies:

- Linear probing
- Quadratic probing
- Double hashing

The main emphasis is on comparing behavior under both approximately uniform workloads and deliberately skewed workloads.

## Why this project matters

Hash tables are commonly used in databases, operating systems, networking systems, compilers, and large-scale data-processing systems because they provide efficient lookup and insertion behavior. However, performance is not determined by load factor alone. It also depends on:

- how collisions are resolved,
- how the data is distributed,
- and how clustering or locality change under real workload conditions.

Relevant literature cited in the proposal highlights that:

- linear probing can suffer from primary clustering as table occupancy grows,
- quadratic probing spreads probes more broadly and may reduce clustering effects,
- and double hashing provides a distinct probe pattern that is useful for additional comparison.

The proposal also highlights that prior work often evaluates these methods under mostly uniform conditions, but real workloads can be skewed and unevenly distributed.

## Core research questions

The proposal centers on the following primary question:

How does workload distribution affect the performance of linear probing, quadratic probing, and double hashing in open-addressed hash tables?

Related questions include:

- How does each strategy respond when workloads change from uniform to increasingly skewed?
- Does one strategy experience a larger increase in probe count or execution time under skewed conditions?
- Does higher occupancy amplify the effect of workload skew?
- Are the relative advantages of the strategies different under uniform and skewed workloads?

## Methodology

The project uses implementation and empirical benchmarking.

### Implementations

Separate hash-table implementations will be created for:

- linear probing,
- quadratic probing,
- double hashing.

These implementations will use equivalent table capacities and comparable hashing conditions so the primary variable being studied is the collision-resolution method.

### Workload design

Two main workload types will be generated:

1. Uniform workload
   - initial hash locations are distributed approximately evenly across the table
2. Skewed workload
   - a larger share of initial hash locations are concentrated in a smaller portion of the table
   - this creates more collisions and a less uniform distribution

The same generated key sets are used for all three strategies so comparisons are fair.

### Experimental conditions

The strategies will be evaluated across several occupancy levels:

- lower load factor
- moderate load factor
- higher load factor

Multiple trials will be run for each condition to improve reliability.

## Metrics

The proposal focuses on three primary measurements:

- insertion time
- lookup time
- average number of probes required for operations

The number of probes is especially important because it directly reflects algorithmic behavior, while execution time captures empirical performance in practice.

## Expected outcomes

The expected result is not necessarily that one strategy is universally superior. Instead, the study anticipates that:

- under uniform workloads, differences between strategies may be modest at lower occupancy,
- as workloads become more skewed and tables become more heavily occupied, differences in performance may become more pronounced,
- linear probing may be especially sensitive to concentrated collisions because of primary clustering,
- quadratic probing may reduce clustering by spreading probes over a wider range of positions,
- double hashing will provide an additional comparison because its probe sequence differs from both linear and quadratic probing.

## Significance of the study

The broader implication is that collision-resolution strategies should be evaluated not only according to theoretical average-case behavior but also according to the characteristics of the workloads in which they are used. The project aims to provide a more realistic comparison than testing each strategy only under approximately uniform inputs.

## Practical interpretation for this repository

At this stage, the repository appears to be centered on research and benchmarking rather than a finished production implementation. The project likely expects:

- implementation of the three hash-table variants,
- synthetic generation of uniform and skewed workloads,
- benchmarking at multiple occupancy levels,
- performance analysis and comparison tables/graphs,
- and a final write-up that explains which strategies are more or less robust under skewed conditions.

## Working assumptions for future conversations

When continuing this project in future chats, it is reasonable to assume the work is focused on:

- algorithmic comparison of open-addressing strategies,
- empirical performance testing,
- workload skew analysis,
- and presenting results with timing and probe-count measurements.

This should be treated as a research project with a benchmarking orientation rather than a single straightforward implementation task.

## Planned program structure and file outline

This project should be organized as a small benchmarking program with distinct responsibilities. The goal is to keep experimentation, data generation, and results analysis separate so the project stays easy to extend and compare fairly.

### 1. Core project entry point

- README.md
  - high-level project description
  - how to run the benchmark
  - how to interpret the output
  - references to the proposal and research questions

- main entry script file
  - responsible for orchestrating the entire experiment
  - selects workload types and occupancy levels
  - runs each hash-table implementation under the same experimental conditions
  - collects results from each trial
  - passes results to analysis and reporting modules

Sections to include in the main entry point:

- configuration for table size and load factors
- experiment loop over workload types and occupancy levels
- loop over trial counts
- dispatch to each collision-resolution strategy
- results aggregation and output generation

### 2. Hash table implementations

A dedicated module should contain the three open-addressing implementations. Each one should follow the same interface so they can be benchmarked fairly.

Suggested internal sections:

- shared hash table base behavior
- table creation and resizing logic
- insertion logic
- lookup logic
- probe counting logic
- state reporting for metrics

Implementation files should be organized by a common pattern, for example:

- hash_table_base.py or hash_table_common.py
  - shared table metadata
  - common helper functions
  - abstract interface for insert and lookup
  - reusable validation helpers

- linear_probing.py
  - linear-probe sequence logic
  - insertion and lookup behavior specific to linear probing

- quadratic_probing.py
  - quadratic-probe sequence logic
  - insertion and lookup behavior specific to quadratic probing

- double_hashing.py
  - secondary hash function logic
  - probe sequence for double hashing

- collision_strategy_factory.py or strategy_registry.py
  - central registry of the three strategies
  - allows the experiment runner to select a strategy by name

### 3. Workload generation

This part of the project is responsible for generating the data sets used in the benchmark.

Suggested structure:

- workload_generator.py
  - common workload generation interface
  - functions to generate keys
  - generation routines for uniform and skewed workloads

- uniform_workload.py
  - distribute keys approximately evenly across the table
  - produces a relatively balanced initial hash distribution

- skewed_workload.py
  - create a concentrated region of hot slots
  - intentionally increase clustering opportunity
  - produce a non-uniform hash distribution

Important sections inside workload generation:

- key generation for integer or string inputs
- reproducibility control, such as seeded random generation
- workload size and occupied-slot assignment logic
- validation that the same key set can be reused across all strategies

### 4. Experiment runner and configuration

This is the logic that defines what is being tested.

Suggested structure:

- experiment_config.py
  - occupancy levels
  - number of trials per condition
  - table capacity settings
  - workload sizes
  - benchmarking parameters

- experiment_runner.py
  - loops over workload types
  - loops over occupancy levels
  - invokes each strategy with the same inputs
  - records timing and probe metrics
  - stores aggregate metrics for later analysis

This module should clearly separate:

- experiment definition
- experiment execution
- experiment result collection

### 5. Metrics and benchmarking layer

Benchmarking should be isolated from the hash-table logic itself so it stays clean and reusable.

Suggested structure:

- benchmarking.py or metrics.py
  - timing wrappers around insert and lookup operations
  - cumulative probe-count collection
  - per-operation metric tracking
  - average, median, or min-by-trial summaries

Important sections:

- timer utilities
- probe counter instrumentation
- metric aggregation across trials
- result object for a single experimental run

This layer should not contain the actual collision algorithms; it should only measure them.

### 6. Results analysis and reporting

This part turns raw benchmark data into interpretable comparisons.

Suggested structure:

- analysis.py
  - compare uniform versus skewed workloads
  - compare strategies across occupancy levels
  - summarize which strategy is most sensitive to skew

- report_generator.py
  - produce summary tables
  - generate graphs or plots
  - format output for a final report or presentation

Sections to include:

- performance summary by workload type
- performance summary by load factor
- comparison charts for insertion and lookup operations
- ranking of strategies under each condition
- narrative-level summary notes for interpretation

### 7. Data models and result records

A small data model layer is useful to keep results consistent.

Suggested structures:

- result_record.py or metrics_schema.py
  - workload type
  - strategy name
  - table size
  - load factor
  - trial number
  - insertion time
  - lookup time
  - average probes
  - total probes

This makes it easier to export results or analyze them in a tabular way.

### 8. Optional utilities and validation

This is helpful but not strictly required at the start.

Possible files:

- utils.py
  - helper functions for formatting, rounding, validation, and repeated logic

- validation.py
  - sanity checks that the table behaves correctly after insertion and lookup

- plotting.py
  - chart generation for benchmark results

These modules become more useful once the core algorithm comparison is working.

## Recommended high-level architecture

A clean architecture for this project is:

1. Workload generator creates test data.
2. Experiment runner picks a strategy and a workload.
3. Hash table implementation performs inserts/lookups.
4. Benchmarking layer measures time and probes.
5. Results are aggregated and compared.
6. Analysis/reporting modules summarize the findings.

This keeps the code readable and ensures each component has one major responsibility.

## Recommended module boundaries

The project should separate these concerns clearly:

- data generation
- collision strategy logic
- benchmark execution
- result aggregation
- analysis and reporting

This separation is important because the project is not just implementing hash tables; it is studying how different strategies behave under different workload conditions.

## Not allowed in this file

This document intentionally does not include actual code. It is only an architecture and planning outline for future coding work.

## Suggested next step

The next practical step is to convert this outline into a concrete file tree and then implement the project in the order below:

1. shared hash table interface
2. linear probing implementation
3. quadratic probing implementation
4. double hashing implementation
5. workload generation
6. experiment runner
7. benchmarking metrics
8. analysis and report output

This order keeps the work incremental and makes debugging easier because each stage adds a clear, testable capability.

## Concrete file tree for the project

A realistic structure for this project is:

hash_table_research_project/
├── README.md
├── PROJECT_CONTEXT.md
├── Project_Proposal_Final.pdf
├── requirements.txt
├── src/
│ ├── **init**.py
│ ├── main.py
│ ├── config.py
│ ├── hash_table/
│ │ ├── **init**.py
│ │ ├── base_hash_table.py
│ │ ├── linear_probing.py
│ │ ├── quadratic_probing.py
│ │ ├── double_hashing.py
│ │ └── strategy_registry.py
│ ├── workloads/
│ │ ├── **init**.py
│ │ ├── generator.py
│ │ ├── uniform_workload.py
│ │ └── skewed_workload.py
│ ├── benchmark/
│ │ ├── **init**.py
│ │ ├── runner.py
│ │ ├── metrics.py
│ │ └── result_record.py
│ ├── analysis/
│ │ ├── **init**.py
│ │ ├── compare_strategies.py
│ │ └── report_generator.py
│ ├── models/
│ │ ├── **init**.py
│ │ └── experiment_result.py
│ └── utils/
│ ├── **init**.py
│ ├── validation.py
│ └── plotting.py
├── data/
│ ├── raw/
│ └── processed/
├── results/
│ ├── tables/
│ ├── charts/
│ └── summaries/
└── tests/
├── test_hash_table_behavior.py
├── test_workloads.py
└── test_benchmark_runner.py

## Recommended implementation order

This is the cleanest build sequence for the project:

1. Shared hash table interface
   - define the shared operations all strategies must support
   - decide how insertion, lookup, and probe counting will be exposed
   - define the common state fields required by each implementation

2. Base hash table and common utilities
   - set up table sizing, slot representation, and validation helpers
   - create the shared logic used by every collision strategy
   - establish a consistent way to report internal statistics

3. Linear probing implementation
   - implement the linear probe sequence
   - confirm insertion and lookup behavior with a controlled set of keys
   - verify the probe counting logic

4. Quadratic probing implementation
   - implement the quadratic probe sequence
   - ensure the algorithm handles collisions and table occupancy correctly
   - compare its behavior to linear probing in the same conditions

5. Double hashing implementation
   - define the secondary hash function
   - implement the probe sequence and collision handling
   - ensure it behaves consistently with the other strategies

6. Workload generation
   - create a uniform workload generator
   - create a skewed workload generator
   - make sure both use the same keys and the same input sizes where possible
   - include random seed control for reproducibility

7. Experiment configuration
   - define table capacities
   - define load factor ranges
   - define the number of trials per condition
   - define workload size settings

8. Benchmark runner
   - iterate through workload type, load factor, and strategy combinations
   - run the same experiment across all strategies
   - capture timing and probe statistics for each run

9. Result data model
   - capture trial-level result records
   - store strategy name, workload type, occupancy level, probe count, and timings
   - prepare the data for comparison and plotting

10. Analysis and reporting
    - compare uniform versus skewed outcomes
    - summarize performance differences across occupancy levels
    - generate tables and graphs needed for the final report

11. Validation and final review
    - verify that all strategies are tested under identical conditions
    - confirm that metrics are collected consistently
    - check that the final output clearly answers the project research questions

## Recommended development mindset

The project should be built incrementally and fairly. Every strategy must be tested against the same workload sets, the same number of trials, and the same occupancy conditions. That fairness is essential because the project is a comparative study rather than a single algorithm implementation.

## Planning rule

This document stays at the design and workflow level. It does not include implementations, function signatures, or code logic. Those will be created later in a separate development step.
