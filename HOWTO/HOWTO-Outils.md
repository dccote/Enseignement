# Enseignement

[TOC]

## Logiciels

Différents documents, scripts, figures ou autres reliés à l'enseignement.

1. Graphiques
   1. Le logiciel MATLAB (Windows+Mac) peut être utilisé pour faire des graphiques. Des ordinateurs au laboratoire ont le logiciel MATLAB.  Une licence étudiante est aussi disponible à la Faculté.
   2. Le langage de programmation Python permet de faire des graphiques grâce au package matplotlib.
   3. Le logiciel Gnuplot est gratuit et permet de faire des graphiques acceptables.
   4. Le logiciel Excel permet de faire des graphiques en pointe de tarte (délicieux).
2. Analyse d'images
   1. Plusieurs montages utilsent le logiciel d'analyse d'images **ImageJ ou Fiji**. Pour le télécharger (gratuitement), consultez le site [Fiji](http://fiji.sc/Fiji)
   2. Le logiciel MATLAB peut être utilisé pour faire les analyses. Des ordinateurs au laboratoire ont le logiciel MATLAB.  Une licence étudiante est aussi disponible a la Faculté.

## MATLAB

### Obtenir MATLAB

- Utilisez les ordinateurs de laboratoire ou obtenez une licence facultaire - etudiant.

### Entrer des données

- À la main (aide MATLAB: Les matrices):
  - ```matlab
     x = [ 0 1 2 3 4 5 6 ]	
     y = [ 0 3.5 4 6.2 4.4 4.5 8.0];
     ```

- Du disque (aide MATLAB: Importer des fichiers texte ):
  - ```matlab
    donnees = dlmread('file.dat');
    x=donnees(:,1)
    y=donnees(:,2)
    ```

    Vous pouvez utiliser ```load('data.txt')```, mais les données seront dans la variable ```data```.

### Faire un graphique

- Vous pouvez utiliser la commande plot, mais vous pouvez aussi utiliser le fichier de commande ci-dessous, appelé [plotNice.m](../SRC/plotNice.m) pour faire un graphique de bonne qualité.
  - ```matlab
    matlab
    plot(x,y);
    plotNice("Titre", "Axe des X", "Axe des Y", x,y);
    ```
  - ```matlab
    function plotNice( theTitle, theXLabel, theYLabel, varargin )
    % plotNice Plot data with decent default values.  Similar to 'plot'.
    %         Use : plotNice( theTitle, theXLabel, theYLabel, X,Y,... )
    
    m = {'-o','-.','*','.','x','s','d','^','v','>','<','p','h'};
    set_marker_order = @() set(gca(), ...
    'LineStyleOrder',m, 'ColorOrder',[0 0 0], ...
    'NextPlot','replacechildren');
    set_marker_order();
    h=plot(varargin{:});
    h.Marker = 'o';
    h.LineWidth = 2;
    h.MarkerSize = 20;  
    
    title(theTitle);
    xlabel(theXLabel);
    ylabel(theYLabel);
    
    set(gca,'FontSize',20);
    set(gcf,'color',[1 1 1]);
    
    end
    ```
### Faire une régression ("un fit")

- Vous pouvez utiliser la commande fit avec le type de régression (aide MATLAB, tous les modèles):

  - ```matlab
    f=fit(x,y,'poly2')
    plot(f,x,y);
    ```

## Python

### Obtenir

- Dans bien des cas, vous voudrez avoir l'ensemble des modules scientifiques.  L'installation de

  Anaconda est recommandée: tout s'installe en bloc. Sinon:

  - Utilisez les ordinateurs de laboratoire.
  - OS X et Linux: Ouvrez un terminal.  Python vient avec le systeme.
  - Windows: Téléchargez et installez Python sur votre machine: <https://www.python.org/downloads/>

### Entrer des données

- À la main:
  - ```python
    x = [ 0, 1, 2, 3, 4, 5, 6 ];
    y = [ 0, 3.5, 4, 6.2, 4.4, 4.5, 8.0];
    ```
- Du disque:
  - ```python
    import numpy as np
    import matplotlib
    import matplotlib.pyplot as plt
    donnees = np.loadtxt('data.txt')
    x=donnees[:,0]
    y=donnees[:,1]
    ```
### Faire un graphique

- Vous pouvez utiliser la commande plot de matplotlib:

  - ```matlab
    import numpy as np
    import matplotlib
    import matplotlib.pyplot as plt
    
    x = [ 0, 1, 2, 3, 4, 5, 6 ];
    y = [ 0, 3.5, 4, 6.2, 4.4, 4.5, 8.0];
    
    donnees = np.loadtxt('data.txt')
    x=donnees[:,0]
    y=donnees[:,1]
    
    plt.plot(x, y)
    
    plt.show()
    ```

## Gnuplot

### Obtenir gnuplot

- Utilisez les ordinateurs de laboratoire.
- Windows: Téléchargez [l'application fonctionnelle](http://sourceforge.net/projects/gnuplot/files/gnuplot/5.0.1/) sur sourceforget.net
- OS X/Linux: Téléchargez le code source sur http://sourceforge.net/projects/gnuplot/files/gnuplot/5.0.1/ et compilez vous même l'application avec: ./configure; make install dans le repertoire du code.
- OS X: Utilisez macport et tapez : sudo port install gnuplot

### Entrer des données

- À la main

  - gnuplot ne travaille pas facilement avec des données hors d'un fichier.  Entrez les données dans un fichier et nommez-le 'data.txt' par exemple.  Séparez les colonnes par une tabulation. [Aide format Gnuplot](http://lowrank.net/gnuplot/datafile-e.html)
- D'un fichier
  - ```gnuplot
    set xlabel 'exposition (mR)'
    set ylabel 'niveau de gris (UA)'
    plot 'data.txt' using 1:2 title "valeur mesuree" lw 3 pt 5 ps 3
    ```

### Faire un graphique

- ```
  set xlabel 'Axe des X'
  set ylabel 'Axe des Y'
  plot 'data.txt' using 1:2 title "Valeur mesurée" lw 3 pt 5 ps 3
  ```



