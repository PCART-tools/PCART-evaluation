from scipy.fft import idst
x = [1, 2, 3, 4]
type = 2
n = None
axis = -1
norm = None
overwrite_x = False
workers = None
result = idst(x, type, n, axis, norm=norm, overwrite_x=overwrite_x, orthogonalize=None)
