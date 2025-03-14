from sklearn.ensemble import AdaBoostRegressor
from sklearn.datasets import make_regression
(X, y) = make_regression(n_features=4, n_informative=2, random_state=0, shuffle=False)
regr = AdaBoostRegressor(learning_rate=1.0, loss='linear', n_estimators=50, base_estimator=None, estimator=None)
