# A Comprehensive Guide to Polars: Efficient Data Manipulation Compared to Pandas

In the realm of data manipulation, **Pandas** has been the go-to library for Python developers and data scientists due to its versatility and power. However, with the increasing size of datasets and the need for speed, alternatives like **Polars** have emerged. This tutorial will introduce you to Polars, demonstrating its efficiency and showcasing benchmarks that contrast its performance with Pandas through simple data manipulation tasks.

## What is Polars?

Polars is a fast DataFrame library designed for parallel execution and efficient memory management. Unlike Pandas, which is single-threaded and can struggle with large datasets, Polars leverages lazy evaluation and parallel processing, making it suitable for high-performance data manipulation.

### Key Benefits of Polars:
- **Speed**: Built with performance in mind, Polars utilizes Rust's concurrency features.
- **Memory Efficiency**: Uses Arrow memory format, ensuring minimal memory overhead.
- **Lazy Evaluation**: Only computes the result when needed, allowing for optimizations.

## Getting Started with Polars

Before we dive into the benchmarks, ensure you have both Pandas and Polars installed. You can do this with pip:

```bash
pip install pandas polars
```

### Creating a Dataset

To compare performance, we first need to create a dataset. We'll generate a CSV file with random data.

#### Dataset Creation Script: `benchmark-part-1/0_create_dataset.py`
```python
import pandas as pd
import numpy as np

def create_large_dataset(size=10**6):
    data = {
        "id": np.random.randint(1, 10000, size),
        "value_1": np.random.randn(size),
        "value_2": np.random.randn(size),
        "category": np.random.choice(['A', 'B', 'C', 'D'], size),
    }
    return data

dataset_size = 10**6
data_pandas = create_large_dataset(dataset_size)
df_pandas = pd.DataFrame(data_pandas)

df_pandas.to_csv('test_dataset.csv', index=False)
```

Run this script to generate a dataset of 1,000,000 records, then we can proceed with the benchmarking.

## Benchmarking Polars vs Pandas

We'll benchmark three common data manipulation tasks: reading a CSV file, adding a new column, and filtering rows.

### 1. Benchmarking CSV Reading

#### Benchmark Import Script: `benchmark-part-1/1_benchmark_read.py`
```python
import pandas as pd
import polars as pl
import timeit

def read_csv_pandas():
    pd.read_csv('test_dataset.csv')

def read_csv_polars():
    pl.read_csv('test_dataset.csv')

time_pandas_csv = timeit.timeit(read_csv_pandas, number=10)
time_polars_csv = timeit.timeit(read_csv_polars, number=10)
print(f"CSV Read - Pandas: {time_pandas_csv:.4f} s, Polars: {time_polars_csv:.4f} s")
```

### 2. Benchmarking Column Creation

#### Column Creation Benchmark Script: `benchmark-part-1/2_create_column_benchmark.py`
```python
import pandas as pd
import polars as pl
import timeit

df_pandas = pd.read_csv('test_dataset.csv')
df_polars = pl.read_csv('test_dataset.csv')

def add_column_pandas():
    df_pandas['new_column'] = df_pandas['value_1'] * df_pandas['value_2']

def add_column_polars():
    df_polars.with_columns((pl.col('value_1') * pl.col('value_2')).alias('new_column'))

time_pandas_add_column = timeit.timeit(add_column_pandas, number=10)
time_polars_add_column = timeit.timeit(add_column_polars, number=10)
print(f"Add Column - Pandas: {time_pandas_add_column:.4f} s, Polars: {time_polars_add_column:.4f} s")
```

### 3. Benchmarking Row Filtering

#### Row Filtering Benchmark Script: `benchmark-part-1/3_filter_benchmark.py`
```python
import pandas as pd
import polars as pl
import timeit

df_pandas = pd.read_csv('test_dataset.csv')
df_polars = pl.read_csv('test_dataset.csv')

def filter_rows_pandas():
    df_pandas[df_pandas['category'] == 'A']

def filter_rows_polars():
    df_polars.filter(pl.col('category') == 'A')

time_pandas_filter = timeit.timeit(filter_rows_pandas, number=10)
time_polars_filter = timeit.timeit(filter_rows_polars, number=10)
print(f"Filter Rows - Pandas: {time_pandas_filter:.4f} s, Polars: {time_polars_filter:.4f} s")
```

### 4. Benchmarking GroupBy Operations

#### GroupBy Benchmark Script: `benchmark-part-1/4_groupby_benchmark.py`
```python
import pandas as pd
import polars as pl
import timeit

df_pandas = pd.read_csv('test_dataset.csv')
df_polars = pl.read_csv('test_dataset.csv')

def groupby_pandas():
    df_pandas.groupby('category').agg({'value_1': 'mean'})

def groupby_polars():
    df_polars.groupby('category').agg(pl.col('value_1').mean())

time_pandas_groupby = timeit.timeit(groupby_pandas, number=10)
time_polars_groupby = timeit.timeit(groupby_polars, number=10)
print(f"Group By - Pandas: {time_pandas_groupby:.4f} s, Polars: {time_polars_groupby:.4f} s")
```

## Conclusion

Through this tutorial, you have seen how Polars not only offers a powerful alternative to Pandas for handling large datasets but also provides an opportunity for better performance. In every task — reading CSV files, adding columns, filtering, and grouping — Polars consistently outperformed Pandas, making it a robust choice for data manipulation.

**Next Steps**
As you progress in your data science journey, consider incorporating Polars into your workflow for better efficiency, especially when dealing with large datasets. Happy coding!