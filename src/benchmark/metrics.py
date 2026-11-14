# Benchmarking and metric collection helpers

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
        "insertion_time": insertion_time,
        "total_insert_probes": total_probes,
        "average_insert_probes": average_probes,
        "max_insert_probes": max_probes
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
    
    lookup_time = end_time - start_time
    
    average_probes = (
        total_probes / len( lookup_keys )
        if len( lookup_keys ) > 0
        else 0
    )
    
    return{
        "lookup_time": lookup_time,
        "total_lookup_probes": total_probes,
        "average_lookup_probes": average_probes,
        "max_lookup_probes": max_probes,
        "successful_lookups": successful_lookups,
        "unsuccessful_lookups": unsuccessful_lookups
        }