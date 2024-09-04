import pandas as pd
import polars as pl
import numpy as np
import timeit

def create_large_dataset(size=10**6):
    data = {
        "id": np.random.randint(1, 10000, size),
        "value_1": np.random.randn(size),
        "value_2": np.random.randn(size),
        "category": np.random.choice(['A', 'B', 'C', 'D'], size),
    }
    return data

dataset_size = 10**6

data_polars = create_large_dataset(dataset_size)
df_polars = pl.DataFrame(data_polars)

df_polars.write_csv('test_dataset.csv')