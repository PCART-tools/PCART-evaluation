import pandas as pd
import numpy as np
df = pd.DataFrame({'A': range(1, 6), 'B': range(10, 15)})
sampled_df = df.sample(n=3, frac=None, replace=False, weights=[0.1, 0.2, 0.3, 0.2, 0.2])
