import numpy as np
from numpy.random import *
import matplotlib.pyplot as plt
from numpy.fft import *

I = complex(0,1)

def readVectorsFromFile(filename):
    x = np.loadtxt(filename, usecols=(0))
    y = np.loadtxt(filename, usecols=(1))
    return (x,y)

def generatePinkNoise(dt:float, noise:float, size:int = 32768):
    N = size
    fMax = 1/dt/2
    freq = np.linspace(0, fMax, N)

    amplitude = 1/(freq**0.1+0.01)
    phase = np.random.uniform(size=N)*6.28
    spectrum = amplitude*np.exp(I*phase)
    spectrum[0] = 2*N

    intensity = irfft(spectrum)
    return intensity

def generateIntensityTrace(df:float, noise:float):
    dx = (xMax - xMin)/N
    x = np.linspace(xMin, xMax, N)
    noise = random.exponential()*0.05
    y = 1+np.cos(2 * np.pi / 0.6328 * x)+noise

    spectrum = fft(y)
    dx = x[1]-x[0] # on obtient dx, on suppose equidistant
    N = len(x)     # on obtient N directement des données
    frequencies = fftfreq(N, dx) # Cette fonction est fournie par numpy
    wavelengths = 1/frequencies  # Les fréquences en µm^-1 sont moins utiles que lambda en µm
    return (wavelengths, frequencies, spectrum)

def generateWhiteLightInterferogram(xMin, xMax, N):
    """ Genere un tableau de N valeurs equidistantes enntre xMin et xMax.
    Ensuite, genere un tableau de N valeurs qui representent un interferogramme
    d'une source blanche visible. On ajoute du bruit pour rendre le tout
    plus realiste.
    """

    dx = (xMax - xMin)/N
    xs = np.linspace(xMin, xMax, N)

    fMax = 1/dx/2
    fs = np.linspace(0, fMax, N)

    f1 = 1/0.4
    f2 = 1/0.8

    amplitude = np.exp(-(f-(f1+f2/2))**2/0.2)
    phase = np.random.uniform(size=N)*6.28
    spectrum = amplitude*np.exp(I*phase)
    spectrum[0] = 2*N

    intensity = irfft(spectrum)
    return amplitude


# dt = 0.01
# N = 32768
# intensity = generatePinkNoise(dt=0.01, noise=0.01, size=N)
# time = np.linspace(0, N*dt, 2*(N-1))

# intensity = generatePinkNoise(dt=0.01, noise=0.01, size=N)


# plt.plot(time, intensity, '-')
# plt.show()

# np.savetxt("hene.txt", intensity, header="X in seconds")

xMax = +100
xMin = -100
N = 1024

dx = (xMax - xMin)/N
xs = np.linspace(xMin, xMax, N)

fMax = 1/dx/2
fs = np.linspace(0, fMax, N)
print(fs)
print(fMax)

f1 = 1/0.4
f2 = 1/0.8
fm = np.repeat(1, N)*(f1+f2/2)

amplitude = np.exp(-(fs-fm)**2/0.2)
phase = np.random.uniform(size=N)*6.28
spectrum = amplitude*np.exp(I*phase)
spectrum[0] = 2*N

intensity = irfft(spectrum)

plt.plot(amplitude, '-')
plt.show()
