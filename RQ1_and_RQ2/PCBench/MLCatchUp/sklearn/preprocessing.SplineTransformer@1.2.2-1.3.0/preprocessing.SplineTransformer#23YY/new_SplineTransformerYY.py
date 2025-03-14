import numpy as np
from sklearn.preprocessing import SplineTransformer
X = np.arange(6).reshape(6, 1)
spline = SplineTransformer(extrapolation='constant', knots='uniform', n_knots=5, include_bias=True, sparse_output=False)
