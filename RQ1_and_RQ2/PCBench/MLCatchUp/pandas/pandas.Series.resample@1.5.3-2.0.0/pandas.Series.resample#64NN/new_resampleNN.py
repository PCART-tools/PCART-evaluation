import pandas as pd
index = pd.date_range('1/1/2000', periods=9, freq='T')
series = pd.Series(range(9), index=index)
series.resample('3T', axis=0, closed=None, label=None, convention='start', kind=None, loffset=None, base=None, on=None, level=None).sum()
