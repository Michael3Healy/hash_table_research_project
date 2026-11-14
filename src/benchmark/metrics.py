"""Benchmarking and metric collection helpers.

Planned contents for this file:
- timing utilities for insertion and lookup operations
- probe-count aggregation for each benchmarked action
- averaging and summarizing metrics across repeated trials
- helper functions for converting raw measurements into comparable statistics

This file is responsible for measuring performance without determining the algorithm itself.
"""

# File outline only: no implementation code.
# 1. timer wrappers around hash-table operations
# 2. probe counting utilities
# 3. aggregation of trial-level data
# 4. summary statistics helpers

import time

def measure_insertions( table, keys ):
    total_probes = 0
    max_probes = 0
    
    start_time = time.perf_counter()
    for key in keys:
        table.insert( key, key )
        probes = table.last_probe_count 
        total_probes += probes
        
        if probes > max_probes:
            max_probes = probes
            
    end_time = time.perf_counter()
    insertion_time = end_time - start_time
    
    average_probes = (
        total_probes / len( keys )
        if len( keys ) > 0
        else 0
    )
    
    return {
        "INSERTION_TIME": insertion_time, 
        "TOTAL INSERT PROBES" : total_probes,
        "AVERAGE INSERT PROBES" : average_probes,
        "MAX INSERT PROBES" : max_probes
        }

def measure_lookups( table, lookup_keys ):
    total_probes = 0
    max_probes = 0
    
    successful_lookups = 0
    unsuccessful_lookups = 0
    
    start_time = time.perf_counter()
    
    for key in lookup_keys:
        result = table.find(key)
        probes = table.last_probe_count
        total_probes += probes
        
        if probes > max_probes:
            max_probes = probes
            
        if result:
            successful_lookups += 1
        else: 
            unsuccessful_lookups += 1
    end_time = time.perf_counter()
    
    looup_time = end_time - start_time
    
    average_probes = (
        total_probes / len( lookup_keys )
        if len( lookup_keys ) > 0
        else 0
    )
    
    return{
        "LOOKUP TIME" : looup_time,
        "TOTAL LOOKUP PROBES" : total_probes,
        "AVERAGE LOOKUP PROBES" : average_probes,
        "MAX LOOKUP PROBES" : max_probes,
        "SUCCESSFUL LOOKUPS" : successful_lookups,
        "UNSUCCESSFUL LOOKUPS": unsuccessful_lookups
        }