import matplotlib.pyplot as plt
import numpy as np
X = np.random.rand(100, 100)
plt.imshow(X, 'viridis', None, filternorm=True, alpha=None, resample=None, filterrad=4.0, aspect='auto', interpolation='nearest', interpolation_stage=None)
