# Les bases de l'électronique



Une version PDF de ce document [existe](https://github.com/dccote/Enseignement/blob/master/HOWTO/HOWTO-Electronique.pdf).

Une version Markdown peut être lu avec les équations avec le logiciel gratuit [Typora](http://typora.io).

[TOC]

## Prélude

On ne s'en sort pas: la connaissance de l'électronique est essentielle pour accomplir les moindre tâches en optique: photodétection, numérisation, contrôle d'appareils, interface microprocesseur, gestion USB, etc... Il y a deux façons d'aborder ce domaine: 1) en devenant opérationnel ou 2) en comprenant[^1]. S'il y avait un seul conseil que je donnerais: les circuits, aussi complexes soient-ils, se séparent toujours en petits blocs fonctionnels. Savoir reconnaître les blocs représente 90% de la bataille.  J'espère avec ce document faire le premier aspect (vous rendre opérationnel) et avec un peu de chance, le deuxième (vous aider à comprendre).

La meilleure façon d'apprendre l'électronique, c'est d'en faire, d'être mauvais, et de s'améliorer. Pour citer Dave Grohl, c'est comme la musique :

> “When I think about kids watching a TV show like American Idol or The Voice, then they think, ‘Oh, OK, that’s how you become a musician, you stand in line for eight [...] hours with 800 people at a convention center and… then you sing your heart out for someone and then they tell you it’s not [...] good enough.’ Can you imagine?” he implores. “It’s destroying the next generation of musicians! Musicians should go to a yard sale and buy and old [...] drum set and get in their garage and just suck. And get their friends to come in and they’ll suck, too. And then they’ll [...] start playing and they’ll have the best time they’ve ever had in their lives and then all of a sudden they’ll become Nirvana. Because that’s exactly what happened with Nirvana. Just a bunch of guys that had some shitty old instruments and they got together and started playing some noisy-ass shit, and they became the biggest band in the world. That can happen again! You don’t need a [...] computer or the internet or The Voice or American Idol.” - Dave Grohl

Expérimenter peut se faire pour apprendre de façon intelligente:

1. Briser un fil, brûler une résistance, écraser un condensateur, brancher un transistor à l'envers, péter un chip à 10$ fait partie de l'apprentissage. Ce n'est pas grave: c'est quelques dollars. Voir 2.
2. Brancher 100V dans un oscilloscope de 3000$ et le péter, mettre ses mains ou sa langue sur 1200V et finir à l'hôpital, brûler une puce à 200\$ qui a un temps de livraison de 8 semaines, faire sauter le microntrolleur d'un laser commercial, fait partie de la liste des choses qui font que les gens se font mettre dehors.  Apprenez la différence avec 1.

Bon apprentissage.

## Les bases

![](HOWTO-Electronique.assets/image-20210128131705277.png)

1. Une source de tension idéale donne une différence de potentiel constante entre ses bornes, quelle que soit la résistance connectée entre ses bornes.
2. Une source de courant idéale donne un courant constant quelle que soit la résistance connectée entre ses bornes.
3. Un voltmètre idéal a une résistance "infinie" et mesure la différence de potentiel entre ses bornes sans prendre de courant.
4. Un ampèremètre idéal a une résistance nulle et mesure le courant qui passe entre ses bornes sans perte de potentiel.

## Commentaires généraux

1. La perte de tension à travers une résistance est donnée par le courant qui passe à travers multiplié par la résistance $V = RI$
2. Le courant qui passe dans un circuit est donné par la tension aux bornes de ce circuit divisée par la résistance totale du circuit $I = {V}/{R_t}$
3. La puissance dissipée par un élément est $P = VI $
4. **On mesure des tensions, en Volts**. La raison pourquoi on travaille en tension plutôt qu'en courant est qu'une mesure en parallèle d'une tension n'affecte pas le système et est égale à la mesure qui nous intéresse. Si on mesurait des courants, on devrait faire un calcul pour obtenir le courant du système à partir de notre mesure (car les courants se séparent selon les résistances) et si on le mesurait en série on devrait s'inclure dans le système.  Les deux options ne sont pas pratique.
   1. Un capteur qui retourne un courant devra être adapté pour s'intégrer au reste de notre circuit
5. Si on retourne vraiment à la base de l'électromagnétisme, une différence de potentiel entre deux points (i.e. un gradient) nous dit qu'il y a un champ électrique entre ces deux points. Donc lorsque je mets une différence de potentiel entre deux points, les charges sont accélérées (i.e. il y a du courant).
6. Les résistances, capacitances et inductance sont regroupés sous le terme général *impédance*, qui est une résistance complexe.
7. Finalement, on décrira souvent les courants et les tensions en termes de fréquences d'oscillation.  On parle de DC pour les fréquences 0 Hz et AC pour les autres.
   1. Ne pas confondre $f$ et $\omega = 2\pi f$.  
