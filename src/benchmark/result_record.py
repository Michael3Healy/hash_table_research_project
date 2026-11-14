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



#RESULT RECORD 

from dataclasses import dataclass, asdict

@dataclass
class ResultRecord:
    
    #EXPERIMENT CONFIG
    stategy_name: str
    workload_types: str
    
    tabel_size: int
    load_factor: float
    
    trial_number: int
    
    #TIMING METRICS
    insertion_time: float
    lookup_time: float
    
    #PROBE STATISTICS 
    total_insert_proes: int
    total_lookup_probes: int
    
    average_insert_probes: float
    average_lookup_probes: float
    
    max_insert_probes: int
    max_lookup_probes: int
    
    #LOOKUP COMP
    successful_lookups: int
    unsuccessful_lookups: int
    
    # WORKLOAD DATA
    num_keys: int
    
    
    def to_dict( self ):
        return asdict( self )
    def _str_( self ):
        return (
            f"\nResultRecord(\n"
            f"  Strategy: {self.strategy_name}\n"
            f"  Workload: {self.workload_type}\n"
            f"  Table Size: {self.table_size}\n"
            f"  Load Factor: {self.load_factor:.2f}\n"
            f"  Trial: {self.trial_number}\n"
            f"  Insert Time: {self.insertion_time:.6f}s\n"
            f"  Lookup Time: {self.lookup_time:.6f}s\n"
            f"  Avg Insert Probes: {self.average_insert_probes:.2f}\n"
            f"  Avg Lookup Probes: {self.average_lookup_probes:.2f}\n"
            f"  Max Insert Probes: {self.max_insert_probes}\n"
            f"  Max Lookup Probes: {self.max_lookup_probes}\n"
            f")"
        )




    
    
    