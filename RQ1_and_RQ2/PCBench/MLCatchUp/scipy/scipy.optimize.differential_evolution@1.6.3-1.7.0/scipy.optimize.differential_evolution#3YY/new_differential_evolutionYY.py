from scipy.optimize import differential_evolution

def func(x):
    return x[0] ** 2 + x[1] ** 2
bounds = [(-2, 2), (-2, 2)]
result = differential_evolution(func=func, bounds=bounds, x0=None)
