from scipy.optimize import brute

def func(x):
    return (x - 2) ** 2
ranges = (slice(-5, 5, 0.1),)
args = ()
Ns = 20
full_output = 0
finish = None
disp = False
result = brute(func, ranges, args, Ns, full_output, finish, disp=disp, workers=1)
