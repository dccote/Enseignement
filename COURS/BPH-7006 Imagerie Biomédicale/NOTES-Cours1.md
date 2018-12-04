[TOC]

# BPH-7006 Imagerie

## Notes

Pour tout information manquante, se référer aux notes ([iBook](https://itunes.apple.com/ca/book/optique/id949326768?mt=11) ou [PDF](https://www.dropbox.com/s/ms9onzkg4y4771n/Optique-1.1.9.pdf?dl=0)) de Daniel Côté.

![225x225bb](assets/225x225bb.jpg)

## Résumé du premier cours

Les diapositives sont disponibles [ici](https://www.icloud.com/keynote/0HW4-8BHOf1WDqqQbkVMHjn9Q#BPH-7006_Imagerie).

### Optique ondulatoire

1. L'optique ondulatoire considère la longueur d'onde de la lumière $\lambda \ne 0$.

2. Un front d'onde représente les points de phase constante. (par exemple, un maximum).

3. Un front d'onde peut avoir une profile de champ électrique d'amplitude variable.

4. Les ondes sphériques et planes sont des bases complètes et peuvent décrire tous les faisceaux.

5. Le vecteur de Poynting instantané est $\vec{S}= \frac{1}{\mu} \vec{E} \times \vec{B} $ [W/cm^2^]

6. Le vecteur de Poynting moyen d'une onde sinusoïdale est $\vec{S}= \frac{c \epsilon_\circ}{2} \left| \vec{E}_\circ \right|^2 $ où $\left| \vec{E}_\circ \right|$ est l'amplitude de l'onde sinusoidale.

7. Des chifffres à retenir: 

   1. Un photon de à $\lambda = 1 \mu m$ a une énergie de 1eV
   2. 1 photon par seconde dans le visible donne environ 10^-19^ W
   3. 100 pW donne 1 photon par 100 ns dans le visible.
   4. Une PMT ne peut mesurer des photons plus rapproché que 100 ns.

8. L'indice de réfraction provient de la réaction du matériel avec ses dipôles qui s'opposent au champ électrique de l'onde

9. L'équation de Sellmeir donne l'indice de réfraction avec précision dans les zones de transparence

10. Le site http://refractiveindex.info regorge d'information. C'est obscène tellement il y en a beaucoup.

### Optique géométrique

1. L'optique géométrique est la manipulation des faisceaux dans des conditions où les distances sont beaucoup plus grandes que la longueur d'onde (essentiellement $\lambda \rightarrow 0$)
  1. On détermine la position des objets, des images, des diaphragmes
  2. Il n'y a pas d'interférence
  3. Il n'y a pas de diffraction
2. Une lentille a une seul distance focale (dans l'air) et deux points focaux (avant et arrière).
3. Les plans principaux et les plans nodaux sont superposées si la lentille est dans l'air
4. On mesure les distances focales à partir des plans principaux
   1. Une lentille mince a ses plans principaux au centre avec les plans nodaux
5. Les plans principaux sont de grossissement transverse de $M_T= 1$
6. Les plans nodaux sont de grossissement angulaire $M_A= 1$
7. Le produit est toujours $M_T \times M_A \equiv 1$.
8. On peut utiliser Zemax (dispendieux) Oslo (gratuit) ou Code V pour faire des calculs avec aberrations
9. On peut utiliser une librairie MATLAB du groupe dcclab à https://github.com/DCC-Lab/dcclab-matlab-toolbox
10. Ouverture numérique NA d'une lentille
   1. $NA = n \sin u$ où $u$ est l'angle maximal de sortie ou d'entrée
   2. Résolution d'une lentille (ou grosseur du point focal) $\Delta x = \frac{\lambda}{2 NA}$
11. f-number ou $f_\#$ d'une lentille
   1. $f_\# = f / D$ où $D$ est le diamètre extérieur du faisceau, au maxium le diamètre de la lentille
   2. Grosseur du point focal (ou résolution d'une lentille) $\Delta x = f_\# \lambda$
12. $f_\# = \frac{1}{2 NA} $
13. Bonne qualité de lentille : Grand $NA$ ou petit $f_\#$

### Systèmes

1. Les plans objets et images sont des plans conjuguées
2. Le plan objet et son plan de Fourier sont "des plans de Fourier l'un de l'autre". On ne dit pas "conjugués" car il n'y a pas d'image de l'objet.
3. **Système 2f**: Un objet à $f$ d'une lentille donne la transformé de Fourier à l'autre plan focal $f$.
4. **Système 4f**: Deux système 2f consécutifs avec un objet à $f_1$ de la première lentille donne une image à $f_2$ de la deuxième lentille avec un grossissement transverse  $M_T = -f_2/f_1$.
5. Le diaphragme d'entrée (*aperture stop*) limite le cône angulaire de lumière à l'entrée
6. Le diaphragme de champ (*field stop*) limite la grandeur du champ de vue (*field of view*).

