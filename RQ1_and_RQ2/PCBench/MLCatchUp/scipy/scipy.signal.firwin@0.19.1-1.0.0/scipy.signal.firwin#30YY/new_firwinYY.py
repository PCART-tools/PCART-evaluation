import scipy.signal
taps = scipy.signal.firwin(30, 0.3, 0.05, window='hamming', pass_zero=True, scale=True, nyq=1.0, fs=None)
