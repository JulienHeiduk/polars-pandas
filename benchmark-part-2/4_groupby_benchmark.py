import pandas as pd
import polars as pl
from memory_profiler import memory_usage
import timeit

# Load datasets
df_pandas = pd.read_csv('test_dataset.csv')
df_polars = pl.read_csv('test_dataset.csv')

# Function to perform groupby and aggregation in pandas
def groupby_agg_pandas():
    df_pandas.groupby('category').agg({'value_1': 'mean', 'value_2': 'sum'})

# Function to perform groupby and aggregation in polars
def groupby_agg_polars():
    df_polars.groupby('category').agg([
        pl.col('value_1').mean(),
        pl.col('value_2').sum()
    ])

# Measure memory usage and time for Pandas
mem_usage_pandas = memory_usage((groupby_agg_pandas,), max_iterations=1)
time_pandas_groupby = timeit.timeit(groupby_agg_pandas, number=10)

# Measure memory usage and time for Polars
mem_usage_polars = memory_usage((groupby_agg_polars,), max_iterations=1)
time_polars_groupby = timeit.timeit(groupby_agg_polars, number=10)

# Print the results
print(f"Groupby benchmark - Pandas: {time_pandas_groupby:.4f} s, Memory Usage: {mem_usage_pandas[0]:.2f} MiB")
print(f"Groupby benchmark - Polars: {time_polars_groupby:.4f} s, Memory Usage: {mem_usage_polars[0]:.2f} MiB")
