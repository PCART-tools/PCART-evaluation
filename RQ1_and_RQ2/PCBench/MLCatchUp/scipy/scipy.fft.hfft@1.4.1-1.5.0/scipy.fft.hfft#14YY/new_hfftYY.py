import scipy
x = [1, 2, 3, 4]
n = 8
axis = 0
norm = 'ortho'
overwrite_x = False
workers = 1
result = scipy.fft.hfft(x=x, n=n, axis=axis, norm=norm, plan=None)
