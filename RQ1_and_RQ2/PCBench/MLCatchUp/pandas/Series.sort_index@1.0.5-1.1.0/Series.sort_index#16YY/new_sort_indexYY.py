import pandas as pd
s = pd.Series(['a', 'b', 'c', 'd'], index=[3, 2, 1, 4])
s.sort_index(0,  None,  True,  False,  'quicksort')
