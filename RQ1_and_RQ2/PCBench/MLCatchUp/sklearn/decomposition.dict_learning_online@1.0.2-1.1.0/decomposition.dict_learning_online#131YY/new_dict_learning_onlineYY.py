from sklearn.decomposition import dict_learning_online
import numpy as np
X = np.array([[-1, -1], [-2, -1], [1, 1], [2, 1]])
dict_learning_online(X, return_code=True, callback=None, alpha=1, dict_init=None, n_iter=100, n_components=2, max_iter=None, tol=0.001, max_no_improvement=10)
