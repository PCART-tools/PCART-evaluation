from scipy.fft import irfft
x = [1, 2, 3, 4, 5]
n = 10
axis = -1
norm = 'ortho'
overwrite_x = False
result = irfft(x=x, n=n, axis=axis, norm=norm, plan=None)
