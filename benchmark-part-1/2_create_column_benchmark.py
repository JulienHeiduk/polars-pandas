import pandas as pd
import polars as pl
import numpy as np
import timeit

df_pandas = pd.read_csv('test_dataset.csv')

df_polars = pl.read_csv('test_dataset.csv')

def add_column_pandas():
    df_pandas['new_column'] = df_pandas['value_1'] * df_pandas['value_2']

def add_column_polars():
    df_polars.with_columns((pl.col('value_1') * pl.col('value_2')).alias('new_column'))

time_pandas_add_column = timeit.timeit(add_column_pandas, number=10)
time_polars_add_column = timeit.timeit(add_column_polars, number=10)
print(f"                                           Add a new column - Pandas: {time_pandas_add_column:.4f} s, Polars: {time_polars_add_column:.4f} s")
