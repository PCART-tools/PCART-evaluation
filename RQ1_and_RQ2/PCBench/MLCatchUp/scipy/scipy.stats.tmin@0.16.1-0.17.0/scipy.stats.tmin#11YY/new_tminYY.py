import scipy.stats
result = scipy.stats.tmin([1, 2, 3, 4, 5], 2, 0, inclusive=True, nan_policy='propagate')
