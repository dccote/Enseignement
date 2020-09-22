import numpy as np
from numpy.fft import *
import matplotlib.pyplot as plt

N = 1024
x = np.linspace(0, 1, N)
y = np.sin(6.28*x)

plt.plot(y)
plt.show()

spectrum = fft(y)
plt.plot(abs(spectrum))
plt.show()