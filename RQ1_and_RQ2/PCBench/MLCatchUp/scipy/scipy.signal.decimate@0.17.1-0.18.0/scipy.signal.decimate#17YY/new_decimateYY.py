import numpy as np
from scipy.signal import decimate
x = np.array([1.0, 2.0, 3.0, 4.0, 5.0, 6.0])
result = decimate(x, q=2, n=None, ftype='iir', axis=(- 1), zero_phase=None)
