import pandas as pd
import numpy as np
df = pd.DataFrame({'B': [0, 1, 2, np.nan, 4]})
df.rolling(window=2, min_periods=None, center=False, win_type='triang', on=None).sum()
