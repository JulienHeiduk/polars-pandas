import pandas as pd
import polars as pl
import numpy as np
import timeit

df_pandas = pd.read_csv('test_dataset.csv')

df_polars = pl.read_csv('test_dataset.csv')

def filter_rows_pandas():
    df_pandas[df_pandas['category'] == 'A']

def filter_rows_polars():
    df_polars.filter(pl.col('category') == 'A')
time_pandas_filter = timeit.timeit(filter_rows_pandas, number=10)
time_polars_filter = timeit.timeit(filter_rows_polars, number=10)
print(f"                                           Rows filter - Pandas: {time_pandas_filter:.4f} s, Polars: {time_polars_filter:.4f} s")
