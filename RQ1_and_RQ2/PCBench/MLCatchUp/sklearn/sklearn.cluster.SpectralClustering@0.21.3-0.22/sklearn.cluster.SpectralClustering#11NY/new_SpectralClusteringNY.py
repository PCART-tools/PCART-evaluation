from sklearn.cluster import SpectralClustering
import numpy as np
X = np.array([[1, 1], [2, 1], [1, 0], [4, 7], [3, 5], [3, 6]])
clustering = SpectralClustering(5, None, None, n_init=10).fit(X, n_components=None)
