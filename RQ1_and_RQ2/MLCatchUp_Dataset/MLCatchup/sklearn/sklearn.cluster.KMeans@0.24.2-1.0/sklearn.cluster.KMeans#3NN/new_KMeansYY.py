# -*- coding: utf-8 -*-
import numpy as np
#import matplotlib.pyplot as plt
from sklearn.cluster import KMeans as km
from sklearn.cluster import MiniBatchKMeans as minikm
from sklearn.cluster import Birch
#import pandas as pd
from sklearn import metrics
import time
from sklearn.decomposition import PCA
#from pyclustering.cluster import kmeans
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import davies_bouldin_score

def best_original_kmeans(number_clusters, data):

    for i in range(1, number_clusters + 1):

        '''Utiliza K-means para clusterizar os dados'''
        kmeans = km(n_clusters=i, n_init=20, verbose=False, tol=1e-06)
        kmeans.fit(X=data)

    #return clusters, cost_clusters, best_model, best_cluster

np.random.seed(80) #新增
x=5 #新增
data=np.random.rand(200,3)  #新增
best_original_kmeans(x,data)   #新增