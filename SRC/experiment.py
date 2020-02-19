import csv
import matplotlib.pyplot as plt

""" Une classe DataFile pour lire les données de fichiers CSV. A utiliser
comme suit:

import experiment # Copiez le fichier experiment.py dans votre repertoire

file = experiment.DataFile('data.csv')
print(file.columns[0]) #Premiere colonne
print(file.columns[1]) #Deuxieme colonne...

"""

class DataFile:
    def __init__(self, filepath, delimiter=','):
        self.filepath = filepath
        self.rows = []

        with open(self.filepath) as csvfile:
            dialect = csv.Sniffer().sniff(csvfile.read(1024))
            csvfile.seek(0)
            fileReader = csv.reader(csvfile, dialect,
                quoting=csv.QUOTE_NONNUMERIC)

            for row in fileReader:
                self.rows.append(row)

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

class Graph:
    def __init__(self, x=None, y=None):

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

        self._title = ""
        self.x = x
        self.y = y
        self.linewidth = 2
        self.markersize= 7
        (self.fig, self.axes) = plt.subplots(figsize=(6, 5))
        self.axes.set(xlabel="X [arb. u]", ylabel="Y [arb. u]", title="")
        self.axes.plot(x, y, 'ko', markersize=self.markersize)

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


