import numpy as np
from scipy.fft import hfftn
x = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
s = (3, 3)
axes = (0, 1)
norm = 'ortho'
overwrite_x = False
result = hfftn(x, s=s, axes=axes, norm=norm, overwrite_x=overwrite_x, workers=None, plan=None)
print(result)
