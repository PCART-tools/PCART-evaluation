import numpy as np
from scipy.fft import ihfft2
x = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype=float)
s = (3, 3)
axes = (-2, -1)
norm = 'ortho'
overwrite_x = False
workers = 1
result = ihfft2(x=x, s=s, axes=axes, norm=norm, overwrite_x=overwrite_x, plan=None)
