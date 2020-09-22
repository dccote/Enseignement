import numpy as np
from numpy.fft import *
import matplotlib.pyplot as plt

N = 1024
x = np.linspace(0, 1, N)
y = np.sin(6.28*x)

spectrum = fft(y)
dx = x[1]-x[0] # on obtient dx, on suppose equidistant
frequencies = fftfreq(N, dx) # Cette fonction est fournie par numpy
spectrumShifted = fftshift(spectrum)

plt.plot(frequencies, spectrum)
plt.show()