from plotly.figure_factory import create_violin
import numpy as np
from scipy import stats
data_list = np.random.randn(100)
fig = create_violin(data_list, None, None, '#604d9e', False, None, True, 450, 600, title='Violin and Rug Plot', sort=False)
