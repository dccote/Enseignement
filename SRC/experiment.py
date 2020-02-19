import csv

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


