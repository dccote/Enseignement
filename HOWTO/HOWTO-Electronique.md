# Les bases de l'électronique

On ne s'en sort pas: la connaissance de l'électronique est essentielle pour accomplir les moindre tâches en optique: photodétection, numérisation, contrôle d'appareils, interface microprocesseur, gestion USB, etc... Il y a deux façons d'aborder ce domaine: 1) en devenant opérationnel[^1] ou 2) en comprenant[^1]. S'il y avait un seul conseil que je donnerais: les circuits, aussi complexes soient-ils, se séparent toujours en petits blocs fonctionnels. Savoir reconnaître les blocs représente 90% de la bataille.  J'espère avec ce document faire le premier et possiblement le deuxième.

En terminant:

1. Briser un fil, brûler une résistance, écraser un condensateur, brancher un transistor à l'envers, péter un chip à 10$ fait partie de l'apprentissage. Ce n'est pas grave: c'est quelques dollars. Voir 2.
2. Brancher 100V dans un oscilloscope de 3000$ et le péter, mettre ses mains ou sa langue sur 1200V et finir à l'hôpital, brûler une puce à 200\$ qui a un temps de livraison de 8 semaines, faire sauter le microntrolleur d'un laser commercial, fait partie de la liste des choses qui font que les gens se font mettre dehors.  Apprenez la différence avec 1.



## Vraiment: les bases

![image-20210128123012217](HOWTO-Electronique.assets/image-20210128123012217.png)

1. Une source de tension idéale donne une différence de potentiel constante entre ses bornes, quelle que soit la résistance connectée entre ses bornes.
2. Une source de courant idéale donne un courant constant quelle que soit la résistance connectée entre ses bornes.
3. Un voltmètre idéal a une résistance "infinie" et mesure la différence de potentiel entre ses bornes sans prendre de courant.
4. Un ampèremètre idéal a une résistance nulle et mesure le courant qui passe entre ses bornes sans perte de potentiel.

## Être opérationnel

### Commentaires généraux

1. **On mesure des tensions, en Volts**. La raison pourquoi on travaille en tension plutôt qu'en courant est qu'une mesure en parallèle d'une tension n'affecte pas le système et est égale à la mesure qui nous intéresse. Si on mesurait des courants, on devrait faire un calcul pour obtenir le courant du système à partir de notre mesure (car les courants se séparent selon les résistances) et si on le mesurait en série on devrait s'inclure dans le système.  Les deux options ne sont pas pratique.
   1. Un capteur qui retourne un courant devra être adapté pour s'intégrer au reste de notre circuit
2. Les résistances, capacitances et inductance sont regroupés sous le terme général *impédance*, qui est une résistance complexe.
3. Une source de tension idéale a une impédance de sortie faible.
4. Une source de courant idéale a une impédance de sortie élevée.
5. On veut souvent qu'un appareil ait une impédance d'entrée de 50 Ω (s'il accepte du courant) ou élevé par exemple 1MΩ (s'il doit être en parallèle sans affecter le circuit).
6. Finalement, on décrira souvent les courants et les tensions en termes de fréquences d'oscillation.  On parle de DC pour les fréquences 0 Hz et AC pour les autres.
   1. Ne pas confondre $f$ et $\omega = 2\pi f$.  



**Règles du pouce**

- $V = RI$
- **Résistance**
  1. Une résistance moyenne est de 10 kΩ.
  2. Une petite résistance résiduelle est de l'ordre de 1 Ω ou moins
  3. Une grande résistance d'entrée est de l'ordre de 1 à 10 MΩ.
- **Capacitance**

  1. Une capacitance moyenne est environ 1 µF
  2. Une capacitance ne laisse pas passer le courant continu. Son impédance diminue avec l'augmentation de la fréquence d'oscillation du courant ou de la tension.
  3. L'impédance d'une capacitance est $\frac{1}{j 2\pi f C}$.
  4. Les capacitance résiduelles de connecteurs sont de l'ordre de quelques pF.
  5. Un câble a une capacitance de 30 pF/m
- **Inductance**
  1. On travaille très peu avec les inductances
  2. Une inductance s'oppose au courant qui varie vite, et pas du tout au courant qui n'osccile pas. Son impédance augmente avec l'augmentation de la fréquence d'oscillation du courant ou de la tension.
  3. L'impédance d'une inductance est $j 2 \pi f L$
- **Tension**

  1. Une tension moyenne dans un circuit simple est entre de l'ordre du Volt.
  2. Une tension d'alimentation dans un circuit est typiquement ±12V ou ±15V
  3. Un circuit logique TTL fonctionne avec 0 V et 5 V comme signaux.
  4. Mesurer 1 Volt est facile.  Mesure 1 mV est difficile. Mesure 10 V est très facile.
  5. Un bruit typique dans un circuit est de l'ordre du 1 mV.
- **Courant**

  1. Un courant moyen est de l'ordre de 10 à 100 µA
  2. Un très petit courant est en pA.
  3. Un courant très important est 1A
- **Batterie**
  1. Une batterie de maison AA contient 2000 mA-h (milli-ampère $\times$ heure).
- **Filtres**
  1. Un filtre RC a un temps caractéristique de $\tau = RC$ en  secondes



### Blocs fonctionnels à décrire

1. RC HP, LP

2. Op-amp follower/buffer

3. Op-amp gain

4. Op-amp transimpedance

5. Op-amp adder

6. Numeriseur

7. Instrumentaiton amplifier

8. https://artofelectronics.net




### Commentaires photodétection

1. Les photodétecteurs produisent des courants de 0.5A/W.










[^1]: J'étais nul en électronique au bacc. Nul. Zéro.  J'ai eu un déclic dans le cours Physique Expérimentale III en 1994 avec [Normand Balaux](https://www.coopfuneraire2rives.com/avis-de-deces/normand-balaux-147920/#ecrire) (que j'aimais beaucoup même s'il était extrêmement discret).  Par la suite, un stage d'été à Toronto en compagnie de l'excellent étudiant [Gary Allan](https://www.linkedin.com/in/gary-allan-6250a210/) m'a convaincu de l'importance d'apprendre l'électronique au moins pour être opérationnel au laboratoire. Pour graduer, j'ai dû faire beaucoup d'électronique, réparer des choses, en construire des nouvelles, automatiser mes montages, etc... À force d'en faire, les automatismes de laboratoire se sont transformés en connaissances.

