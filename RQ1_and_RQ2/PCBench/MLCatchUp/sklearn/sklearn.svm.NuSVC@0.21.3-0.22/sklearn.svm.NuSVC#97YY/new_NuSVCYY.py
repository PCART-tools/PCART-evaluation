import numpy as np
X = np.array([[-1, -1], [-2, -1], [1, 1], [2, 1]])
y = np.array([1, 1, 2, 2])
from sklearn.svm import NuSVC
clf = NuSVC(0.5, 'rbf', 3, 'scale', 0.0, True, False, 0.001, cache_size=200, class_weight=None, verbose=False, max_iter=(- 1), decision_function_shape='ovr', break_ties=False)
