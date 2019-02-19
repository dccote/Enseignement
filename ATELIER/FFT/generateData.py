import numpy as np
from numpy.random import *
import matplotlib.pyplot as plt
from numpy.fft import *

filename="hene-short-200.txt"
N = 200
xMin = -10
xMax = 10
x1 = np.linspace(xMin, xMax, N)
noise = random(N)*0.1
y1 = np.cos(2 * np.pi / 0.632 * x1)+noise

np.savetxt(filename, np.transpose((x1,y1)),header="#Interferogramme He-Ne\n\n# Position\tIntensite\n\n")

# Pour etudiants
x1 = np.loadtxt(filename, usecols=(0))
y1 = np.loadtxt(filename, usecols=(1))
spectre = fft(y1)
fig, (axes, axesFFT) = plt.subplots(2,1,figsize=(10, 7))
axes.plot(x1, y1, 'o-')
axes.set_title("Donnees")
axesFFT.plot(x1, spectre, 'o-')
axes.set_title("Spectre")
plt.show()

x1 = np.loadtxt(filename, usecols=(0))
y1 = np.loadtxt(filename, usecols=(1))
spectre = abs(fft(y1))
fig, (axes, axesFFT) = plt.subplots(2,1,figsize=(10, 7))
axes.plot(x1, y1, 'o-')
axes.set_title("Donnees")
axesFFT.plot(x1, spectre, 'o-')
axes.set_title("Spectre (valeur absolue)")
plt.show()


filename="hene-short-2000.txt"
N = 2000
xMin = -10
xMax = 10
x1 = np.linspace(xMin, xMax, N)
noise = random(N)*0.1
y1 = np.cos(2 * np.pi / 0.632 * x1)+noise
np.savetxt(filename, np.transpose((x1,y1)),header="#Interferogramme He-Ne\n\n# Position\tIntensite\n\n")

x1 = np.loadtxt(filename, usecols=(0))
y1 = np.loadtxt(filename, usecols=(1))
spectre = abs(fft(y1))
fig, (axes, axesFFT) = plt.subplots(2,1,figsize=(10, 7))
axes.plot(x1, y1, 'o-')
axes.set_title("Donnees")
axesFFT.plot(x1, spectre, 'o-')
axes.set_title("Spectre (valeur absolue)")
plt.show()

filename="hene-long-2000.txt"
xMin = -100
xMax = 100
x1 = np.linspace(xMin, xMax, N)
noise = random(N)*0.1
y1 = np.cos(2 * np.pi / 0.632 * x1)+noise
np.savetxt(filename, np.transpose((x1,y1)),header="#Interferogramme He-Ne\n\n# Position\tIntensite\n\n")

x1 = np.loadtxt(filename, usecols=(0))
y1 = np.loadtxt(filename, usecols=(1))
spectre = abs(fft(y1))
fig, (axes, axesFFT) = plt.subplots(2,1,figsize=(10, 7))
axes.plot(x1, y1, 'o-')
axesFFT.plot(x1, spectre, 'o-')
plt.show()


filename="white-2000.txt"
N = 2000
xMin = -100
xMax = 100
x1 = np.linspace(xMin, xMax, N)
noise = random(N)*0.01
y1 = np.exp(-x1*x1/4)*np.sin(2 * np.pi / 0.540 * x1)/(2 * np.pi / 0.540 * x1)+noise
np.savetxt(filename, np.transpose((x1,y1)),header="#Interferogramme He-Ne\n\n# Position\tIntensite\n\n")

x1 = np.loadtxt(filename, usecols=(0))
y1 = np.loadtxt(filename, usecols=(1))
spectre = abs(fft(y1))
fig, (axes, axesFFT) = plt.subplots(2,1,figsize=(10, 7))
axes.plot(x1, y1, 'o-')
axesFFT.plot(x1, spectre, 'o-')
plt.show()

filename="sodium-20000.txt"
N = 20000
xMin = -1500
xMax = 1500
x1 = np.linspace(xMin, xMax, N)
noise = random(N)*0.01
y1 = (np.sin(2 * np.pi / 0.589 * x1)+np.sin(2 * np.pi / 0.5896 * x1))+noise
np.savetxt(filename, np.transpose((x1,y1)),header="#Interferogramme He-Ne\n\n# Position\tIntensite\n\n")
spectre = abs(fft(y1))
fig, (axes, axesFFT) = plt.subplots(2,1,figsize=(10, 7))
axes.plot(x1, y1, '-')
axesFFT.plot(x1, spectre, '-')
plt.show()