8. Ainsi, puisque les circuits sont assez souvent linéaires, on décomposera en fréquences le courant et les tensions



## Règles (très) générales

- **Tension**
  1. Une tension moyenne dans un circuit simple est de l'ordre du Volt.
  2. # Une tension d'alimentation dans un circuit analogique est typiquement ±12V ou ±15V
  3. Un circuit logique de type TTL (i.e. *Transistor-To-Transistor-Logic*) fonctionne avec 0 V et 5 V comme signaux.
  4. Mesurer 1 Volt est facile.  Mesure 1 mV est difficile. Mesure 10 V est très facile.
  5. Un bruit typique dans les circuits de Monsieur-tout-monde est de l'ordre de quelques mVs.
- **Courant**
  1. Un courant moyen est de l'ordre de 10 à 100 µA
  2. Un très petit courant est en pA.
  3. Un courant très important est 1A

- **Résistance**
  1. Une résistance moyenne est de 10 kΩ.
  2. Une petite résistance résiduelle est de l'ordre de 1 à 10 Ω ou moins
  3. Une grande résistance d'entrée est de l'ordre de 1 à 10 MΩ.
  4. L'impédance d'une résistance est simplement $R$
  5. Les résistances en série s'additionnent pour donner la résistance totale $R_t = R_1 + R_2$
  6. En parallèle, on additionnent les inverses $R_t^{-1} = R_1^{-1} + R_2^{-1}$. Si ça vous surprend, c'est très simple: l'inverse de la résistance s'appelle la conductance.  Si j'ai deux "conduits" en parallèle, la "conductance" totale est la somme des deux, comme avec des tuyaux d'eau.
- **Capacitance**
1. Une capacitance moyenne est environ 1 µF
  2. Une capacitance ne laisse pas passer le courant continu. Son impédance diminue avec l'augmentation de la fréquence d'oscillation du courant ou de la tension.
  3. L'impédance d'une capacitance est $\frac{1}{j 2\pi f C}$.
  4. Les capacitances résiduelles de connecteurs sont de l'ordre de quelques pF.
  5. Un câble "standard" a une capacitance de 30 pF/m
- **Inductance**
  1. On travaille très peu avec les inductances
  2. Une inductance s'oppose au courant qui varie vite, et pas du tout au courant qui n'oscille pas. Son impédance augmente avec l'augmentation de la fréquence d'oscillation du courant ou de la tension.
  3. L'impédance d'une inductance est $j 2 \pi f L$
- **Batterie**
  1. Une batterie de maison AA contient une charge de 2000 mA-h (milli-ampère $\times$ heure), c'est-à-dire qu'elle peut fournir 2000 mA pendant une heure, ou 100 mA pendant 20 heures. 
- **Filtres**
  1. Un filtre RC a un temps caractéristique de $\tau = RC$ en  secondes



##Les appareils réels

![](HOWTO-Electronique.assets/image-20210129113556657.png)



1. Source de tension réelle: pour avoir la résistance interne d'une source de tension, c'est très simple:
   1. On mesure la tension avec un voltmètre dans le **circuit ouvert**, c'est-à-dire sans courant, en connectant directement le voltmètre aux bornes de la source.  Puisque le voltmètre a une résistance très élevé, il n'y a pas de courant et donc aucune perte de potentiel à travers la résistance interne, et on mesure directement $V_s$.
   2. Ensuite, on **ferme le circuit** avec une *résistance de charge*$R_c$ (pour que du courant passe) qu'on espère être proche de la résistance interne. On mesure la tension aux bornes de la résistance de charge. On l'appelera $V_c$, pour "tension aux bornes de la résistance de charge".  La tension mesurée sera plus faible que la tension $V_s$ car la résistance interne sera responsable d'une baisse de tension égale à $V_i = R_i I$, car maintenant, il y a du courant qui passe dans le circuit, contrairement à (1) où il n'y en avait pas.
   3. Puisque l'on sait $V_c$ et $R_c$, on peut calculer **le courant** qui passe dans la résistance de charge, et donc dans le circuit, avec $I= V_c/R_c$.
   4. Puisque la tension appliquée est $V_s$, et qu'une perte de tension de $V_c$ est mesurée à travers la résistance, on sait que la **perte de tension** dans la résistance interne est $V_i = V_s - V_c$ car la boucle doit passer de $V_c$ à 0V.
   5. On sait la perte de tension dans la résistance interne et on sait le courant, donc la résistance interne est simplement $R_i = R_c(V_s - V_c)/V_c$.

## Les résistances

À la base de plusieurs circuits, il y a les résistances.  Elles viennent en différents formats:

