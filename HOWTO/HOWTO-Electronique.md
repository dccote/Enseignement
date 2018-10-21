# Les bases de l'électronique

On ne s'en sort pas: la connaissance de l'électronique est essentielle pour accomplir les moindre tâches en optique: photodétection, numérisation, contrôle d'appareils, interface microprocesseur, gestion USB, etc... Il y a deux façons d'aborder ce domaine: 1) en devenant opérationnel[^1] ou 2) en comprenant.  J'espère avec ce document faire le premier et possiblement le deuxième.

## Être opérationnel

### Commentaires généraux

1. Les circuits, aussi complexes soient-ils, se séparent toujours en petits blocs fonctionnels. Savoir reconnaître les blocs représente 90% de la bataille.
2. **On mesure des tensions, en Volts**. La raison pourquoi on travaille en tension plutôt qu'en courant est qu'une mesure en parallèle d'une tension n'affecte pas le système et est égale à la mesure qui nous intéresse. Si on mesurait des courants, on devrait faire un calcul pour obtenir le courant du système à partir de notre mesure (car les courants se séparent selon les résistances) et si on le mesurait en série on devrait s'inclure dans le système.  Les deux options ne sont pas pratique.
   1. Un capteur qui retourne un courant devra être adapté pour s'intégrer au reste de notre circuit
3. Les résistances, capacitances et inductance sont regroupés sous le terme général *impédance*, qui est une résistance complexe.
4. Une source de tension idéale a une impédance de sortie faible.
5. Une source de courant idéale a une impédance de sortie élevée.
6. On veut souvent qu'un appareil ait une impédance d'entrée de 50 Ω



**Règles du pouce**

- **Résistance**

  1. Une résistance moyenne est de 10 kΩ.
  2. Une petite résistance résiduelle est de l'ordre de 1 Ω au moins
  3. Une grande résistance d'entrée est de l'ordre de 1 à 10 MΩ.

- **Capacitance**

  1. Une capacitance moyenne est environ 1 µF
  2. Les capacitance résiduelles de connecteurs sont de l'ordre de quelques pF.
  3. Un câble a une capacitance de 30 pF/m

- **Inductance**

  1. On travaille très peu avec les inductances

- **Tension**

  1. Une tension moyenne dans un circuit simple est entre de l'ordre du Volt.
  2. Une tension d'alimentation dans un circuit est typiquement ±12V ou ±15V
  3. Un circuit TTL fonctionne avec 0 V et 5 V comme signaux.
  4. Mesurer 1 Volt est facile.  Mesure 1 mV est difficile. Mesure 10 V est très facile.
  5. Un bruit typique dans un circuit est de l'ordre du 1 mV.

- **Courant**

  1. Un courant moyen est de l'ordre de 10 à 100 µA
  2. Un très petit courant est en pA.
  3. Un courant très important est 1A

- **Batterie**

  1. Une batterie de maison AA contient 2000 mA-h (milli-ampère $\times$ heure).








### Commentaires photodétection

1. Les photodétecteurs produisent des courants de 0.5A/W.
2. 

[^1]: J'étais nul en électronique au bacc. Nul. Zéro.  J'ai eu un déclic dans le cours Physique Expérimentale III en 1994 avec [Normand Balaux](https://www.coopfuneraire2rives.com/avis-de-deces/normand-balaux-147920/#ecrire) (que j'aimais beaucoup même s'il était extrêmement discret).  Par la suite, un stage d'été à Toronto en compagnie de l'excellent étudiant [Gary Allan](https://www.linkedin.com/in/gary-allan-6250a210/) m'a convaincu de l'importance d'apprendre l'électronique au moins pour être opérationnel au laboratoire. Pour graduer, j'ai dû faire beaucoup d'électronique, réparer des choses, en construire des nouvelles, automatiser mes montages, etc... À force d'en faire, les automatismes de laboratoire se sont transformés en connaissances.

