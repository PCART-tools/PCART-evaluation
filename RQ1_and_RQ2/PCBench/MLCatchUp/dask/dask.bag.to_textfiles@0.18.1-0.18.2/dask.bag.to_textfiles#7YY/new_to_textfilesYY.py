import dask.bag as db
b = db.from_sequence(['apple', 'banana', 'cherry', 'date', 'elderberry'], npartitions=2)
b.to_textfiles('/home/zhang/Documents/*.txt', None, compression='infer', last_endline=False)
