import numpy as np
from sklearn.preprocessing import SplineTransformer
X = np.arange(6).reshape(6, 1)
spline = SplineTransformer(knots='uniform', include_bias=True, extrapolation='constant', order='C', n_knots=5, sparse_output=False)
