import pandas as pd
df = pd.Series({'name': ['Raphael', 'Donatello'], 'mask': ['red', 'purple'], 'weapon': ['sai', 'bo staff']})
df.to_csv(None,  ',',  '',  None,  None, header=True, index=False, index_label=None)
