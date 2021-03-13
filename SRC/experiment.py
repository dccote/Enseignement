import csv
import matplotlib.pyplot as plt
import re
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

class Relation:
    def __init__(self, x=None, y=None, dx=None, dy=None):
        self.label = "Data"
        self.isFunction = False
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy

    @property
    def hasXErrorBars(self):
        return self.dx is not None

    @property
    def hasYErrorBars(self):
        return self.dy is not None
    
    def __repr__(self):
        return "{0}±{1} {2}±{3}".format(self.x, self.dx, self.y, self.dy)

class Fit(Relation):
    def __init__(self, relation, degree):
        N = 100
        xs = numpy.linspace(min(relation.x), max(relation.x), N)
        polynomial = Polynomial.fit(relation.x, relation.y, deg=degree)
        ys = polynomial(xs)
        Relation.__init__(self, x=xs, y=ys)

        self.isFunction = True
        self.label = "Polynomial fit"
        self.degree = degree
        self.N = N

class DataFile:
    def __init__(self, filepath, relationships=None):
        self.filepath = filepath
        self.rows = []
        self.iteration = 0
        self.relationships = []
        self.readFile(filepath)

        if relationships is not None:
            self.assign(relationships)
        elif len(self.rows[0]) == 2:
            self.relationships = ['x0','y0']

    def readFile(self, filepath):
        with open(filepath) as csvfile:
            dialect = csv.Sniffer().sniff(csvfile.read(1024))
            csvfile.seek(0)
            fileReader = csv.reader(csvfile, dialect,
                quoting=csv.QUOTE_NONNUMERIC)

            for row in fileReader:
                self.rows.append(row)

        self.relationships = [None]*len(self.rows[0])

    def __iter__(self):
        return self

    def __next__(self):
        try:
            c = self.relations[self.iteration]
            self.iteration += 1
            return c
        except:
            raise StopIteration()

    def assign(self, relationships):
        for i, role in enumerate(relationships.split()):
            self.relationships[i] = role

    # Column manipulation
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

    def column(self, pattern=None, index=None):
        for i, a in enumerate(self.relationships):
            if a is not None:
                if re.match(pattern, a) is not None:
                    return self.columns[i]
        return None

    def relation(self, index):
        relation = Relation()

        relation.y = self.column(pattern="y{0}".format(index))
        if relation.y is None:
            return None

        relation.x = self.column(pattern="x{0}".format(index))
        if relation.x is None:
            relation.x = self.column(pattern="x0")

        relation.dx = self.column(pattern="dx{0}".format(index))
        relation.dy = self.column(pattern="dy{0}".format(index))
        return relation

    @property
    def relations(self):
        relations = []
        for c in range(10) :
            relation = self.relation(index=c)
            if relation is not None:
                relations.append(relation)
        return relations

class XYGraph:
    def __init__(self, datafile):
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
        self.linewidth = 1 # Set to 1 or 2 to connect the dots
        self.markersize= 7
        (self.fig, self.axes) = plt.subplots(figsize=(6, 5))
        self.axes.set(xlabel="X [arb. u]", ylabel="Y [arb. u]", title="")

        self.addCurves(datafile.relations)

    def add(self, x, y, dx=None, dy=None):
        self.curves.append(Relation(x,y,dx,dy))

    def addCurve(self, relation):
        self.curves.append(relation)

    def addCurves(self, relations):
        for relation in relations:
            self.curves.append(relation)

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
        symbols = [{"marker":'o','color':'k'},
                   {"marker":'o','color':'k',"markerfacecolor":'none'},
                   {"marker":'s','color':'k'},
                   {"marker":'s','color':'k',"markerfacecolor":'none'}]
        for i, curve in enumerate(self.curves):
            if not curve.hasXErrorBars and not curve.hasYErrorBars:
                if curve.isFunction:
                    self.axes.plot(curve.x, curve.y,
                                   color='k', 
                                   linestyle='-', 
                                   linewidth=self.linewidth,
                                   label=curve.label)
                else:
                    self.axes.plot(curve.x, curve.y, **symbols[i],
                                   markersize=self.markersize, 
                                   linestyle='-', 
                                   linewidth=0,
                                   label=curve.label)

            elif curve.hasYErrorBars:
                self.axes.errorbar(curve.x, curve.y, **(symbols[i]),
                               markersize=self.markersize,
                               linestyle='-',
                               linewidth=self.linewidth,
                               label=curve.label)

        if len(self.curves) >= 2:
            self.axes.legend()

        plt.show()

    def save(self, filepath):
        self.fig.savefig(filepath, dpi=600)

if __name__ == "__main__":
    data = DataFile('data.csv', relationships="x0 y0 y1")
    graph = XYGraph(data)
    graph.addCurve( Fit(data.relations[1], degree=2))
    graph.ylabel = "Intensity"
    graph.xlabel = "Current"
    graph.show()
    graph.save("figure.pdf")
