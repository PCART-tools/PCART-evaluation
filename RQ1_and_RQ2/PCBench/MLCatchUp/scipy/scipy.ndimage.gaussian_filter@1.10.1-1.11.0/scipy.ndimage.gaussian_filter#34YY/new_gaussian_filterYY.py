from scipy import ndimage
input = ...
sigma = 1.5
order = 0
output = None
mode = 'reflect'
cval = 0.0
truncate = 4.0
radius = None
result = ndimage.gaussian_filter(input, radius=radius, output=output, sigma=sigma, mode=mode, order=order, axes=None)
