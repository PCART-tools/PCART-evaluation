import matplotlib.pyplot as plt
import numpy as np
X = np.random.rand(100, 100)
plt.imshow(X, 'viridis', None, filterrad=4.0, vmax=None, vmin=None, filternorm=True, alpha=None, aspect='auto', interpolation='nearest', interpolation_stage=None)
