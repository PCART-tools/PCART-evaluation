from pandas import testing as tm
import pandas as pd
a = pd.Series([1, 2, 3, 4])
b = pd.Series([1, 2, 3, 4])
tm.assert_series_equal(a, b, True, 'equiv', True, False, check_names=True, check_exact=True, check_datetimelike_compat=False, check_categorical=True, check_category_order=True, check_freq=True, rtol=1e-05, atol=1e-08, check_flags=True)
