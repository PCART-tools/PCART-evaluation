import numpy as np
a = np.array([[10, 7, 4], [3, 2, 1]])
result = np.percentile(a, q=[25, 50, 75], method='linear')
print(result)
