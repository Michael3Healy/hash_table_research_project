
# RESULT RECORD structure for benchmark runs

from dataclasses import dataclass, asdict

@dataclass
class ResultRecord:
    
    #EXPERIMENT CONFIG
    strategy_name: str
    workload_type: str
    
    table_size: int
    load_factor: float
    
    trial_number: int
    
    #TIMING METRICS
    insertion_time: float
    lookup_time: float
    
    #PROBE STATISTICS 
    total_insert_probes: int
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
    def __str__( self ):
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




    
    
    