import numpy as np
from numpy.random import *
import matplotlib.pyplot as plt
from numpy.fft import *

""" Ce script genere des interferogrammes tels qu'obtenus avec un interferometre de Michelson 
dans le but d'etudier la transformée de Fourier et de comprendre comment la resolution est 
déterminée.
"""


# Parametres de generation

def genererXVecteur(xMin, xMax, N):
	dx = (xMax - xMin)/N
	x = np.linspace(xMin, xMax, N)
	return x

def lireVecteursSurDisque(filename):
	x = np.loadtxt(filename, usecols=(0))
	y = np.loadtxt(filename, usecols=(1))
	return (x,y)

def transformeDeFourier(x,y):
	spectre = abs(fft(y))
	dx = x[1]-x[0]
	N = len(x)
	frequencies = fftfreq(N, dx)
	wavelengths = 1/frequencies
	return (wavelengths, frequencies, spectre)

def genereHeNeInterferogramme(x):
	noise = random(len(x))*0.1
	y = np.cos(2 * np.pi / 0.632 * x)+noise
	return y

def plotCombinedFigures(x, y, w, s, title="", left=500, right=800):
	fig, (axes, axesFFT) = plt.subplots(2,1,figsize=(10, 7))
	axes.plot(x, y, '-')
	axes.set_title("Interferogramme")
	axesFFT.plot(w*1000, s, '-')
	axesFFT.set_xlim(left=left, right=right)
	axesFFT.set_xlabel("Longueur d'onde [nm]")
	axes.set_title(title)
	plt.show()


# Basse resolution
x = genererXVecteur(xMin=-10, xMax=10, N=200)
y = genereHeNeInterferogramme(x)
(w, f, s)  = transformeDeFourier(x,y)
df = f[1]-f[0]
dl = 0.6328*df*df*1000
plotCombinedFigures(x,y,w,s,left=600, right=650, title="Spectre basse resolution {0:0.4f} nm".format(dl))

# Haute resolution
# Resolution ∆f = 1/(200 µm * 2000)
x = genererXVecteur(xMin=-100, xMax=100, N=2000)
y = genereHeNeInterferogramme(x)
(w, f, s) = transformeDeFourier(x,y)
df = f[1]-f[0]
dl = 0.6328*df*df*1000
plotCombinedFigures(x,y,w,s,left=600, right=650, title="Spectre haute resolution {0:0.4f} nm".format(dl))


# Tres haute resolution
# Resolution ∆f = 1/(2000 µm * 2000)
# Resolution @ 632.8 nm : ∆lambda = 632.8 * ∆f^2 
x = genererXVecteur(xMin=-1000, xMax=1000, N=20000)
y = genereHeNeInterferogramme(x)
(w, f, s) = transformeDeFourier(x,y)
df = f[1]-f[0]
dl = 0.6328*df*df*1000
plotCombinedFigures(x,y,w,s,left=625, right=640, title="Spectre tres haute resolution {0:0.4f} nm".format(dl))



# Lecture des donnees et axes

# Generer la figure

# Parametres de generation
filename="hene-short-2000.txt"
N = 2000
xMin = -10
xMax = 10
x1 = np.linspace(xMin, xMax, N)
y1 = np.cos(2 * np.pi / 0.632 * x1)+noise
np.savetxt(filename, np.transpose((x1,y1)),header="#Interferogramme He-Ne\n\n# Position\tIntensite\n\n")


# Lecture des donnees et axes
x1 = np.loadtxt(filename, usecols=(0))
y1 = np.loadtxt(filename, usecols=(1))
spectre = abs(fft(y1))
fig, (axes, axesFFT) = plt.subplots(2,1,figsize=(10, 7))
axes.plot(x1, y1, '-')
axes.set_title("Donnees")
axesFFT.plot(spectre, '-')
axes.set_title("Spectre (valeur absolue)")
plt.show()

# Generer la figure
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
axes.plot(x1, y1, '-')
axesFFT.plot(spectre, '-')
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
axes.plot(y1, '-')
axesFFT.plot(spectre, '-')
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
axesFFT.plot(spectre, '-')
plt.show()
