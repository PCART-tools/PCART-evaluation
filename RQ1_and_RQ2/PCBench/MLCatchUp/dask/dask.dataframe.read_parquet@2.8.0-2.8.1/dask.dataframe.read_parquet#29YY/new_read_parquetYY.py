import dask.dataframe as dd
ddf = dd.read_parquet('/home/zhang/Documents/example.parquet', None, None, None, None, None, engine='auto', chunksize=None)