1. Elles ont des **valeurs standards** qui semblent bizarres (10, 12, 15, ... 82, etc...), mais il y a une raison: les valeurs par décade (entre 10 et 100, entre 100 et 1000, etc...) sont séparées de façon égales sur une échelle logarithmique, et toute combinaison de 2 résistances peut être à moins de 10% de n'importe quelle valeur désirée. Il existe plusieurs groupes: E12, E24, E48, E96 et E192 qui respectivement permettent une précision de 10% , 5%, 2%, 1% et 0.5%. De plus, il y a des valeurs standards de 10$\Omega$, 100$\Omega$, 1k$\Omega$, 10k$\Omega$, 100k$\Omega$ et 1M$\Omega$ parce que des fois, dans la vie, on aime les chiffres ronds.
2. Elles peuvent être faites pour **dissiper la puissance** un peu, moyen, beaucoup, ou énormément. Les plus fréquentes en laboratoires sont de 0.5W.  Plus elles sont grosses, plus elles dissipent beaucoup de puissance.
   <img src="HOWTO-Electronique.assets/resistor-wattage.jpg" alt="resistor wattage" style="zoom:25%;" />
3. Il existe des résistances variables appelées *potentiomètres*. Certains peuvent se mettre directement sur un *breadboard* (souvent ils sont bleus), d'autre se mettent sur des panneaux de contrôles et ils ont un bouton. Avec un bouton ou avec un tournevis, on peut ajuster la valeur de la résistance.
   <img src="HOWTO-Electronique.assets/3362P SERIES.jpg" alt="3362P Series" style="zoom:10%;" /> <img src="HOWTO-Electronique.assets/1200px-Electronic-Component-Potentiometer.jpg" alt="Potentiometer - Wikipedia" style="zoom:8%;" />
4. Les résistances sont simplement des mauvais conducteurs, avec des obstacles en différentes concentration pour obtenir une résistance désirée.  Ainsi,  au niveau microscopique, une charge accélèrera jusqu'à ce qu'elle entre en collision, recommencera à accélérer, etc... Au niveau macroscopique (i.e. intégré sur un temps de µs par exemple), elle semble avoir une vitesse moyenne constante.



## Les équivalences

On peut prendre un circuit d'une source de tension avec une résistance et la changer en circuit avec une source de courant équivalente, ce qui s'appelle l'équivalent de Norton:

$R_\text{Th} = R_\text{No}$

$V_\text{Th} = I_\text{No} R_\text{No}$

$I_\text{No} = \frac{V_\text{Th}}{R_\text{Th}}$



![img](HOWTO-Electronique.assets/260px-Norton-to-thevenin-20210128132127347.png)



## Équipement



| Description                                           |                          Apparence                           |
| ----------------------------------------------------- | :----------------------------------------------------------: |
| Multimètre                                            | <img src="HOWTO-Electronique.assets/multimeter-523153_960_720-5768a8193df78ca6e45dc883.jpg" alt="What Is a Multimeter?" style="zoom:15%;" /> |
| Câbles BNC ou coaxial                                 | <img src="HOWTO-Electronique.assets/2249-C-12.jpg" alt="2249-C-12" style="zoom:12%;" /> |
| Prises alligators                                     | <img src="HOWTO-Electronique.assets/71IFNUMDJML._AC_SL1500_.jpg" alt="img" style="zoom:12%;" /> |
| Prises bananes                                        | <img src="HOWTO-Electronique.assets/1325-02.jpg" alt="1325-02" style="zoom:15%;" /> |
| Résistances pour différentes dissipation de puissance | <img src="HOWTO-Electronique.assets/resistor-wattage.jpg" alt="resistor wattage" style="zoom:20%;" /> |



## TODO: Reste à faire

1. Voltage divider
2. RC HP, LP
3. Op-amp follower/buffer
4. Op-amp gain
5. Op-amp adder
6. Op-amp transimpedance
7. Numériseur
8. Instrumentation amplifier
9. https://artofelectronics.net










[^1]: J'étais nul en électronique au bacc. Nul. Zéro.  J'ai eu un déclic dans le cours Physique Expérimentale III en 1994 avec [Normand Balaux](https://www.coopfuneraire2rives.com/avis-de-deces/normand-balaux-147920/#ecrire) (que j'aimais beaucoup même s'il était extrêmement discret).  Par la suite, un stage d'été à Toronto en compagnie de l'excellent étudiant [Gary Allan](https://www.linkedin.com/in/gary-allan-6250a210/) m'a convaincu de l'importance d'apprendre l'électronique au moins pour être opérationnel au laboratoire. Pour graduer, j'ai dû faire beaucoup d'électronique, réparer des choses, en construire des nouvelles, automatiser mes montages, etc... À force d'en faire, les automatismes de laboratoire se sont transformés en connaissances.

