import numpy as np
from scipy.fft import dstn
x = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]], dtype=float)
result = dstn(x, orthogonalize=None)
