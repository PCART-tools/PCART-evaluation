import numpy as np
X = np.array([[-1, -1], [-2, -1], [1, 1], [2, 1]])
y = np.array([1, 1, 2, 2])
from sklearn.svm import NuSVC
clf = NuSVC(0.5, 'rbf', 3, 'scale', 0.0, shrinking=True, probability=False, tol=0.001, break_ties=False)
