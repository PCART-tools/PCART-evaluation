#from __future__ import print_function

from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_samples, silhouette_score

#import matplotlib.pyplot as plt #额外的库
import matplotlib.cm as cm
import numpy as np
#import pandas as pd         #额外的库

from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_samples, silhouette_score
import sys
import pandas as pd
import numpy as np
from sklearn import cluster
from scipy.spatial import distance
import sklearn.datasets
from sklearn.preprocessing import StandardScaler

np.random.seed(42)  # 新增
train_set = np.random.rand(100, 2)  # 新增
cluster_range = range(2, 6)  # 新增

for i in cluster_range:
    kmeans = KMeans(n_clusters=i, n_init=10, max_iter=10000).fit(train_set)
