import unittest
import numpy as np
from numpy.fft import *
import matplotlib.pyplot as plt

class TestFourierMethods(unittest.TestCase):

    def testLinearRange(self):
        N = 100
        xs = np.linspace(0, 1, N)
        self.assertEqual(xs[0], 0)
        self.assertEqual(xs[N-1], 1)

    def testFrequencyRange(self):
        N = 16
        xMax = 100
        xMin = -100
        dx = (xMax - xMin)/N

        fMax = 1/dx/2
        df = 1/(N*dx)
        expectedFrequencies = np.linspace(0, fMax, int(N/2), endpoint=False)
        negativeFrequencies = np.linspace(-fMax, 0, int(N/2), endpoint=False)
        expectedFrequencies = np.append(expectedFrequencies,negativeFrequencies)

        frequencies = fftfreq(N, dx) # Cette fonction est fournie par numpy

        self.assertEqual(len(expectedFrequencies), len(frequencies))
        self.assertEqual(expectedFrequencies.all(), frequencies.all())

    def testCosinewaveFFT(self):
        N =1024
        xs = np.linspace(0, 6.28, N) # sine of frequency 1 
        array = np.cos(xs)
        spectrum = fft(array)

        self.assertTrue(np.argmax(abs(spectrum)) == 1)
        self.assertAlmostEqual(abs(spectrum[1]), abs(spectrum[-1]), places=6)
        self.assertAlmostEqual(np.angle(spectrum[1]), -np.angle(spectrum[-1]), places=6)
        self.assertAlmostEqual(np.angle(spectrum[1]), 0, places=2)

    def testSinewaveFFT(self):
        N =1024
        xs = np.linspace(0, 6.28, N) # sine of frequency 1 
        array = np.sin(xs)
        spectrum = fft(array)

        self.assertTrue(np.argmax(abs(spectrum)) == 1)
        self.assertAlmostEqual(abs(spectrum[1]), abs(spectrum[-1]), places=6)
        self.assertAlmostEqual(np.angle(spectrum[1]), -np.angle(spectrum[-1]), places=6)
        self.assertAlmostEqual(np.angle(spectrum[1]), -np.pi/2, places=2)

    def testSinewaveInverseFFT(self):
        N =1024
        xs = np.linspace(0, 6.28, N) # sine of frequency 1 
        array = np.sin(xs)
        spectrum = ifft(array)

        self.assertAlmostEqual(abs(spectrum[1]), abs(spectrum[-1]), places=6)
        self.assertAlmostEqual(np.angle(spectrum[1]), -np.angle(spectrum[-1]), places=6)
        self.assertTrue(np.argmax(abs(spectrum)) == 1)

    def testCosinewaveFromSpectrum(self):
        N = 16
        xMax = 6.28
        xMin = 0
        dx = (xMax - xMin)/N

        space = np.linspace(xMin, xMax, N,endpoint=False)
        frequencies = fftfreq(N, dx)

        spectrum = [0]*N
        spectrum[1] = 0.5 # cosine amplitude of 1 total
        spectrum[-1] = 0.5
        cosine = ifft(spectrum)*N # ifft is normalized by 1/N naturally

        ratio = abs(np.real(cosine)/np.cos(space))
        self.assertAlmostEqual(ratio[0],1, places=3)
        self.assertAlmostEqual(ratio[1],1, places=3)
        self.assertAlmostEqual(ratio[2],1, places=3)

    def testLongCosineFromSpectrum(self):
        N = 2048
        cycles = 10
        xMax = 6.28*cycles
        xMin = 0
        dx = (xMax - xMin)/N

        space = np.linspace(xMin, xMax, N,endpoint=False)
        frequencies = fftfreq(N, dx)

        spectrum = [0]*N
        spectrum[cycles] = 0.5 # cosine amplitude of 1 total
        spectrum[-cycles] = 0.5
        cosine = ifft(spectrum)*N # ifft is normalized by 1/N naturally

        self.assertAlmostEqual(abs(spectrum[cycles]), abs(spectrum[-cycles]), places=6)
        self.assertAlmostEqual(np.angle(spectrum[cycles]), -np.angle(spectrum[-cycles]), places=6)

        ratio = abs(np.real(cosine)/np.cos(space))
        self.assertAlmostEqual(ratio[0],1, places=3)
        self.assertAlmostEqual(ratio[1],1, places=3)
        self.assertAlmostEqual(ratio[2],1, places=3)

    # def testLongCosineFromRealTransform(self):
    #     N = 2048
    #     cycles = 10
    #     xMax = 6.28*cycles
    #     xMin = 0
    #     dx = (xMax - xMin)/N

    #     space = np.linspace(xMin, xMax, N,endpoint=False)
    #     frequencies = fftfreq(N, dx)

    #     spectrum = [0]*N
    #     spectrum[cycles] = 0.5 # cosine amplitude of 1 total
    #     cosine = irfft(spectrum, N/2)*N # ifft is normalized by 1/N naturally
    #     self.assertEqual(len(spectrum), N/2)
    #     self.assertEqual(len(cosine), N/2)

    #     self.assertAlmostEqual(abs(spectrum[cycles]), abs(spectrum[-cycles]), places=6)
    #     self.assertAlmostEqual(np.angle(spectrum[cycles]), -np.angle(spectrum[-cycles]), places=6)

    #     ratio = abs(np.real(cosine)/np.cos(space))
    #     self.assertAlmostEqual(ratio[0],1, places=3)
    #     self.assertAlmostEqual(ratio[1],1, places=3)
    #     self.assertAlmostEqual(ratio[2],1, places=3)


    def testLongCosineInterferogramFromSpectrum(self):
        N = 2048
        cycles = 30
        xMax = 6.28*cycles
        xMin = 0
        dx = (xMax - xMin)/N

        frequencies = fftfreq(N, dx)

        spectrum = [0]*N
        spectrum[cycles] = 1 # cosine amplitude of 1 total
        spectrum[-cycles] = 1
        spectrum[int(cycles+2)] = 1 # cosine amplitude of 1 total
        spectrum[-int(cycles+2)] = 1
        spectrum = np.multiply(np.abs(spectrum),np.abs(spectrum))
        cosine = ifft(spectrum)*N # ifft is normalized by 1/N naturally

        # plt.plot(cosine, '-')
        # plt.show()


    def testLongCosineInterferogramFromSpectrumWithNoise(self):
        N = 2048
        cycles = 30
        xMax = 6.28*cycles
        xMin = 0
        dx = (xMax - xMin)/N

        frequencies = fftfreq(N, dx)

        spectrum = [0]*N
        spectrum[cycles] = 1 # cosine amplitude of 1 total
        spectrum[-cycles] = 1
        spectrum[int(cycles+2)] = 1 # cosine amplitude of 1 total
        spectrum[-int(cycles+2)] = 1
        spectrum = np.multiply(np.abs(spectrum),np.abs(spectrum))
        cosine = ifft(spectrum)*N # ifft is normalized by 1/N naturally

        cosine = np.multiply(cosine,np.random.uniform(low=0.8, high=1.2, size=N))


        # plt.plot(cosine, '-')
        # plt.show()

    def testWhiteLightInterferogramWithNoise(self):
        N =512
        xMax = -10
        xMin = 10
        xs = np.linspace(xMin, xMax, N) # sine of frequency 1 
        dx = xs[1]-xs[0]

        fmin = 1/0.4
        fmax = 1/0.8
        fm = (fmin + fmax)/2
        width = (fmax - fmin)/2

        f = fftfreq(N, dx)
        spectrum = np.exp( -((np.abs(f)-fm)/(width))**2)
        plt.plot(f, spectrum, '-')
        plt.show()

        spectrum = np.multiply(np.abs(spectrum),np.abs(spectrum))
        interferogram = ifft(spectrum)*N # ifft is normalized by 1/N naturally
        interferogram = fftshift(interferogram)
        interferogram = 60+np.multiply(interferogram,np.random.uniform(low=0.8, high=1.2, size=N))
        plt.plot(xs, np.real(interferogram), '-')
        plt.show()
        self.saveInterferogram(xs, np.real(interferogram), "lumiereBlanche")

    def testHeneShortInterferogram(self):
        N =1024
        xs = np.linspace(-20, 20, N) # sine of frequency 1 
        dx = xs[1]-xs[0]

        array = 10 + 0.5*np.cos(2*3.14/0.6328*xs)
        array = np.multiply(array,np.random.uniform(low=0.99, high=1.01, size=N))
        self.saveInterferogram(xs, array, "hene-short.txt")
        # plt.plot(array, '-')
        # plt.show()
        spectrum = fft(array)
        frequencies = fftfreq(N, dx)

    def testHeneLongInterferogram(self):
        N =1024
        xs = np.linspace(-100, 100, N) # sine of frequency 1 
        dx = xs[1]-xs[0]

        array = 10 + 0.5*np.cos(2*3.14/0.6328*xs)
        array = np.multiply(array,np.random.uniform(low=0.99, high=1.01, size=N))
        self.saveInterferogram(xs, array, "hene-long.txt")
        # plt.plot(array, '-')
        # plt.show()
        spectrum = fft(array)
        frequencies = fftfreq(N, dx)

    def testHeneLongEquipe1Interferogram(self):
        N =20022
        dx = 0.2
        xs = np.linspace(-N*dx/2, N*dx/2, N, endpoint=False)

        array = 10 + 0.5*np.cos(2*3.14/0.6328*xs)
        array = np.multiply(array,np.random.uniform(low=0.99, high=1.01, size=N))
        self.saveInterferogram(xs, array, "hene-equipe1.txt")
        plt.plot(array, '-')
        plt.show()
        spectrum = fft(array)
        frequencies = fftfreq(N, dx)

    def testMercuryLampEquipe1Interferogram(self):
        N = 13555
        dx = 0.2
        xs = np.linspace(-N*dx/2, N*dx/2, N, endpoint=False)

        array = 10 + 0.5*np.cos(2*3.14/0.579*xs) + 0.8*np.cos(2*3.14/0.546*xs) + 1.0*np.cos(2*3.14/0.436*xs)
        array = np.multiply(array,np.random.uniform(low=0.9, high=1.1, size=N))
        self.saveInterferogram(xs, array, "mercure-equipe1.txt")
        plt.plot(array, '-')
        plt.show()
        spectrum = fft(array)
        frequencies = fftfreq(N, dx)

    def testWhiteLightInterferogramEquipe1WithNoise(self):
        N = 71150
        dx = 0.2
        xs = np.linspace(-N*dx/2, N*dx/2, N, endpoint=False)

        fmin = 1/0.4
        fmax = 1/0.8
        fm = (fmin + fmax)/2
        width = (fmax - fmin)/2

        f = fftfreq(N, dx)
        spectrum = np.exp( -((np.abs(f)-fm)/(width))**2)
        plt.plot(f, spectrum, '-')
        plt.show()

        spectrum = np.multiply(np.abs(spectrum),np.abs(spectrum))
        interferogram = ifft(spectrum)*N # ifft is normalized by 1/N naturally
        interferogram = fftshift(interferogram)
        interferogram = 60+np.multiply(interferogram,np.random.uniform(low=0.8, high=1.2, size=N))
        plt.plot(xs, np.real(interferogram), '-')
        plt.show()
        self.saveInterferogram(xs, np.real(interferogram), "lumiereBlanche-equipe1.txt")

    def testHeneLongEquipe2Interferogram(self):
        N =10500
        dx = 0.2
        xs = np.linspace(-N*dx/2, N*dx/2, N, endpoint=False)

        array = 10 + 0.5*np.cos(2*3.14/0.6328*xs)
        array = np.multiply(array,np.random.uniform(low=0.99, high=1.01, size=N))
        self.saveInterferogram(xs, array, "hene-equipe2.txt")
        plt.plot(array, '-')
        plt.show()
        spectrum = fft(array)
        frequencies = fftfreq(N, dx)

    def testMercuryLampEquipe2Interferogram(self):
        N = 5000
        dx = 0.2
        xs = np.linspace(-N*dx/2, N*dx/2, N, endpoint=False)

        array = 10 + 0.5*np.cos(2*3.14/0.579*xs) + 0.8*np.cos(2*3.14/0.546*xs) + 1.0*np.cos(2*3.14/0.436*xs)
        array = np.multiply(array,np.random.uniform(low=0.99, high=1.01, size=N))
        self.saveInterferogram(xs, array, "mercure-equipe2.txt")
        plt.plot(array, '-')
        plt.show()
        spectrum = fft(array)
        frequencies = fftfreq(N, dx)

    def testWhiteLightInterferogramEquipe2WithNoise(self):
        N = 71150
        dx = 0.2
        xs = np.linspace(-N*dx/2, N*dx/2, N, endpoint=False)

        fmin = 1/0.4
        fmax = 1/0.8
        fm = (fmin + fmax)/2
        width = (fmax - fmin)/2

        f = fftfreq(N, dx)
        spectrum = np.exp( -((np.abs(f)-fm)/(width))**2)
        plt.plot(f, spectrum, '-')
        plt.show()

        spectrum = np.multiply(np.abs(spectrum),np.abs(spectrum))
        interferogram = ifft(spectrum)*N # ifft is normalized by 1/N naturally
        interferogram = fftshift(interferogram)
        interferogram = 60+np.multiply(interferogram,np.random.uniform(low=0.8, high=1.2, size=N))
        plt.plot(xs, np.real(interferogram), '-')
        plt.show()
        self.saveInterferogram(xs, np.real(interferogram), "lumiereBlanche-equipe2.txt")


    def testMercuryLampInterferogram(self):
        N =1024
        xs = np.linspace(-100, 100, N) # sine of frequency 1 
        dx = xs[1]-xs[0]

        array = 10 + 0.5*np.cos(2*3.14/0.579*xs) + 0.8*np.cos(2*3.14/0.546*xs) + 1.0*np.cos(2*3.14/0.436*xs)
        array = np.multiply(array,np.random.uniform(low=0.9, high=1.1, size=N))
        self.saveInterferogram(xs, array, "mercure.txt")
        # plt.plot(array, '-')
        # plt.show()
        spectrum = fft(array)
        frequencies = fftfreq(N, dx)

    def testSodiumLampInterferogram(self):
        N =30000
        dx = 0.05
        xs = np.linspace(0, N*dx, N) # sine of frequency 1 
        

        array = 2 + 0.5*np.cos(3.14/0.589*xs) + 0.5*np.cos(3.14/0.5896*xs) 
        array = np.multiply(array,np.random.uniform(low=0.99, high=1.01, size=N))
        self.saveInterferogram(xs, array, "sodium-short.txt")
        # plt.plot(array, '-')
        # plt.show()
        spectrum = fft(array)
        frequencies = fftfreq(N, dx)

        # plt.plot(frequencies, abs(spectrum), '-')
        # plt.show()

        # self.assertTrue(np.argmax(abs(spectrum)) == 1)
        # self.assertAlmostEqual(abs(spectrum[1]), abs(spectrum[-1]), places=6)
        # self.assertAlmostEqual(np.angle(spectrum[1]), -np.angle(spectrum[-1]), places=6)
        # self.assertAlmostEqual(np.angle(spectrum[1]), 0, places=2)

    def testSaveTxt(self):
        N =1024
        xs = np.linspace(-100, 100, N) # sine of frequency 1 
        y = 10 + 0.5*np.cos(2*3.14/0.579*xs) + 0.8*np.cos(2*3.14/0.546*xs) + 1.0*np.cos(2*3.14/0.436*xs)
        self.saveInterferogram(xs, y, "test.txt")



    def saveInterferogram(self, x, intensity, filename):
        np.savetxt(filename, np.stack((x, intensity), axis=1),delimiter="\t", header='CheminTotalEnMicrons\tIntensite')


if __name__ == '__main__':
    unittest.main()
