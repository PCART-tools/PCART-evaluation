import dask.dataframe as dd
ddf = dd.read_parquet('/home/zhang/Documents/example.parquet', None, None, None, None, None, 'auto', None, split_row_groups=True, chunksize=None)
