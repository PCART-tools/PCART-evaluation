from sklearn.linear_model import LogisticRegression
from sklearn.inspection import permutation_importance
X = [[1, 9, 9], [1, 9, 9], [1, 9, 9], [0, 9, 9], [0, 9, 9], [0, 9, 9]]
y = [1, 1, 1, 0, 0, 0]
clf = LogisticRegression().fit(X, y)
result = permutation_importance(clf, sample_weight=None, random_state=0, X=X, y=y, scoring=None, n_jobs=None, n_repeats=10, max_samples=1.0)
