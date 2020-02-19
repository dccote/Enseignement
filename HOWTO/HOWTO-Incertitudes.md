# HOWTO- Incertitudes, Exactitude et test d'hypothèses

## Règles *rapides* au laboratoire

1. Nous supposons toujours que les erreurs sont normalement distribuées: les distributions sont donc normales, gaussiennes.
2. Les incertitudes sur les sommes et soustractions peuvent rapidement être obtenue en additionnant les erreurs absolues de chacune: $(a\pm\Delta a) + (b \pm \Delta b) = a+b \pm (\Delta a + \Delta b)$. Deux nombres à ±1 donnent une somme ou une différence à ±2. *Cette règle surestime l'incertitude mais est rapide à calculer.*
3. Les incertitudes sur les produits et quotients peuvent rapidement etre obtenue en additionnant les erreurs relatives de chacune: $(a \pm \Delta a) \times (b \pm \Delta b) = ab \pm (\Delta a / a + \Delta b/b) \%$.  Deux nombres connus à ±2% donne un produit ou un quotient à ±4%.
4. On prend souvent "la moitié de la plus petite division" d'un appareil parce que c'est raisonnable, rapide et cela représente souvent "le pire cas".
5. On peut prendre un grand nombre de mesures pour obtenir la distribution de facon plus précise
6. Si une mesure avec une précision de $\Delta$ est répétée $N$ fois,  la précision sur la moyenne s'améliore à $\Delta/\sqrt{N}$.

## Règles générales *rigoureuses*

1. De façon générale, lorsque la dépendence d'une mesure sur d'autres variables est plus complexe, on fait un calcul d'erreur complet avec les différentielles partielles par rapport à chaque variable: $\Delta = \sqrt{\sum_i \left( \frac{\partial f}{\partial x_i} \Delta x_i\right)^2 }$
2. Les incertitudes des mesures ne sont pas toujours pertinentes dans une expérience
3. On peut modifier *a posteriori* une incertitude suite à une analyse plus poussée.

## Signification de a ± ∆a

Lorsqu'une mesure de $a ± \Delta a$ est donnée, on veut dire qu'un grand nombre de mesures *dans les mêmes conditions* donnera une distribution gausienne centrée sur $\mu = a$ et de largeur $\sigma = \Delta a$. Une mesure de 100 ± 1 est illustrée ci-contre:

![image-20180918210554856](assets/image-20180918210554856.png)



## Exemple: Règle à mesurer

Une règle à mesurer à une division de 1 mm est utilisée pour mesurer la hauteur d'un livre rectangulaire (N=25 mesures) à différents endroits. La distribution est obtenue ci-dessous.  

[18.95, 19.00, 18.95, 18.98, 18.98, 18.98, 19.00, 18.93, 18.98, 18.99, 18.98, 18.95, 18.98, 18.95, 18.98, 18.95, 18.95, 18.96 ,18.99, 18.94, 18.96, 18.98, 18.95, 18.99, 18.95]

Moyenne: 18.698, Écart-type: 0.019 

![image-20180918211716443](assets/image-20180918211716443.png)


Nous concluons:

1. La moitié de la plus petite division de la règle est 0.05 cm. On peut la prendre comme approximation rapide de la précision de la mesure.
2. La distribution des mesures, qui englobe l'ensemble du processus de mesures (le livre, la position où la mesure a été prise, l'angle, la règle, l'effet de parallaxe, etc...), possède une largeur de 0.02 cm.  On peut la prendre comme une meilleure valeur de la précision de la mesure obtenue par statistiques (mais c'est plus long: on a pris 25 mesures).
3. Immédiatement après la première mesure, on dirait que la hauteur du livre est 18.95 ± 0.05 cm. C'est la seule mesure que l'on a. L'incertitude la plus raisonnable est la moitié de la plus petite division.
4. Après 25 mesures, les mesures sont distribuées normalement autour d'une moyenne de 18.97 cm avec une largeur de distribution de 0.02 cm.
5. La connaissance de la moyenne est maintenant 18.968 ± 0.004 cm car l'erreur sur la moyenne après $N$ mesures est $\sigma/\sqrt{N}$. 
   1. Cette moyenne est pertinente si les mesures sont faites dans des conditions identiques et que la hauteur du livre est vraiment la même dans toutes ces conditions. Ceci peut être discutable.
   2. Dans notre cas, la connaissance de la hauteur moyenne pourrait être pertinente pour calculer l'aire de la couverture (en supposant un rectangle) si on s'intéressait vraiment à la surface de façon précise.
   3. Peut-être que de simplement dire que la hauteur du livre est 19 cm est suffisant si on ne s'intéresse pas aux détails précis.





