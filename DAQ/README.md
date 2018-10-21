# DAQ: un tutoriel sur l'acquisition de données

Dans cette section, on retrouve une série de tutoriels à lire et à faire dans l'ordre. Les documents sont disponibles en format PDF et Markdown.

Je le laisse publiquement accessible par choix.  Tout le monde peut lire, faire et commenter ces tutoriels:

1. Le [tutoriel sur le DAQ](https://github.com/dccote/Enseignement/tree/master/DAQ) sur retrouve sur GitHub.
2. À l'intérieur vous trouverez:
   1. Les textes complets en format Markdown, avec des liens vers les images dans  un répertoire nommé `assets`.
   2. Les textes complets, en PDF, mis à jour régulièrement (car Typora support les équations LaTeX, mais pas GitHub).
   3. Les fichiers sources, en Python, pour programmer.

Vous pouvez me contacter à [dccote@cervo.ulaval.ca](mailto:dccote@cervo.ulaval.ca)



## Plan potentiel (et réel)

1. [Semaine 01](./Semaine-01.md): Pourquoi faire ce tutoriel?
2. [Semaine 02](./Semaine-02.md): Entrées-sorties numériques simples
   1. On fait un circuit simple pour obtenir des entrées-sorties avec la puce UM232R
   2. Installer python in libftdi avec Anaconda
   3. Vérifier avec un oscilloscope l'état des *lignes*
   4. Allumer une DEL
   5. Faire clignoter une DEL
   6. Faire un ECHO
3. Semaine-03: La communication par RS-232
   1. Qu'est-ce qu'un protocole?
   2. Pourquoi RS-232? 
   3. Pourquoi USB?
   4. Communiquer entre deux appareils