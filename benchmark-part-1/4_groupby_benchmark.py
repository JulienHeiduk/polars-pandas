import pandas as pd
import polars as pl
import numpy as np
import timeit

df_pandas = pd.read_csv('test_dataset.csv')

df_polars = pl.read_csv('test_dataset.csv')

def groupby_agg_pandas():
    df_pandas.groupby('category').agg({'value_1': 'mean', 'value_2': 'sum'})

def groupby_agg_polars():
    df_polars.group_by('category').agg([
        pl.col('value_1').mean(),
        pl.col('value_2').sum()
    ])

# Comparaison du temps de groupby et agrégation
time_pandas_groupby = timeit.timeit(groupby_agg_pandas, number=10)
time_polars_groupby = timeit.timeit(groupby_agg_polars, number=10)
print(f"                                           Groupby benchmark - Pandas: {time_pandas_groupby:.4f} s, Polars: {time_polars_groupby:.4f} s")