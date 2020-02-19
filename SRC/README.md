# Enseignement-SRC
Ce repertoire GitHub contient différents **scripts** reliés à l'enseignement du génie physique et de la physique. 

* [experiment.py](experiment.py): un petit script Python pouvant être importé pour rapidement lire des fichiers `csv` en Python grâce à une classe `DataFile` et `Graph`. S'utilise simplement comme suit:
  
  ```python
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
  ```
  
* [plotNice.m](plotNice.m): un petit script pour faire un graphique raisonnablement bien constitué dans MATLAB.

* [plotTableFromMarkdown.py](plotTableFromMarkdown.py): un script Python pour extraire un tableau d'un fichier Markdown pour ensuite faire un graphique dans matplotlib en python. Très limité: ne prend que le premier tableau et ne prend que les tableaux à 2 colonnes. S'utilise comme suit:

  ```bash
  python plotTableFromMarkdown.py fichier.md
  ```
  ou
  ```bash
  python plotTableFromMarkdown.py < fichier.md 
  ```





Daniel Côté

dccote@cervo.ulaval.ca

