from pandas import testing as tm
import pandas as pd
a = pd.Series([1, 2, 3, 4])
b = pd.Series([1, 2, 3, 4])
tm.assert_series_equal(a,  b,  True,  'equiv', check_datetimelike_compat=False, check_category_order=True, check_exact=False, check_less_precise=False, obj='Series', check_index=True, check_categorical=True, rtol=1e-05, check_freq=True, atol=1e-08, check_names=True, check_flags=True, check_series_type=True)
