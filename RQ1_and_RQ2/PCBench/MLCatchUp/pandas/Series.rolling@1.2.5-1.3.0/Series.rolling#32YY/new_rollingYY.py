import pandas as pd
import numpy as np
df = pd.Series({'B': 1})
df.rolling(2,  None,  False, win_type='triang', on=None, axis=0, closed=None).sum()
