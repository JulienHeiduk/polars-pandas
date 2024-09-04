import pandas as pd
import polars as pl
from memory_profiler import memory_usage

# Define the functions to read CSV with pandas and polars
def read_csv_pandas():
    pd.read_csv('test_dataset.csv')

def read_csv_polars():
    pl.read_csv('test_dataset.csv')

# Measure memory usage for pandas CSV reading
mem_usage_pandas = memory_usage((read_csv_pandas,), max_iterations=100)
print(f"Pandas CSV Read Memory Usage: {mem_usage_pandas[0]:.2f} MiB")

# Measure memory usage for polars CSV reading
mem_usage_polars = memory_usage((read_csv_polars,), max_iterations=100)
print(f"Polars CSV Read Memory Usage: {mem_usage_polars[0]:.2f} MiB")