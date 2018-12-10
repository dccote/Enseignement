[TOC]

# BPH-7006 Imagerie

## Notes

Pour tout information manquante, se référer aux notes ([iBook](https://itunes.apple.com/ca/book/optique/id949326768?mt=11) ou [PDF](https://www.dropbox.com/s/ms9onzkg4y4771n/Optique-1.1.9.pdf?dl=0)) de Daniel Côté.

![225x225bb](assets/225x225bb.jpg)

## Résumé du deuxième cours

Les diapositives sont disponibles [ici](./DIAPOS-Cours2-Système.url).

## Système à grand champ

1. Un système grand champ illumine une surface et image cette surface sur une caméra ou sur l'oeil.

2. On l'appelle un système imageant.

3. Typiquement, les systèmes grand champ n'ont pas de sectionnement optique (sauf HiLo)

4. Pour un système imageant, deux choses déterminent le champs de vue:

   1. La largeur du chamnp de vue de l'illumination sur l'échantillon
   2. La largeur du champ de vue de l'imagerie sur la caméra

5. On calcule le champs de vue à l'aide de l'optique géométrique en trouvant le diaphragme de champ. (Voir [PDF](https://www.dropbox.com/s/ms9onzkg4y4771n/Optique-1.1.9.pdf?dl=0)).

6. Si un objectif est conçu pour un système, le diaphragme d'entrée sera l'entrée arrière de l'objectif et correspond à l'ouverture numérique


## Système à balayage

1. Un système à balayage acquiert la lumière séquentiellement en balayant le faisceau sur l'échantillon et en envoyant la lumière sur un détecteur de type PMT ou APD (i.e. *point-detector*)

2. On l'appelle système à balayage

3. Les systèmes à balayage ont du sectionnement optique

   1. Soit par détection confocal, où un pinhole devant le détecteur est imagé sur l'échantillon et bloque la lumière hors du point focal
   2. Soit par excitation multiphotonique, où l'illumination excite l'échantillon seulement au point focal et cette fluorescence/émission est envoyée au détecteur en totalité

4. Le champ de vue d'un système à balayage est obtenu en regardant l'angle de balayage maximal $\theta_\text{max}$ du système de balayage à l'entrée arrière de l'objectif de focal $f_\text{obj}$.  On obtient: $f_\text{obj} \theta_\text{max}$.

5. Si un objectif est conçu pour un système, le diaphragme d'entrée sera l'entrée arrière de l'objectif et correspond à l'ouverture numérique

6. Pour chaque grossissement $M$ du faisceau par un système 4f, le balayage en angle est réduit du même facteur $1/M$.

7. Un système à balayage doit considerer:

   1. Les angles balayées
   2. La grosseur du faisceau à l'objectif 
