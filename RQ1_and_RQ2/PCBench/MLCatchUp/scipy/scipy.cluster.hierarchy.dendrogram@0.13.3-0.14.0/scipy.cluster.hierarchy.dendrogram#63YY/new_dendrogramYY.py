import scipy.cluster.hierarchy as sch
import numpy as np
import matplotlib
matplotlib.use('Agg')
Z = np.array([[1, 2, 0.1, 2], [3, 4, 0.2, 3], [0, 5, 0.3, 5], [6, 7, 0.4, 7]])
sch.dendrogram(Z, 30, truncate_mode=None, color_threshold=None, get_leaves=True, orientation='top', labels=None, count_sort=False, distance_sort=False, show_leaf_counts=True, ax=None)
