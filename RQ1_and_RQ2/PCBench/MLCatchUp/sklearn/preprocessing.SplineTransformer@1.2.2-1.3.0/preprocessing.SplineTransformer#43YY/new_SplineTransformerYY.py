import numpy as np
from sklearn.preprocessing import SplineTransformer
X = np.arange(6).reshape(6, 1)
spline = SplineTransformer(n_knots=5, degree=3, extrapolation='constant', sparse_output=False)
