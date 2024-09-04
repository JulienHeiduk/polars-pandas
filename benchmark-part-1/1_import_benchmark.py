import pandas as pd
import polars as pl
import numpy as np
import timeit

def read_csv_pandas():
    pd.read_csv('test_dataset.csv')

def read_csv_polars():
    pl.read_csv('test_dataset.csv')

time_pandas_csv = timeit.timeit(read_csv_pandas, number=10)
time_polars_csv = timeit.timeit(read_csv_polars, number=10)
print(f"                                           Import CSV - Pandas: {time_pandas_csv:.4f} s, Polars: {time_polars_csv:.4f} s")