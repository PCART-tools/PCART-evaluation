import numpy as np
X = np.array([[-1, -1], [-2, -1], [1, 1], [2, 1]])
y = np.array([1, 1, 2, 2])
from sklearn.svm import SVC
clf = SVC(1.0, 'rbf', degree=3, gamma='auto_deprecated', coef0=0.0, shrinking=True, probability=False, break_ties=False)
