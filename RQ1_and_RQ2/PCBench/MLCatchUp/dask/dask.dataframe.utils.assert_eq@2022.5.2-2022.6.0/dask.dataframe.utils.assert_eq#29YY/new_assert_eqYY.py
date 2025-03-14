from dask.dataframe.utils import assert_eq
import dask.dataframe as dd
import pandas as pd
pdf = pd.DataFrame({'A': range(5), 'B': range(5, 10)})
ddf = dd.from_pandas(pdf, npartitions=2)
ddf_result = ddf.groupby('A').sum()
pdf_result = pdf.groupby('A').sum()
assert_eq(ddf_result, pdf_result, True, True, check_divisions=True, check_index=True, scheduler='sync', sort_results=True)
