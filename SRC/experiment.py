import csv
from typing import List

import matplotlib.pyplot as plt
import numpy as np
from numpy.polynomial import Polynomial

""" Une classe DataFile pour lire les données de fichiers CSV et
une class XYGraph pour voir et sauvegarder un graphique. A utiliser
comme suit:

import experiment as Exp

# La classe DataFile permet de rapidement lire des données .csv
# On utilise columnId pour rapidement assigner quelle colonne va
# avec quelle autre colonne pour les graphiques. On aura donc 
# rapidement accès à curves[0],curves[1],etc...
data = Exp.DataFile('data.csv', columnId='x0 y0 y1 dy0 dy1')
print(data.columns[0]) #Premiere colonne
print(data.columns[1]) #Deuxieme colonne...
print(data.x) #Synonyme de columns[0]
print(data.y) #Synonyme de columns[1]

# La classe XYGraph permet de rapidement faire un graphique raisonnable
graph = Exp.XYGraph(data)
graph.xlabel = "Courant [mA]"
graph.ylabel = "Intensité [arb. u]"
graph.show()
graph.save('test.pdf')

"""


class Curve:
    def __init__(self, x=None, y=None, dx=None, dy=None):
        self.label = ""
        self.connectPoints = False
        self.isVisible = True
        self.x = Column(x) if x is not None else None
        self.y = Column(y) if y is not None else None
        self.dx = Column(dx) if dx is not None else None
        self.dy = Column(dy) if dy is not None else None

    def hide(self):
        self.isVisible = False

    def show(self):
        self.isVisible = True

    @property
    def hasXErrorBars(self):
        return self.dx is not None

    @property
    def hasYErrorBars(self):
        return self.dy is not None

    def setXErrorTo(self, percent=None, value=None):
        if percent is not None:
            self.dx = self.x * percent
        elif value is not None:
            self.dx = [value] * len(self.x)

    def setYErrorTo(self, percent=None, value=None):
        if percent is not None:
            self.dy = self.x * percent
        elif value is not None:
            self.dy = [value] * len(self.y)

    def __repr__(self):
        return "{0}±{1} {2}±{3}".format(self.x, self.dx, self.y, self.dy)


class Fit(Curve):
    def __init__(self, relation, degree):
        N = 100
        xs = np.linspace(min(relation.x), max(relation.x), N)
        polynomial = Polynomial.fit(relation.x, relation.y, deg=degree)
        ys = polynomial(xs)
        Curve.__init__(self, x=xs, y=ys)

        self.connectPoints = True
        self.label = self.latexPolynomial(polynomial.coef)
        self.degree = degree
        self.N = N

    def latexPolynomial(self, coefficients):
        formatStrings = ["{0:.2g}", "{0:.2g}x", "{0:.2g}x^{1}", "{0:.2g}x^{1}", "{0:.2g}x^{1}", "{0:.2g}x^{1}",
                         "{0:.2g}x^{1}", "{0:.2g}x^{1}"]
        formatStringsWhenCoefIs1 = ["{0:.2g}", "x", "x^{1}", "x^{1}", "x^{1}", "x^{1}", "x^{1}", "x^{1}"]
        terms = []
        for i, a in enumerate(coefficients):
            if abs(a - 1) > 1e-3:
                terms.append(formatStrings[i].format(a, i))
            else:
                terms.append(formatStringsWhenCoefIs1[i].format(a, i))

        return "${0}$".format("+".join(terms))

class Function(Curve):
    def __init__(self, xs, function, label=None):
        ys = function(xs)
        Curve.__init__(self, x=xs, y=ys)
        self.function = function
        self.connectPoints = True
        self.label = label


class Column(np.ndarray):
    """
    We want to have an array but with a few extra properties (role and label). For this, we subclass
    np.array.  This requires some care and is explained here: https://np.org/doc/stable/user/basics.subclassing.html
    """
    def __new__(cls, input_array, label=None, role=None):
        # Input array is an already formed ndarray instance
        # We first cast to be our class type
        obj = np.asarray(input_array).view(cls)
        # add the new attribute to the created instance
        obj.label = label if label is not None else ""
        obj.role = role
        # Finally, we must return the newly created object:
        return obj

    def __array_finalize__(self, obj):
        if obj is None: return
        self.label = getattr(obj, 'label', None)
        self.role = getattr(obj, 'role', None)

    def normalize(self):
        maxValue = max(self)
        self /= maxValue


