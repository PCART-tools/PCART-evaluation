import scipy.stats
result = scipy.stats.ttest_ind([1, 2, 3, 4, 5], b=[2, 3, 4, 5, 6], nan_policy='propagate')
