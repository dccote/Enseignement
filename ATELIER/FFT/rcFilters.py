import numpy as np
from numpy.fft import *
import matplotlib.pyplot as plt
import unittest

def write8BitPWM(value):
	intValue = int(value)
	return intValue*[1] + (256-intValue)*[0]

def pwmSineWave(baseTimeSteps, freq):

	values = []
	for i in range(0, len(baseTimeSteps), 256):
		t = baseTimeSteps[i]
		amplitude = 255*(np.sin(2*np.pi*freq*t)+1)/2
		values.extend(write8BitPWM(amplitude))

	return values

def atelier():
	plt.style.use('https://raw.githubusercontent.com/dccote/Enseignement/master/SRC/dccote-errorbars.mplstyle')

	N = 100000
	x = np.linspace(0, 1000, N)


	y = np.zeros(shape=(N,))
	amplitudes = np.random.rand(N,1)

	for i,value in enumerate(x):
		millisecond = int(value)
		if millisecond == 1:
			y[i] = 1

	plt.plot(x,y, 'k-')
	plt.xlim(0,5)
	plt.xlabel("Temps [ms]")
	plt.ylabel("Amplitude [arb.u.]")
	plt.show()


	spectrum = fft(y)
	dx = x[1]-x[0] # on obtient dx, on suppose equidistant
	frequencies = fftfreq(N, dx) # Cette fonction est fournie par numpy

	plt.plot(frequencies, abs(spectrum), 'k-')
	plt.xlim(0,5) 
	plt.xlabel("Frequences [kHz]")
	plt.ylabel("Amplitude [arb.u.]")
	plt.show()

	y = np.zeros(shape=(N,))
	amplitudes = np.random.rand(N,1)

	for i,value in enumerate(x):
		millisecond = int(value)
		y[i] = amplitudes[millisecond] 

	plt.plot(x,y, 'k-')
	plt.xlim(0,5) 
	plt.xlabel("Temps [ms]")
	plt.ylabel("Amplitude [arb.u.]")
	plt.show()


	spectrum = fft(y)
	dx = x[1]-x[0] # on obtient dx, on suppose equidistant
	frequencies = fftfreq(N, dx) # Cette fonction est fournie par numpy
	spectrumShifted = fftshift(spectrum)

	plt.plot(frequencies, abs(spectrum), 'k-')
	plt.xlim(0,5)
	plt.ylim(0,2500) 
	plt.xlabel("Frequences [kHz]")
	plt.ylabel("Amplitude [arb.u.]")
	plt.show()


