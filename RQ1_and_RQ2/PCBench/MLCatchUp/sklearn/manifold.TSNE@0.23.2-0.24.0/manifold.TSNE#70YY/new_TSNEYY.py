import numpy as np
from sklearn.manifold import TSNE
X = np.array([[0, 0, 0], [0, 1, 1], [1, 0, 1], [1, 1, 1]])
X_embedded = TSNE(n_iter=1000, n_iter_without_progress=300, early_exaggeration=12.0, perplexity=30.0, learning_rate=200.0, n_components=2).fit_transform(X, square_distances='legacy')
