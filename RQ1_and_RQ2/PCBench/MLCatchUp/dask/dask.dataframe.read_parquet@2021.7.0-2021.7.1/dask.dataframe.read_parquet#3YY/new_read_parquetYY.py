import dask.dataframe as dd
ddf = dd.read_parquet('./example.parquet', None, aggregate_files=None)
