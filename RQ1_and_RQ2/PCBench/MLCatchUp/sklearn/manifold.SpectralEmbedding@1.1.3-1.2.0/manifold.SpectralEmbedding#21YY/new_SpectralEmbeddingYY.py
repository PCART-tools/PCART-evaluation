from sklearn.datasets import load_digits
from sklearn.manifold import SpectralEmbedding
(X, _) = load_digits(return_X_y=True)
X.shape
embedding = SpectralEmbedding(2, affinity='nearest_neighbors', random_state=None, gamma=None, eigen_tol='auto')
