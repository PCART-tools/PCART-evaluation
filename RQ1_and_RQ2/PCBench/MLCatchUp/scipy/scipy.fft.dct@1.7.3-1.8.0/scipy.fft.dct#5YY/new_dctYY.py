from scipy import fft
import numpy as np
x = np.array([1, 2, 3, 4, 5])
result = fft.dct(x=x, type=2, orthogonalize=None)
