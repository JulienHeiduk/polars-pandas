import pandas as pd
import polars as pl
from memory_profiler import memory_usage
import timeit

# Load datasets
df_pandas = pd.read_csv('test_dataset.csv')
df_polars = pl.read_csv('test_dataset.csv')

# Function to add a new column in pandas
def add_column_pandas():
    df_pandas['new_column'] = df_pandas['value_1'] * df_pandas['value_2']

# Function to add a new column in polars
def add_column_polars():
    df_polars.with_columns((pl.col('value_1') * pl.col('value_2')).alias('new_column'))

# Measure memory usage and time for Pandas
mem_usage_pandas = memory_usage((add_column_pandas,), max_iterations=100)
time_pandas_add_column = timeit.timeit(add_column_pandas, number=10)

# Measure memory usage and time for Polars
mem_usage_polars = memory_usage((add_column_polars,), max_iterations=100)
time_polars_add_column = timeit.timeit(add_column_polars, number=10)

# Print the results
print(f"Add a new column - Pandas: {time_pandas_add_column:.4f} s, Memory Usage: {mem_usage_pandas[0]:.2f} MiB")
print(f"Add a new column - Polars: {time_polars_add_column:.4f} s, Memory Usage: {mem_usage_polars[0]:.2f} MiB")
