from sklearn.cluster import AgglomerativeClustering
import numpy as np
X = np.array([[1, 2], [1, 4], [1, 0], [4, 2], [4, 4], [4, 0]])
clustering = AgglomerativeClustering(connectivity=None, memory=None, linkage='ward', affinity='euclidean', n_clusters=2, compute_full_tree='auto').fit(X, compute_distances=False)