class TestRCFilters(unittest.TestCase):
	def testInit(self):
		self.assertTrue(True)

	def testNumberOfLinspaceElementsNoEndpoint(self):
		N = 100

		x = np.linspace(0,1, N, endpoint=True)
		self.assertEqual(len(x), N)
		self.assertEqual(x[0], 0)
		self.assertEqual(x[N-1], 1.0)

	def testNumberOfLinspaceElementsWithEndpoint(self):
		N = 100

		x = np.linspace(0,1, N, endpoint=False)
		self.assertEqual(len(x), N)
		self.assertEqual(x[0], 0)
		self.assertEqual(x[N-1], 1.0-1/N)
		self.assertEqual(x[1]-x[0], 1/(N))

	def testPWMSineWave(self):
		N = 100*256

		x = np.linspace(0,1, N, endpoint=False)
		values = pwmSineWave(x, freq=2)
		self.assertEqual(len(values), len(x))

	def testTimeScale(self):
		N = 480*256

		x = np.linspace(0,1, N, endpoint=False)
		values = pwmSineWave(x, freq=2)
		sum = 0
		for x,y in zip(x,values):
			if x < 1/480:
				sum += y
		self.assertEqual(mean(sum), 0.5)


	def testTimeScale(self):
		N = 480*256

		x = np.linspace(0,1, N, endpoint=False)
		values = pwmSineWave(x, freq=2)
		plt.plot(x,values)
		plt.show()

	def testSpectrum(self):
		N = 480*256

		x = np.linspace(0,1, N, endpoint=False)

		values = pwmSineWave(x, freq=2)
		spectrum = fft(values)

		dx = x[1]-x[0]
		frequencies = fftfreq(N, dx)
		plt.plot(frequencies,abs(spectrum))
		plt.xlim(0,1000)
		plt.show()

	def testIdealFilter(self):
		N = 480*256

		x = np.linspace(0,1, N, endpoint=False)
		values = pwmSineWave(x, freq=2)
		spectrum = fft(values)

		dx = x[1]-x[0]
		frequencies = fftfreq(N, dx)
		filteredSpectrum = np.zeros(N,dtype=complex)

		for i, s in enumerate(spectrum):
			if abs(frequencies[i]) < 10:
				filteredSpectrum[i] = s
			else:
				filteredSpectrum[i] = 0

		filteredWave = ifft(filteredSpectrum)
		plt.plot(x, filteredWave.real)
		realSineWave = np.sin(2*np.pi*5*x)/2+0.5
		plt.show()

		self.assertTrue( np.max( abs(realSineWave-filteredWave)) < 0.03)

		# plt.plot(x, abs(realSineWave-filteredWave))
		# plt.show()

	def testRCFilter(self):

		N = 480*256

		x = np.linspace(0,1, N, endpoint=False)
		values = pwmSineWave(x, freq=2)
		spectrum = fft(values)

		dx = x[1]-x[0]
		frequencies = fftfreq(N, dx)
		filteredSpectrum = np.zeros(N,dtype=complex)


		R = 1000000
		C = 4e-6/6.28
		j = complex(0,1)
		fc = 1/R/C/2/np.pi
		response = 1/(j*2*np.pi*frequencies*C+0.0001)/(R+1/(j*2*np.pi*frequencies*C+0.0001))
		plt.title("Frequency cut-off f_c = {0:.2f} Hz".format(fc))
		plt.plot(frequencies, abs(response))
		plt.xscale('log')
		plt.yscale('log')
		plt.show()


		filteredSpectrum = response*spectrum
		filteredWave = ifft(filteredSpectrum)
		plt.title("Frequency cut-off f_c = {0:.2f} Hz".format(fc))
		plt.plot(x, filteredWave.real)
		realSineWave = np.sin(2*np.pi*5*x)/2+0.5
		plt.show()

		self.assertTrue( np.max( abs(realSineWave-filteredWave)) < 0.03)




if __name__ == "__main__":
	unittest.main()
	# # plt.style.use('https://raw.githubusercontent.com/dccote/Enseignement/master/SRC/dccote-errorbars.mplstyle')
	# systemClock = 980.39*64*256
	# pwmResolution = 256
	# pwmBaseClockFactor = 64
	# pwmUserClockFactor = pwmBaseClockFactor * pwmResolution

	# baseClock = int(systemClock/pwmBaseClockFactor)
	# userClock = int(baseClock/pwmResolution)

	# userFreq = 5 # Hz
	# Nb = int(baseClock)
	# Nu = int(userClock)

	# # tSyst = np.linspace(0,1, N)/systemClock
	# tBase = np.linspace(0,1, baseClock+1, endpoint=True)
	# tUser = np.linspace(0,1, userClock+1, endpoint=True)

	# sineWave = pwmSineWave(tUser, userFreq)
	# plt.plot(tBase, sineWave, 'k-')
	# # plt.plot(tUser, np.sin(2*np.pi*tUser/(1/nCycles))/2+0.5, 'k-.')
	# plt.show()

	# # dx = x[1]-x[0] 
	# # frequencies = fftfreq(N, dx) # Cette fonction est fournie par numpy
	# # spectrum = fft(sineWave)
	# # # spectrum = fftshift(spectrum)
	# # filteredSpectrum = np.zeros(N)
	# # N = len(spectrum)
	# # for i in range(len(spectrum)):
	# # 	f = abs(frequencies[i])
	# # 	if f == 0:
	# # 		filteredSpectrum[i] = spectrum[i]
	# # 	elif f < 100:
	# # 		filteredSpectrum[i] = spectrum[i]
	# # 	else:
	# # 		filteredSpectrum[i] = 0

	# # plt.plot(frequencies, abs(filteredSpectrum),'k-')
	# # plt.xlim(0, 1000)
	# # plt.show()

	# # # plt.plot(x, sineWave, 'k-')
	# # # plt.plot(x, np.sin(2*np.pi*x/(1/nCycles))/2+0.5, 'k-.')
	# # plt.plot(ifft(filteredSpectrum),'k-')
	# # plt.show()