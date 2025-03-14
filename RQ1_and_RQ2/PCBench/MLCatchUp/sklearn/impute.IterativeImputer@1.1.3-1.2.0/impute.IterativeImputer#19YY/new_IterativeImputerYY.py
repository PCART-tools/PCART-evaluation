import numpy as np
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
imp_mean = IterativeImputer(max_iter=10, n_nearest_features=None, tol=0.001, initial_strategy='mean', sample_posterior=False, missing_values=0, keep_empty_features=False)
