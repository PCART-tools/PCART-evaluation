import pandas as pd
import numpy as np
df = pd.DataFrame({'B': [0, 1, 2, np.nan, 4]})
df.rolling(2,  None,  False,  None, on=None, axis=0, closed=None).sum()
