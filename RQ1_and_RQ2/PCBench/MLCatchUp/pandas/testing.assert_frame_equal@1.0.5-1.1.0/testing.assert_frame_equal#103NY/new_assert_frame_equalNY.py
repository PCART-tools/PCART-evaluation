import pandas as pd
from pandas._testing import assert_frame_equal
df1 = pd.DataFrame({'a': [1, 2], 'b': [3, 4]})
df2 = pd.DataFrame({'a': [1, 2], 'b': [3.0, 4.0]})
assert_frame_equal(df1, df1, True, 'equiv', 'equiv', True, False, True, False, False, False, True, False, 'DataFrame', check_freq=True, rtol=1e-05, atol=1e-08)
