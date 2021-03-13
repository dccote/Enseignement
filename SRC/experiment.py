import csv
import re
from typing import List

import matplotlib.pyplot as plt
import numpy
from numpy.polynomial import Polynomial

""" Une classe DataFile pour lire les données de fichiers CSV et
une class Graph pour voir et sauvegarder un graphique. A utiliser
comme suit:

import experiment as Exp

# La classe DataFile permet de rapidement lire des données .csv
data = Exp.DataFile('data.csv')
print(data.columns[0]) #Premiere colonne
print(data.columns[1]) #Deuxieme colonne...
print(data.x) #Synonyme de columns[0]
print(data.y) #Synonyme de columns[1]

# La classe Graph permet de rapidement faire un graphique raisonnable
graph = Exp.Graph(x=data.x, y=data.y)
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
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy

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
        xs = numpy.linspace(min(relation.x), max(relation.x), N)
        polynomial = Polynomial.fit(relation.x, relation.y, deg=degree)
        ys = polynomial(xs)
        Curve.__init__(self, x=xs, y=ys)

        self.connectPoints = True
        self.label = self.latexString(polynomial)
        self.degree = degree
        self.N = N

    def latexString(self, p):
        """ Small function to print nicely the polynomial p as we write it in maths, in LaTeX code. Obtained from:
        https://perso.crans.org/besson/publis/notebooks/Demonstration%20of%20numpy.polynomial.Polynomial%20and%20nice
        %20display%20with%20LaTeX%20and%20MathJax%20(python3).html
        """
        coefs = p.coef  # List of coefficient, sorted by increasing degrees
        res = ""  # The resulting string
        for i, a in enumerate(coefs):
            if int(a) == a:  # Remove the trailing .0
                a = int(a)
            if i == 0:  # First coefficient, no need for X
                if a > 0:
                    res += "{a:.2g} + ".format(a=a)
                elif a < 0:  # Negative a is printed like (a)
                    res += "({a:.2g}) + ".format(a=a)
                # a = 0 is not displayed
            elif i == 1:  # Second coefficient, only X and not X**i
                if a == 1:  # a = 1 does not need to be displayed
                    res += "x + "
                elif a > 0:
                    res += "{a:.2g}x + ".format(a=a)
                elif a < 0:
                    res += "({a:.2g})x + ".format(a=a)
            else:
                if a == 1:
                    # A special care needs to be addressed to put the exponent in {..} in LaTeX
                    res += "x^{i} + ".format(i="{%d}" % i)
                elif a > 0:
                    res += "{a:.2g}x^{i} + ".format(a=a, i="{%d}" % i)
                elif a < 0:
                    res += "({a:.2g})x^{i} + ".format(a=a, i="{%d}" % i)
        return "$" + res[:-3] + "$" if res else ""


class Column:
    def __init__(self, values):
        self.values = values
        self.label = ""
        self.role = None
        self.iteration = 0

    def __repr__(self):
        return "{0}".format(self.values)

    def __len__(self):
        return len(self.values)

    def __getitem__(self, index):
        return self.values[index]

    def __setitem__(self, value, index):
        self.values[index] = value

    def __iter__(self):
        self.iteration = 0
        return self

    def __next__(self):
        try:
            v = self.values[self.iteration]
            self.iteration += 1
            return v
        except Exception:
            raise StopIteration()


class DataFile:
    def __init__(self, filepath, identification=None):
        self.filepath = filepath

        self.rows = self.readRows(self.filepath)
        self.columns = self.extractColumns(self.rows)
        self.dictionary = self.classifyColumns(identification)
        self.curves = self.extractCurves(self.columns)

        self.iteration = 0

    def readRows(self, filepath):
        rows = []
        with open(filepath) as csvfile:
            dialect = csv.Sniffer().sniff(csvfile.read(1024))
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
            for row in rows:
                element = row[index]
                data.append(element)
            columns.append(Column(data))
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
        curve.label = "{0} vs {1}".format(curve.y.label, curve.x.label)

        return curve

    @property
    def x(self):
        return self.dictionary.get('x0')

    @property
    def y(self):
        return self.dictionary.get('y0')


class XYGraph:
    def __init__(self, datafile=None):
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
        self.axes.set(xlabel="X [arb. u]", ylabel="Y [arb. u]", title="")

        self.curves = []
        if datafile is not None:
            self.addCurves(datafile.curves)

    def add(self, x, y, dx=None, dy=None):
        self.curves.append(Curve(x, y, dx, dy))

    def addCurve(self, curve):
        self.curves.append(curve)

    def addCurves(self, curves):
        for curve in curves:
            self.curves.append(curve)

    @property
    def xlabel(self):
        return self.axes.get_xlabel()

    @xlabel.setter
    def xlabel(self, label):
        self.axes.set_xlabel(label)

    @property
    def ylabel(self):
        return self.axes.get_ylabel()

    @ylabel.setter
    def ylabel(self, label):
        self.axes.set_ylabel(label)

    def createFigure(self):
        symbols = [{"marker": 'o', 'color': 'k'},
                   {"marker": 'o', 'color': 'k', "markerfacecolor": 'none'},
                   {"marker": 's', 'color': 'k'},
                   {"marker": 's', 'color': 'k', "markerfacecolor": 'none'}]
        for i, curve in enumerate(self.curves):
            if not curve.isVisible:
                continue

            if not curve.hasXErrorBars and not curve.hasYErrorBars:
                if curve.connectPoints:
                    self.axes.plot(curve.x, curve.y,
                                   color='k',
                                   linestyle='-',
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

        if len(self.curves) >= 2:
            self.axes.legend()

    def show(self):
        self.createFigure()
        plt.show()

    def save(self, filepath):
        self.createFigure()
        self.fig.savefig(filepath, dpi=600)


if __name__ == "__main__":
    data = DataFile('data.csv', identification="x0 y0 y1 dx0 dy0")
    curve0, curve1 = data.curves
    # curve0.hide()
    # curve1.hide()
    graph = XYGraph(data)

    graph.addCurve(Fit(data.curves[1], degree=2))
    graph.ylabel = "Intensity"
    graph.xlabel = "Current"
    graph.show()
    graph.save("figure.pdf")
    data.curves[0].label = "Some parabola"
    data.curves[1].label = "Some data with errors"
    graph.show()
    graph.save("figure.pdf")
