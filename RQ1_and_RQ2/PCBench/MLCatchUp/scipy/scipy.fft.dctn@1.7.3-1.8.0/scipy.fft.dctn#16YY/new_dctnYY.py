import numpy as np
from scipy.fft import dctn
x = np.random.randn(4, 4, 4)
result = dctn(x, 2, (3, 3, 3), (0, 1, 2), norm='ortho', orthogonalize=None)
