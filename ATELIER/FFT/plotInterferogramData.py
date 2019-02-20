import numpy as np
from numpy.random import *
import matplotlib.pyplot as plt
from numpy.fft import *

""" Ce script genere des interferogrammes tels qu'obtenus avec un interferometre
de Michelson dans le but d'etudier la transformée de Fourier et de comprendre 
comment la resolution spectrale est déterminée.
"""

def readVectorsFromFile(filename):
	x = np.loadtxt(filename, usecols=(0))
	y = np.loadtxt(filename, usecols=(1))
	return (x,y)

def generateHeNeInterferogram(xMin, xMax, N):
	""" Genere un tableau de N valeurs equidistantes enntre xMin et xMax.
	Ensuite, genere un tableau de N valeurs qui representent un interferogramme
	d'un laser He-Ne a 0.6328 microns. On ajoute du bruit pour rendre le tout
	plus realiste.
	"""
	dx = (xMax - xMin)/N
	x = np.linspace(xMin, xMax, N)
	noise = random(len(x))*0.05
	y = 1+np.cos(2 * np.pi / 0.6328 * x)+noise
	return (x,y)

def generateWhiteLightInterferogram(xMin, xMax, N):
	""" Genere un tableau de N valeurs equidistantes enntre xMin et xMax.
	Ensuite, genere un tableau de N valeurs qui representent un interferogramme
	d'une source blanche visible. On ajoute du bruit pour rendre le tout
	plus realiste.
	"""
	dx = (xMax - xMin)/N
	x = np.linspace(xMin, xMax, N)
	noise = random(len(x))*0.05
	k1 = 1/0.4
	k2 = 1/0.8
	y = 1+np.exp(-x*x/4)*(np.sin(2 * np.pi * (k1+k2)*x/2)/x * np.sin(2 * np.pi * (k1-k2)*x/2)+ noise)
	return (x,y)

def fourierTransformInterferogram(x,y):
	""" A partir du tableau de valeurs Y correspondant a l'abscisse X, 
	la transformée de Fourier est calculée et l'axes des fréquences (f en 
	µm^-1) et des wavelengths (1/f en microns) est retournée.

	Le spectre est un ensemble de valeurs complexes pour lesquelles l'amplitude
	et la phase sont pertinentes: l'ordre des valeurs commence par la valeur DC (0)
	et monte jusqu'a f_max=1/2/∆x par resolution de ∆f = 1/N/∆x. A partir de la
	(N/2) ieme valeur, la frequence est negative jusqu'a -∆f dans la N-1 case.
	Voir 
	https://github.com/dccote/Enseignement/blob/master/HOWTO/HOWTO-Transformes%20de%20Fourier%20discretes.pdf 
	"""
	spectrum = fft(y)
	dx = x[1]-x[0] # on obtient dx, on suppose equidistant
	N = len(x)     # on obtient N directement des données
	frequencies = fftfreq(N, dx) # Cette fonction est fournie par numpy
	wavelengths = 1/frequencies  # Les fréquences en µm^-1 sont moins utiles que lambda en µm
	return (wavelengths, frequencies, spectrum)

def plotCombinedFigures(x, y, w, s, title="", left=400, right=800):
	""""
	On met l'interferogramme et le spectre sur la meme page.
	"""
	fig, (axes, axesFFT) = plt.subplots(2,1,figsize=(10, 7))
	axes.plot(x, y, '-')
	axes.set_title("Interferogramme")
	axesFFT.plot(w*1000, abs(s), 'o-')
	axesFFT.set_xlim(left=left, right=right)
	axesFFT.set_xlabel("Longueur d'onde [nm]")
	axesFFT.set_title(title)
	plt.show()


# Basse resolution
(x,y) = generateHeNeInterferogram(xMin=-10, xMax=10, N=200) # en microns
(w, f, s)  = fourierTransformInterferogram(x,y)
df = f[1]-f[0]
dl = 0.6328*0.6328*df*1000 # x 1000 pour nm
plotCombinedFigures(x,y,w,s,left=632.8-5*dl, right=632.8+5*dl, title="Spectre He-Ne basse resolution {0:0.2f} nm".format(dl))

# Haute resolution
# Resolution ∆f = 1/(200 µm * 2000)
# Resolution @ 632.8 nm : ∆lambda = 632.8^2 * ∆f car ∆lambda/lambda = ∆f/f.
(x,y) = generateHeNeInterferogram(xMin=-100, xMax=100, N=2000) # en microns
(w, f, s) = fourierTransformInterferogram(x,y)
df = f[1]-f[0]
dl = 0.6328*0.6328*df*1000
plotCombinedFigures(x,y,w,s,left=632.8-5*dl, right=632.8+5*dl, title="Spectre He-Ne haute resolution {0:0.2f} nm".format(dl))


# Tres haute resolution
# Resolution ∆f = 1/(2000 µm * 2000)
# Resolution @ 632.8 nm : ∆lambda = 632.8^2 * ∆f 
(x,y) = generateHeNeInterferogram(xMin=-1000, xMax=1000, N=20000) # en microns
(w, f, s) = fourierTransformInterferogram(x,y)
df = f[1]-f[0]
dl = 0.6328*0.6328*df*1000
plotCombinedFigures(x,y,w,s,left=632.8-5*dl, right=632.8+5*dl, title="Spectre He-Ne tres haute resolution {0:0.2f} nm".format(dl))


# Hyper haute resolution
# Resolution ∆f = 1/(20000 µm * 20000)
# Resolution @ 632.8 nm : ∆lambda = 632.8^2 * ∆f 
(x,y) = generateHeNeInterferogram(xMin=-10000, xMax=10000, N=200000) # en microns
(w, f, s) = fourierTransformInterferogram(x,y)
df = f[1]-f[0]
dl = 0.6328*0.6328*df*1000
plotCombinedFigures(x,y,w,s,left=632.8-5*dl, right=632.8+5*dl, title="Spectre He-Ne hyper haute resolution {0:0.2f} nm".format(dl))


# Spectre de lumiere blanche
# Resolution ∆f = 1/(20000 µm * 20000)
# Resolution @ 500 nm : ∆lambda = 500^2 * ∆f 
(x,y) = generateWhiteLightInterferogram(xMin=-100, xMax=100, N=20000) # en microns
(w, f, s)  = fourierTransformInterferogram(x,y)
df = f[1]-f[0]
dl = 0.500*0.500*df*1000 # resolution autour de 0.500 µm en nm
plotCombinedFigures(x,y,w,s,left=0, right=2000, title="Spectre lumiere blanche, resolution {0:0.2f} nm".format(dl))

