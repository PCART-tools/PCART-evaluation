import numpy as np
data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
np.savetxt('example.txt', data, fmt='%.18e', delimiter=' ', encoding=None)