class DataFile:
    def __init__(self, filepath, columnId=None):
        self.filepath = filepath
        self.headers = []
        self.rows = self.readRows(self.filepath)
        self.columns = self.extractColumns(self.rows)
        self.dictionary = self.classifyColumns(columnId)
        self.curves = self.extractCurves(self.columns)
        self.iteration = 0

    def readRows(self, filepath):
        rows = []
        with open(filepath) as csvfile:
            dialect = csv.Sniffer().sniff(csvfile.read(1024))
            csvfile.seek(0)
            if csv.Sniffer().has_header(csvfile.read(1024)):
                csvfile.seek(0)
                self.headers = csvfile.readline().split(',')
            else:
                csvfile.seek(0)
            fileReader = csv.reader(csvfile, dialect,
                                    quoting=csv.QUOTE_NONNUMERIC)

            for row in fileReader:
                rows.append(row)
        return rows

    def extractColumns(self, rows):
        nColumns = len(rows[0])
        columns = []
        for index in range(nColumns):
            data = []
            label = None
            for row in rows:
                data.append(row[index])

            if len(self.headers) != 0:
                label = self.headers[index]

            column = Column(data,label=label)

            columns.append(column)
        return columns

    def classifyColumns(self, identification):
        dict = {}
        for i, role in enumerate(identification.split()):
            self.columns[i].role = role
            if len(self.columns[i].label) == 0:
                self.columns[i].label = role
            dict[role] = self.columns[i]
        return dict

    def extractCurves(self, cols):
        curves: List[Curve] = []
        for c in range(10):
            curve = self.buildCurve(c)
            if curve is not None:
                curves.append(curve)
        return curves

    def buildCurve(self, index):
        curve = Curve()
        curve.y = self.dictionary.get("y{0}".format(index))
        if curve.y is None:
            return None

        curve.x = self.dictionary.get("x{0}".format(index))
        if curve.x is None:
            curve.x = self.dictionary.get("x0")

        curve.dx = self.dictionary.get("dx{0}".format(index))
        curve.dy = self.dictionary.get("dy{0}".format(index))
        curve.label = "{0}".format(curve.y.label)

        return curve

    @property
    def x(self):
        return self.dictionary.get('x0')

    @property
    def y(self):
        return self.dictionary.get('y0')


class XYGraph:
    def __init__(self, datafile=None, useColors=False):
        SMALL_SIZE = 11
        MEDIUM_SIZE = 13
        BIGGER_SIZE = 36

        plt.rc('font', size=SMALL_SIZE)  # controls default text sizes
        plt.rc('axes', titlesize=SMALL_SIZE)  # fontsize of the axes title
        plt.rc('axes', labelsize=MEDIUM_SIZE)  # fontsize of the x and y labels
        plt.rc('xtick', labelsize=SMALL_SIZE)  # fontsize of the tick labels
        plt.rc('ytick', labelsize=SMALL_SIZE)  # fontsize of the tick labels
        plt.rc('legend', fontsize=SMALL_SIZE)  # legend fontsize
        plt.rc('figure', titlesize=BIGGER_SIZE)  # fontsize of the figure title

        self.linewidth = 1  # Set to 1 or 2 to connect the dots
        self.markersize = 7
        self.fig, self.axes = plt.subplots(figsize=(6, 5))
        self.xlim = None
        self.xlabel = "X"
        self.ylabel = "Y"

        self.curves = []
        if datafile is not None:
            self.curves.extend(datafile.curves)

        self.useColors = useColors
        self.symbolsBlackAndWhite = [{"marker": 'o', 'color': 'k'},
                   {"marker": 'o', 'color': 'k', "markerfacecolor": 'none'},
                   {"marker": 's', 'color': 'k'},
                   {"marker": 's', 'color': 'k', "markerfacecolor": 'none'},
                   {"marker": 'v', 'color': 'k'},
                   {"marker": 'v', 'color': 'k', "markerfacecolor": 'none'},
                   {"marker": 'D', 'color': 'k'},
                   {"marker": 'D', 'color': 'k', "markerfacecolor": 'none'}
                   ]
        self.symbolsColors = [{"marker": 'o', 'color': 'k'},
                   {"marker": 'o', 'color': 'r'},
                   {"marker": 'o', 'color': 'b'},
                   {"marker": 's', 'color': 'g'},
                   {"marker": 'o', 'color': 'k', "markerfacecolor": 'none'},
                   {"marker": 'o', 'color': 'r', "markerfacecolor": 'none'},
                   {"marker": 's', 'color': 'b', "markerfacecolor": 'none'},
                   {"marker": 's', 'color': 'g', "markerfacecolor": 'none'}
                   ]
        self.linesBlackAndWhite = [{"linestyle": '-', 'color': 'k'},
                   {"linestyle": '--', 'color': 'k'},
                   {"linestyle": '-.', 'color': 'k'},
                   {"linestyle": 'dotted', 'color': 'k'},
                   {"linestyle": ':', 'color': 'k', "markerfacecolor": 'none'},
                   {"linestyle": '--', 'color': 'k', "markerfacecolor": 'none'},
                   {"linestyle": '-.', 'color': 'k', "markerfacecolor": 'none'},
                   {"linestyle": '-', 'color': 'k', "markerfacecolor": 'none'}
                   ]
        self.linesColors = [{"linestyle": '-', 'color': 'k'},
                   {"linestyle": '-', 'color': 'r'},
                   {"linestyle": '-', 'color': 'b'},
                   {"linestyle": '-', 'color': 'g'},
                   {"linestyle": '--', 'color': 'k', "markerfacecolor": 'none'},
                   {"linestyle": '--', 'color': 'r', "markerfacecolor": 'none'},
                   {"linestyle": '--', 'color': 'b', "markerfacecolor": 'none'},
                   {"linestyle": '--', 'color': 'g', "markerfacecolor": 'none'}
                   ]

    def add(self, x, y, dx=None, dy=None):
        self.curves.append(Curve(x, y, dx, dy))

    def addCurve(self, curve):
        self.curves.append(curve)

    def addCurves(self, curves):
        self.curves.extend(curves)

    def createFigure(self):
        self.axes.cla()
        self.axes.set(xlabel=self.xlabel, ylabel=self.ylabel, title="")

        if self.useColors:
            symbols = self.symbolsColors
            lines = self.linesColors
        else:
            symbols = self.symbolsBlackAndWhite
            lines = self.linesBlackAndWhite

        for i, curve in enumerate(self.curves):
            if not curve.isVisible:
                continue

            if not curve.hasXErrorBars and not curve.hasYErrorBars:
                if curve.connectPoints:
                    self.axes.plot(curve.x, curve.y,
                                   **lines[i],markersize=0,
                                   linewidth=self.linewidth,
                                   label=curve.label)
                else:
                    self.axes.plot(curve.x, curve.y, **symbols[i],
                                   markersize=self.markersize,
                                   linestyle='',
                                   linewidth=1,
                                   label=curve.label)
            elif curve.hasXErrorBars and curve.hasYErrorBars:
                self.axes.errorbar(curve.x, curve.y,
                                   xerr=list(curve.dx), yerr=list(curve.dy),
                                   **(symbols[i]),
                                   markersize=self.markersize,
                                   linestyle='',
                                   linewidth=1,
                                   label=curve.label,
                                   capsize=self.markersize / 2)
            elif curve.hasYErrorBars:
                self.axes.errorbar(curve.x, curve.y,
                                   yerr=list(curve.dy),
                                   **(symbols[i]),
                                   markersize=self.markersize,
                                   linestyle='',
                                   linewidth=1,
                                   label=curve.label,
                                   capsize=self.markersize / 2)
            elif curve.hasXErrorBars:
                self.axes.errorbar(curve.x, curve.y,
                                   xerr=list(curve.dx),
                                   **(symbols[i]),
                                   markersize=self.markersize,
                                   linestyle='',
                                   linewidth=1,
                                   label=curve.label,
                                   capsize=self.markersize / 2)
        if self.xlim is not None:
            plt.xlim(self.xlim)

        if len(self.curves) >= 2:
            self.axes.legend()

    def show(self):
        self.createFigure()
        plt.show()

    def save(self, filepath):
        self.createFigure()
        self.fig.savefig(filepath, dpi=600)


