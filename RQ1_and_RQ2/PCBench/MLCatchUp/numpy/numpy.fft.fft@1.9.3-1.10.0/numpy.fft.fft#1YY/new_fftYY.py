import numpy as np

def main():
    a = np.array([0, 1, 2, 3, 4])
    result = np.fft.fft(a, norm=None)
    print(result)
if __name__ == '__main__':
    main()
