from sklearn.svm import SVR
from sklearn.ensemble import BaggingRegressor
from sklearn.datasets import make_regression
(X, y) = make_regression(n_samples=100, n_features=4, n_informative=2, n_targets=1, random_state=0, shuffle=False)
regr = BaggingRegressor(base_estimator=SVR(), max_features=1.0, max_samples=1.0, bootstrap=True, bootstrap_features=False, n_estimators=10, warm_start=False, oob_score=False, estimator=None)
