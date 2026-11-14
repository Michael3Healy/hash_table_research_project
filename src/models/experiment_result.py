"""Store the average results from several trials of one experiment."""


class ExperimentResult:
    def __init__(self, strategy_name, workload_type, table_size, load_factor,
                 trial_count, num_keys, average_insertion_time,
                 average_lookup_time, average_insert_probes,
                 average_lookup_probes, max_insert_probes, max_lookup_probes):
        self.strategy_name = strategy_name
        self.workload_type = workload_type
        self.table_size = table_size
        self.load_factor = load_factor
        self.trial_count = trial_count
        self.num_keys = num_keys
        self.average_insertion_time = average_insertion_time
        self.average_lookup_time = average_lookup_time
        self.average_insert_probes = average_insert_probes
        self.average_lookup_probes = average_lookup_probes
        self.max_insert_probes = max_insert_probes
        self.max_lookup_probes = max_lookup_probes

    @classmethod
    def from_records(cls, records):
        """Average trial records from the same experimental condition."""
        records = list(records)

        if not records:
            raise ValueError("At least one trial record is needed")

        first = records[0]

        # Only combine trials with the same strategy and workload settings.
        for record in records:
            if (record.strategy_name != first.strategy_name or
                record.workload_type != first.workload_type or
                record.table_size != first.table_size or
                record.load_factor != first.load_factor or
                record.num_keys != first.num_keys):
                raise ValueError("All records must be from the same experiment")

        count = len(records)

        return cls(
            strategy_name=first.strategy_name,
            workload_type=first.workload_type,
            table_size=first.table_size,
            load_factor=first.load_factor,
            trial_count=count,
            num_keys=first.num_keys,
            average_insertion_time=sum(r.insertion_time for r in records) / count,
            average_lookup_time=sum(r.lookup_time for r in records) / count,
            average_insert_probes=sum(r.average_insert_probes for r in records) / count,
            average_lookup_probes=sum(r.average_lookup_probes for r in records) / count,
            max_insert_probes=max(r.max_insert_probes for r in records),
            max_lookup_probes=max(r.max_lookup_probes for r in records),
        )

    def to_dict(self):
        """Turn the result into a dictionary for tables or CSV files."""
        return {
            "strategy_name": self.strategy_name,
            "workload_type": self.workload_type,
            "table_size": self.table_size,
            "load_factor": self.load_factor,
            "trial_count": self.trial_count,
            "num_keys": self.num_keys,
            "average_insertion_time": self.average_insertion_time,
            "average_lookup_time": self.average_lookup_time,
            "average_insert_probes": self.average_insert_probes,
            "average_lookup_probes": self.average_lookup_probes,
            "max_insert_probes": self.max_insert_probes,
            "max_lookup_probes": self.max_lookup_probes,
        }