def someFunction(x):
    return (x/10-1)**2

if __name__ == "__main__":
    # A Comma-separated vairable file (CSV) can be read easily.
    # Use columnId to identify the columns and assign the curves: you determine
    # which column is x for curve 0, x for curve 1, etc...
    # For each curve, you have x0 y0 dx0 dy0 for x,y and uncertainty (x1 y1 dx1 dy1, etc...).
    # If you don't define x1, x2, x3.... with y1, y2 and y3, it will use the same x0
    data = DataFile('data.csv', columnId="x0 y0 y1 dx0 dy0")

    # You can easily access the curves from the data file, and then change their properties
    curve0, curve1 = data.curves
    curve0.label = "First curve"
    curve1.label = "Other curve"
    # curve0.hide() # You can choose to hide a certain curve
    # curve0.show()

    # You can fit a polynomial to your data
    curveFit = Fit(data.curves[1], degree=2)

    # You create a XYGraph to plot your curves.  By passing a DataFile,
    # you automatically add all curves to the graph
    graph = XYGraph(data)

    # You can then add a separate curve fit
    graph.addCurve(curveFit)

    # Change some properties
    graph.ylabel = "Intensity"
    graph.xlabel = "Current"
    graph.show()
    graph.save("figure1.pdf")

    # Create another graph
    graph2 = XYGraph()
    # Create a function curve: no data points, just a function.
    x = Column(np.linspace(0,20,500))
    # You can use a lambda function
    curveFct1 = Function(x, (lambda x: np.sin(x*x/10) + 3), label="$x^2-x+ 1$")
    graph2.addCurve(curveFct1)
    # You can use a single function defined by the system,
    curveFct2 = Function(x, np.sqrt, label="$\sqrt{x}$")
    graph2.addCurve(curveFct2)
    # You can use your own custom function that accepts a single argument
    curveFct3 = Function(x, someFunction, label="$(x-10)^2$")
    graph2.addCurve(curveFct3)

    graph2.ylabel = "Electric field [a.u.]"
    graph2.xlabel = "Time [s]"
    graph2.show()
    graph2.save("figure2.pdf")
