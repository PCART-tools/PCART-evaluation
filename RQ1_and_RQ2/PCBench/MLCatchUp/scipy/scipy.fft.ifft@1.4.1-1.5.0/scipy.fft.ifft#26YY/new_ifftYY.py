import numpy as np
from scipy.fft import ifft
x = np.array([1.0, 2.0, 3.0, 4.0])
n = None
axis = -1
norm = None
overwrite_x = False
workers = None
result = ifft(x, n=n, axis=axis, norm=norm, overwrite_x=overwrite_x, workers=workers, plan=None)
