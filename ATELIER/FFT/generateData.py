import numpy as np
from numpy.random import *
import matplotlib.pyplot as plt
from numpy.fft import *

N = 200
x1 = np.linspace(-10, 10.0, N)
noise = random(N)
y1 = np.cos(2 * np.pi / 0.632 * x1)+noise
np.savetxt("hene-short-200.txt", np.transpose((x1,y1)),header="#Interferogramme He-Ne\n\n# Position\tIntensite\n\n")

spectre = fft(y1)
fig, (axes, axesFFT) = plt.subplots(2,1,figsize=(10, 7))
axes.plot(x1, y1, 'o-')
axesFFT.plot(x1, spectre, 'o-')
plt.show()


N = 2000
x1 = np.linspace(-10, 10.0, N)
noise = random(N)
y1 = np.cos(2 * np.pi / 0.632 * x1)+noise
np.savetxt("hene-short-2000.txt", np.transpose((x1,y1)),header="#Interferogramme He-Ne\n\n# Position\tIntensite\n\n")
spectre = fft(y1)
fig, (axes, axesFFT) = plt.subplots(2,1,figsize=(10, 7))
axes.plot(x1, y1, 'o-')
axesFFT.plot(x1, spectre, 'o-')
plt.show()

N = 2000
x1 = np.linspace(-100, 100, N)
noise = random(N)
y1 = np.cos(2 * np.pi / 0.632 * x1)+noise
np.savetxt("hene-long-2000.txt", np.transpose((x1,y1)),header="#Interferogramme He-Ne\n\n# Position\tIntensite\n\n")
spectre = fft(y1)
fig, (axes, axesFFT) = plt.subplots(2,1,figsize=(10, 7))
axes.plot(x1, y1, 'o-')
axesFFT.plot(x1, spectre, 'o-')
plt.show()
