from sklearn import linear_model
reg = linear_model.LassoLars(1.0, max_iter=500, fit_intercept=True, verbose=False, normalize=True, precompute='auto', jitter=None, random_state=None)
