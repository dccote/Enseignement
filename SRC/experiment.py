import csv
import matplotlib.pyplot as plt
import re

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

class Data:
    def __init__(self, x=None, y=None, dx=None, dy=None):
        self.x: [float] = x
        self.y: [float] = y
        self.dx: [float] = dx
        self.dy: [float] = dy

    @property
    def hasXErrorBars(self):
        return self.dx is not None

    @property
    def hasYErrorBars(self):
        return self.dy is not None
    
    def __repr__(self):
        return "{0} {1} {2} {3}".format(self.x, self.dx, self.y, self.dy)

class DataFile:
    def __init__(self, filepath, roles=None):
        self.filepath = filepath
        self.rows = []

        with open(self.filepath) as csvfile:
            dialect = csv.Sniffer().sniff(csvfile.read(1024))
            csvfile.seek(0)
            fileReader = csv.reader(csvfile, dialect,
                quoting=csv.QUOTE_NONNUMERIC)

            for row in fileReader:
                self.rows.append(row)

        self.assignments = [None]*len(self.rows[0])
        if roles is not None:
            self.assignAll(roles)
        elif len(self.rows[0]) == 2:
            self.assignments = ['x0','y0']

    @property
    def x(self):
        return self.column('x0')

    @property
    def y(self):
        return self.column('y0')

    @property
    def columns(self):
        nColumns = len(self.rows[0])

        columns = []
        for index in range(nColumns):
            column = []
            for row in self.rows:
                element = row[index]
                column.append(element)
            columns.append(column)

        return columns

    def assign(self, column, role):
        possibilities = [r"x\d+",r"y\d+",r"dx\d+",r"dy\d+"]

        self.assignments[column] = role

    def assignAll(self, roles=None):
        for i, role in enumerate(roles.split()):
            self.assign(i, role)

    def column(self, pattern=None, index=None):
        for i, a in enumerate(self.assignments):
            if a is not None:
                if re.match(pattern, a) is not None:
                    return self.columns[i]
        return None

    def curve(self, index):
        data = Data()

        data.y = self.column(pattern="y{0}".format(index))
        if data.y is None:
            return None

        data.x = self.column(pattern="x{0}".format(index))
        if data.x is None:
            data.x = self.column(pattern="x0")

        data.dx = self.column(pattern="dx{0}".format(index))
        data.dy = self.column(pattern="dy{0}".format(index))
        return data

    @property
    def curves(self):
        curves = []
        for c in range(10) :
            curve = self.curve(index=c)
            if curve is not None:
                curves.append(curve)
        return curves

class XYGraph:
    def __init__(self):
        SMALL_SIZE = 11
        MEDIUM_SIZE = 13
        BIGGER_SIZE = 36

        plt.rc('font', size=SMALL_SIZE)          # controls default text sizes
        plt.rc('axes', titlesize=SMALL_SIZE)     # fontsize of the axes title
        plt.rc('axes', labelsize=MEDIUM_SIZE)    # fontsize of the x and y labels
        plt.rc('xtick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
        plt.rc('ytick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
        plt.rc('legend', fontsize=SMALL_SIZE)    # legend fontsize
        plt.rc('figure', titlesize=BIGGER_SIZE)  # fontsize of the figure title

        self.curves = []
        self.linewidth = 2
        self.markersize= 7
        (self.fig, self.axes) = plt.subplots(figsize=(6, 5))
        self.axes.set(xlabel="X [arb. u]", ylabel="Y [arb. u]", title="")

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
        
    def show(self):
        for curve in self.curves:
            if not curve.hasXErrorBars and not curve.hasYErrorBars:
                self.axes.plot(curve.x, curve.y, 'ko', markersize=self.markersize)
            elif curve.hasYErrorBars:
                self.axes.errorbar(curve.x, curve.y, 'ko', markersize=self.markersize)

        plt.show()

    def save(self, filepath):
        self.fig.savefig(filepath, dpi=600)

# class Histogram:

if __name__ == "__main__":
    data = DataFile('data.csv', "x0 y0 y1")
    # data.assign(column=0, role='x0')
    # data.assign(column=1, role='y0')
    # data.assign(column=2, role='y1')
    print(data.curves)
    # print(data.columns[0]) #Premiere colonne
    # print(data.columns[1]) #Deuxieme colonne...
    # print(data.x) #Synonyme de columns[0]
    # print(data.y) #Synonyme de columns[1]

    g = XYGraph()
    g.addCurves(data.curves)

    g.ylabel = "Intensity"
    g.xlabel = "Current"
    g.show()
    g.save("figure.pdf")