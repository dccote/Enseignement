import numpy as np
import matplotlib.pyplot as plt
from numpy.fft import *

hene = np.loadtxt("hene.txt", usecols=(0,1))

x1 = np.linspace(-100, 100.0, 2000)

y1 = np.cos(2 * np.pi / 0.632 * x1)
y2 = np.cos(2 * np.pi * 20 * x1) * np.exp(-x1)

y = fft(y1)

fig, (axes, axesFFT) = plt.subplots(2,1,figsize=(10, 7))

axes.plot(x1, y1, 'o-')
#axes.ylabel('Damped oscillation')
axesFFT.plot(x1, abs(y), 'o-')

plt.show()
