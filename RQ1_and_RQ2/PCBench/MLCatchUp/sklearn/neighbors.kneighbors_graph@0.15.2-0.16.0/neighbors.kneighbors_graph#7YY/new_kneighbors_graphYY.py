from sklearn.neighbors import kneighbors_graph
X = [[0], [3], [1]]
A = kneighbors_graph(X=X, n_neighbors=2, mode='connectivity', metric='minkowski', p=2, metric_params=None, include_self=None)
