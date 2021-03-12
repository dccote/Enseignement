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

class DataFile:
    def __init__(self, filepath):
        self.filepath = filepath
        self.rows = []

        with open(self.filepath) as csvfile:
            dialect = csv.Sniffer().sniff(csvfile.read(1024))
            csvfile.seek(0)
            fileReader = csv.reader(csvfile, dialect,
                quoting=csv.QUOTE_NONNUMERIC)

            for row in fileReader:
                self.rows.append(row)

        if len(self.rows[0]) == 2:
            self.assignments = ['x0','y0']
        else:
            self.assignments = [None]*len(self.rows[0])

    @property
    def x(self):
        index = self.columnIndex('x0')
        if index is not None:
            return self.columns[index]
        return self.columns[0]

    @property
    def y(self):
        index = self.columnIndex('y0')
        if index is not None:
            return self.columns[index]
        return self.columns[1]

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

    def columnIndex(self, pattern):
        for i, a in enumerate(self.assignments):
            result = re.match(pattern, a)
            if result is not None:
                return i
        return None

    # @property
    # def curves(self):
    #     curves = []
    #     if len(self.xVectors) == 1:


class DataCurve:
    def __init__(self, x=None, y=None, dx=None, dy=None):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy


class XYGraph:
    def __init__(self, x=None, y=None, dx=None, dy=None):

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

        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.linewidth = 2
        self.markersize= 7
        (self.fig, self.axes) = plt.subplots(figsize=(6, 5))
        self.axes.set(xlabel="X [arb. u]", ylabel="Y [arb. u]", title="")
        if dx is None and dy is None:
            self.axes.plot(x, y, 'ko', markersize=self.markersize)
        elif dy is not None:
            self.axes.errorbar(x, y, 'ko', markersize=self.markersize)

    def addCurve(self, x=None, y=None, dx=None, dy=None):
        return

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
        plt.ioff()
        plt.show()

    def save(self, filepath):
        self.fig.savefig(filepath, dpi=600)

# class Histogram:

if __name__ == "__main__":
    data = DataFile('data.csv')
    data.assign(column=0, role='x0')
    data.assign(column=1, role='y0')
    print(data.columns[0]) #Premiere colonne
    print(data.columns[1]) #Deuxieme colonne...
    print(data.x) #Synonyme de columns[0]
    print(data.y) #Synonyme de columns[1]

    g = XYGraph(data.x, data.y)
    g.ylabel = "Intensity"
    g.xlabel = "Current"
    g.show()
    g.save("figure.pdf")