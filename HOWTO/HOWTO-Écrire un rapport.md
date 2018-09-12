# Écrire un rapport de laboratoire

## Commentaires généraux

Pour les utilisateurs de LaTeX, vous devriez utiliser [http://sharelatex.com](http://sharelatex.com/) ou [http://overleaf.com](http://overleaf.com/), qui permettent d'éditer un document simultanement avec votre co-équipier (comme Google Docs, mais pour LaTeX). Ma préférence récente est Overleaf.

Voici des commentaires generaux pour tous:

1. Les lettres dans les équations sont des variables et l’espacement entre celles-ci varie.

   1. LaTeX: Si vous voulez écrire un mot, vous devez utiliser: ```$100{\rm mW}$```, et non pas: ```$100 mW$```
   2. Word Equation : Si vous voulez écrire un mot, vous devez utiliser: 100 {Format:Text mW}, et non pas: 100 mW. De plus les espaces sont impossible en mode Math, vous devez changer le format a Text.

2. De la même façon dans LaTeX, on écrit  ```$\sin \theta$``` car sinus est reconnu comme une fonction, pas ```$sin \theta$```. Word les reconnait souvent, mais sinon, on doit convertir en Text.

3. LaTeX: Pour avoir des parenthèse de la bonne grosseur, faites ```\left(``` et ```\right)``` ou ```\left[``` et ```\right]``` etc… comme dans ```$\left( \frac{a}{b} \right)$``` au lieu de ```$( \frac{a}{b} )$```. Dans Word, choisissez le bon "groupe" de parenthèses dans les icônes.

4. LaTeX: Un espace inseparable se fait ```~``` comme dans ```100~mW``` et non pas ```100 mW``` pour éviter que les mots se séparent sur deux lignes. Word: Je crois que c'est control-espace ou option-espace. (unbreakable space ou espace indissociable).

5. Normalement, on gère les équations comme si elles faisaient partie du texte.  On met donc la ponctuation en conséquence et les majuscules:

   Avec l’équation:
   y = mx + b,
   on obtient la pente ….

   Notez la virgule après l’équation, et la minuscule à “on"

6. On n'écrit pas les nombres comme 10E-3 dans un texte.  On utilise un exposant et on écrit 10^-3^.

## Contenu d'un rapport

Le rapport de laboratoire est une **synthèse** de l'expérience. *Un rapport doit être facile à lire par section*.  Ce n'est pas une narration des tâches effectuées. Ce n'est pas non plus un document avec une longue section théorique qui tente de démontrer que vous comprenez la théorie derrière les mesures: cette compréhension sera pparente lorsque vous discuterez des limites de vos appareils et vos résultats. Le rapport de laboratoire doit offrir au lecteur un résumé de l'expérience, des méthodes utilisées et des résultats obtenus, montrer les données expérimentales sous une forme attrayante, analyser en profondeur les résultats en offrant une discussion de ces mêmes résultats en plus des limites de l'expérience. Une conclusion permet de répéter les points saillants du rapport.

Le rapport de **10 pages** de texte (page titre et annexes en sus) doit donc être structuré de la façon suivante :

1. **Page titre**.  

   Cette première page doit comprendre : le nom (Travaux pratiques d’optique-photonique II) et le sigle (GPH-2004) du cours, le trimestre en cours (H-2014), le titre de l’expérience, le nom et l’adresse électronique de l’auteur, le nom du co-équipier lors de la séance de laboratoire, la date de l’expérience et la date de remise du rapport ainsi qu’un résumé

2. **Résumé**: Le résumé donne les résultats des expériences et les différentes limitations rencontrées ("Nous avons mesuré un intervalle spectral libre de X GHz." ou encore "L'utilisation d'une lame quart d'onde avec une source de lumière blanche ne permet pas de bien contrôler la polarisation, ce qui amène une ellipticité de 5% pour l'ensemble des longueurs d'ondes." par exemple). *On doit pouvoir lire le résumé et savoir les conclusions*.

3. **Introduction.**  L’introduction est un paragraphe de 10 à 15 lignes au maximum.  Elle sert à préciser le but de l’expérience, à délimiter le sujet de l’étude expérimentale et à la situer dans un contexte plus général.

4. **Théorie (minimale):** La section théorique sert à introduire de**façon concise**les concepts de base, les équations et les symboles utilisés. Si vous n'utilisez pas une équation, il n'y a pas de raison qu'elle soit dans cette section.  Ne répétez pas le protocole, vous pouvez faire référence au protocole. Toute figure doit être donnée avec référence.

5. Pour chacune des étapes de l’expérience, vous devez décrire brièvement : la méthode de mesure, les résultats obtenus (et l’interprétation physique de ces résultats) et quelques éléments de discussion.  Les résultats peuvent être présentés sous forme de tableau(x) ou de graphique(s). Il est plus habituel de présenter l'ensemble des méthodes d'abord, suivi de l'ensemble des résultats et de terminer par la discussion plutôt que de présenter la méthode, le résultat et une discussion pour chaque mesure. Ainsi, on s'attend à trois grandes sections:

   1. **Méthodes expérimentales:** Vous décrivez rapidement les méthodes, le vocabulaire et tout autre concepts nécessaire à la compréhension des résultats et de leur interprétation. Vous présentez un schéma simplifié du montage expérimental utilisé pour réaliser l’expérience (dans certains cas, quelques schémas peuvent être nécessaires) avec une description **concise** du matériel utilisé. Toute figure doit être donnée avec référence.  Vous devez répondre à la question **"COMMENT?"**. Par exemple, dans Fabry Perot, la position du miroir du Fabry Perot est balayé avec contrôle haute tension de trois éléments piézo-électriques.  La rampe de tension périodique determine le déplacement et la vitesse de ce déplacement.
   2. **Résultats:** Vous présentez les résultats de façon *synthétique.*  Ainsi, vous ne montrez pas les résultats bruts, mais bien les résultats traités. Cette section répond à la question **"QUOI?"**. Par exemple, dans Michelson, vous devriez enlever les données des extrémas pour éviter les erreurs de déplacement de la vis et vous devez montrez vos axes calibrés.
   3. **Discussion**: Cette section représente le coeur de votre rapport.  Vous y exposez l'explication des résultats, mais surtout leurs limites, les imperfections, les améliorations qu'on pourrait faire pour obtenir de meilleures mesures et tout autre commentaire pertinent. Par exemple, pour polarisation, vous discuteriez de l'imperfection de la polarisation circulaire, pour Michelson vous discuteriez de la résolution spectrale.

6. **Conclusion.**  C’est un résumé des grandes lignes du travail expérimental accompli (phases essentielles et points critiques) et un exposé commenté des **principales réalisations, observations et résultats obtenus**.

7. **Annexes (s’il y a lieu).**  Une annexe contient des renseignements complémentaires non essentiels à la compréhension du rapport.  Par exemple, il peut s’agir d’un calcul très détaillé d'incertitude (trop long pour être inclus dans le texte).

**Graphiques**

Les graphiques doivent être lisibles. Le but d'un graphique est de donner plus d'information que ce qui serait donné autrement (par du texte, un tableau, etc.). Donc, à retenir:

1. Des axes bien identifiés avec des lettres assez grandes, pas trop petites.

2. Des symboles de points, lorsque nécessaire, assez différents pour chaque courbe: rond plein, rond vide, c'est beaucoup mieux que rond plein losange plein.

3. Lorsque possible, il est préférable d'utiliser une solution noir et blanc avec des courbes pleine, pointillée, etc...: on ne sait pas comment le lecteur l'imprimera.  Cependant, parfois, c'est impossible et on utilise les couleurs.

4. Lorsque vous exportez vos graphiques, assurez-vous d'avoir une résolution très élevée (600 dpi) si vous utilisez un format pixelisé comme PNG, TIFF, etc...  Vous devriez préférer PDF lorsque possible si votre traitement de texte le supporte. Sinon, voici comment obtenir une bonne résolution en Python ou MATLAB:

   1. Dans Python: ajoutez dpi=600 pour les format pixelisés

      ```python
      import matplotlib.pyplot as plt
      f = plt.figure()
      plt.plot(range(10), range(10), "o")
      #plt.show() #montrer ou non 
      f.savefig("graph.pdf", bbox_inches='tight')
      f.savefig("graph.png", bbox_inches='tight',dpi=600)
      
      ```

   2. Dans MATLAB 2018, dans Figure Properties/Export Setup/Rendering choisissez 600 dpi au lieu de auto et ensuite cliquez le bouton Export.

      Vous pouvez aussi le faire dans un script avec :

      ```matlab
      print(FigureNumber, '-dpng', 'graph.png', '-r600')*
      ```

      L'information est ici:

      <https://www.mathworks.com/matlabcentral/answers/109642-write-compared-images-not-figures>

Pour référence, voici des exemples de bons et mauvais graphiques: 

![Exemple_graphiques](Exemple_graphiques.png)

Voici un bon tableau.  Notez qu'on ne met pas de lignes verticales dans un tableau, et ce, même si Microsoft Word continue de vous le faire par défaut.

![Exemple_tableau](Exemple_tableau.png)