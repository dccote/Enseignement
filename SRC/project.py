import experiment as Exp
import numpy as np

def blackbody(T, wavelengths):
    h = 6.62e-34
    c = 3e8
    k = 1.38e-23
    I = []
    for l in wavelengths:
        f = c/(l*1e-9)
        I.append(2*h*f*f*f/c/c*(1/(np.exp(h*f/k/T)-1)))
    return I


# La classe DataFile permet de rapidement lire des données .csv
# ColumnId permet d'identifier les paires (x,y) qui forment les courbes
# S'il n'y a pas de x1, x2,... ils prennent x0
data = Exp.DataFile('ampoules.csv', columnId='x0 y0 y1 y2 y3 y4 y5 y6 y7')

for i,curve in enumerate(data.curves):
    curve.connectPoints = True
    curve.y.normalize()

x = np.linspace(350,900)
siliconResponse = x/1200
curve2700 = Exp.Curve(x, blackbody(T=3500, wavelengths=x))
curve2700.connectPoints = True
curve2700.y *= siliconResponse
curve2700.y.normalize()

# La classe Graph permet de rapidement faire un graphique raisonnable
graph = Exp.XYGraph(useColors=True)
graph.addCurve(data.curves[7])
# graph.addCurve(data.curves[1])
# graph.addCurve(data.curves[2])
# graph.addCurve(data.curves[4])
# graph.addCurve(data.curves[5])
# graph.addCurve(data.curves[6])
graph.addCurve(curve2700)
graph.xlabel = "Wavelength [nm]"
graph.ylabel = "Intensité [arb. u]"
graph.xlim = (350, 900)
graph.show()
graph.save('test.pdf')

# graphTemp = Exp.XYGraph(useColors=True)
# curve2700 = Exp.Curve(x, blackbody(T=2700, wavelengths=x))
# curve2700.connectPoints = True
# curve2700Corr = Exp.Curve(x, blackbody(T=2700, wavelengths=x))
# #curve2700Corr.y.normalize()
# curve2700Corr.y /= siliconResponse
# curve2700Corr.connectPoints = True

# curve3500 = Exp.Curve(x, blackbody(T=3500, wavelengths=x))
# curve3500.y /= siliconResponse

# curve3500.connectPoints = True

# graphTemp.addCurve(curve2700)
# graphTemp.addCurve(curve2700Corr)
# graphTemp.addCurve(curve3500)
# graphTemp.show()