import numpy as np
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [np.nan, np.nan, np.nan]])
result = np.nanmean(a=a, axis=0, dtype=np.float64, out=None, keepdims=False)
