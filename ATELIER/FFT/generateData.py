import numpy as np
from numpy.random import *
import matplotlib.pyplot as plt
from numpy.fft import *

N = 200
xMin = -10
xMax = 10
x1 = np.linspace(xMin, xMax, N)

noise = random(N)*0.1
y1 = np.cos(2 * np.pi / 0.632 * x1)+noise
np.savetxt("hene-short-200.txt", np.transpose((x1,y1)),header="#Interferogramme He-Ne\n\n# Position\tIntensite\n\n")

x1 = np.loadtxt("hene-short-200.txt", usecols=(0))
y1 = np.loadtxt("hene-short-200.txt", usecols=(1))
spectre = fft(y1)
fig, (axes, axesFFT) = plt.subplots(2,1,figsize=(10, 7))
axes.plot(x1, y1, 'o-')
axes.set_title("Donnees")
axesFFT.plot(x1, spectre, 'o-')
axes.set_title("Spectre")
plt.show()



N = 2000
xMin = -10
xMax = 10
x1 = np.linspace(xMin, xMax, N)
noise = random(N)*0.1
y1 = np.cos(2 * np.pi / 0.632 * x1)+noise
np.savetxt("hene-short-2000.txt", np.transpose((x1,y1)),header="#Interferogramme He-Ne\n\n# Position\tIntensite\n\n")
spectre = fft(y1)
fig, (axes, axesFFT) = plt.subplots(2,1,figsize=(10, 7))
axes.plot(x1, y1, 'o-')
axesFFT.plot(x1, spectre, 'o-')
plt.show()

N = 2000
xMin = -100
xMax = 100
x1 = np.linspace(xMin, xMax, N)
noise = random(N)*0.1
y1 = np.cos(2 * np.pi / 0.632 * x1)+noise
np.savetxt("hene-long-2000.txt", np.transpose((x1,y1)),header="#Interferogramme He-Ne\n\n# Position\tIntensite\n\n")
spectre = fft(y1)
fig, (axes, axesFFT) = plt.subplots(2,1,figsize=(10, 7))
axes.plot(x1, y1, 'o-')
axesFFT.plot(x1, spectre, 'o-')
plt.show()

N = 2000
xMin = -100
xMax = 100
x1 = np.linspace(xMin, xMax, N)
noise = random(N)*0.01
y1 = np.exp(-x1*x1/4)*np.sin(2 * np.pi / 0.540 * x1)/(2 * np.pi / 0.540 * x1)+noise
np.savetxt("white-2000.txt", np.transpose((x1,y1)),header="#Interferogramme He-Ne\n\n# Position\tIntensite\n\n")
spectre = abs(fft(y1))
fig, (axes, axesFFT) = plt.subplots(2,1,figsize=(10, 7))
axes.plot(x1, y1, 'o-')
axesFFT.plot(x1, spectre, 'o-')
plt.show()


N = 20000
xMin = -1500
xMax = 1500
x1 = np.linspace(xMin, xMax, N)
noise = random(N)*0.01
y1 = (np.sin(2 * np.pi / 0.589 * x1)+np.sin(2 * np.pi / 0.5896 * x1))+noise
np.savetxt("sodium-20000.txt", np.transpose((x1,y1)),header="#Interferogramme He-Ne\n\n# Position\tIntensite\n\n")
spectre = abs(fft(y1))
fig, (axes, axesFFT) = plt.subplots(2,1,figsize=(10, 7))
axes.plot(x1, y1, '-')
axesFFT.plot(x1, spectre, '-')
plt.show()
