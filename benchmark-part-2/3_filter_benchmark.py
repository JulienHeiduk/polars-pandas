import pandas as pd
import polars as pl
from memory_profiler import memory_usage
import timeit

# Load datasets
df_pandas = pd.read_csv('test_dataset.csv')
df_polars = pl.read_csv('test_dataset.csv')

# Function to filter rows in pandas
def filter_rows_pandas():
    df_pandas[df_pandas['category'] == 'A']

# Function to filter rows in polars
def filter_rows_polars():
    df_polars.filter(pl.col('category') == 'A')

# Measure memory usage and time for Pandas
mem_usage_pandas = memory_usage((filter_rows_pandas,), max_iterations=100)
time_pandas_filter = timeit.timeit(filter_rows_pandas, number=10)

# Measure memory usage and time for Polars
mem_usage_polars = memory_usage((filter_rows_polars,), max_iterations=100)
time_polars_filter = timeit.timeit(filter_rows_polars, number=10)

# Print the results
print(f"Rows filter - Pandas: {time_pandas_filter:.4f} s, Memory Usage: {mem_usage_pandas[0]:.2f} MiB")
print(f"Rows filter - Polars: {time_polars_filter:.4f} s, Memory Usage: {mem_usage_polars[0]:.2f} MiB")

