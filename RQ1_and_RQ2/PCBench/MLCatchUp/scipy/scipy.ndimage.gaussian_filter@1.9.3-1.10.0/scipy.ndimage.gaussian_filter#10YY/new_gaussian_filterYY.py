from scipy.ndimage import gaussian_filter
input_data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
sigma = 1.0
output_data = gaussian_filter(input_data, sigma, order=0, output=None, radius=None)
print(output_data)
