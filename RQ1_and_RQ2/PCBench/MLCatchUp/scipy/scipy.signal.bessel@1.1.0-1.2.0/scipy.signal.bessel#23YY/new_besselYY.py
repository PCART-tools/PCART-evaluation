from scipy import signal
(N, Wn, btype, analog, output, norm) = (4, 0.5, 'low', False, 'ba', 'phase')
result = signal.bessel(N, Wn, btype=btype, analog=analog, output=output, norm=norm, fs=None)
