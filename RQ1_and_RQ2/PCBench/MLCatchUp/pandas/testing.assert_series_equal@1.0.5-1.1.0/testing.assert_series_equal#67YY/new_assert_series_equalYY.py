import pandas as pd
from pandas._testing import assert_series_equal
df1 = pd.Series({'a': 1, 'b': 1})
df2 = pd.Series({'a': 1, 'b': 1})
assert_series_equal(df1, df1, True, 'equiv', True, False, True, False, check_datetimelike_compat=False, check_categorical=True, check_category_order=True, check_freq=True, rtol=1e-05, atol=1e-08)
