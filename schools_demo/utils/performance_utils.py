from time import perf_counter_ns


def measure_time_in_seconds(start, stop):
    return (stop - start) / 1000000000.0
