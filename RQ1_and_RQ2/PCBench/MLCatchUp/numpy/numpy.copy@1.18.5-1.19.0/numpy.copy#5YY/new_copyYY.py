import numpy as np
a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.copy(a=a, order='F', subok=False)
