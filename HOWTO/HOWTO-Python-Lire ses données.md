# Comment lire ses données en Python?

Ce document indique comment lire des données à partir du disque pour les analyser dans Python.

## Formats

Il existe plusieurs formats pour sauvegarder les données.  Un format fréquent est le format `CSV`, pour *Comma-Separated-Variables*: des lignes de données, avec chaque colonne séparée de sa voisine par une virgule. Malgré leurs noms, les fichiers `CSV` ne sont pas toujours en fait des nombres séparés par des virgules: on peut voir des tabulations, des espaces, ou des point-virgules.  De plus, les fins de lignes peuvent être de types "Windows" (CR-LF) ou Unix et macOS (LF).

### Module CSV

Le module `csv` peut lire les fichiers rapidement:

```python
import csv

with open('data.csv', newline='') as csvfile:
     fileReader = csv.reader(csvfile, delimiter=',')
     for row in fileReader:
        # row est une list des elements
        print('\t'.join(row)) # On les écrit, separés par \t

```

Un petit module simple est disponible [ici](../SRC/experiment.py) pour rapidement lire les fichiers `csv` et accéder aux colonnes:

```python
import experiment # Copiez le fichier experiment.py dans votre repertoire

file = experiment.DataFile('data.csv')
print(file.columns[0]) #Premiere colonne
print(file.columns[1]) #Deuxieme colonne...



```

