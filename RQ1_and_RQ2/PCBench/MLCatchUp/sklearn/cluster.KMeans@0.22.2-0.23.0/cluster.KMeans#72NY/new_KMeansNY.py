from sklearn.cluster import KMeans
import numpy as np
X = np.array([[1, 2], [1, 4], [1, 0], [10, 2], [10, 4], [10, 0]])
kmeans = KMeans(2, precompute_distances='auto', verbose=0, random_state=0, copy_x=True, n_jobs=None, algorithm='auto', init='k-means++', n_init=10, max_iter=300, tol=0.0001).fit(X)
