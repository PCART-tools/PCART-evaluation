from sklearn import linear_model
reg = linear_model.LassoLars(1.0, fit_path=True, positive=False, fit_intercept=True, verbose=False, normalize=True, precompute='auto', max_iter=500, eps=2.220446049250313e-16, copy_X=True, jitter=None, random_state=None)
