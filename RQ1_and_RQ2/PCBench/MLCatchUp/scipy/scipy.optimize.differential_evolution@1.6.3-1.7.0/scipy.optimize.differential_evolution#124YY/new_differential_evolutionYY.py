from scipy.optimize import differential_evolution

def func(x):
    return x[0] ** 2 + x[1] ** 2
bounds = [(-2, 2), (-2, 2)]
result = differential_evolution(func, bounds, (), 'best1bin', 1000, 15, 0.01, (0.5, 1), 0.7, seed=None, callback=None, disp=False, polish=True, init='latinhypercube', atol=0, x0=None)
