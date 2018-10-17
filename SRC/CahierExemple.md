# Données exemples pour graphiques

Voici des données pour tester le script qui extrait les données et qui affiche le graphique


| Tension [V] | Intensite raltive |
| ----------- | ----------------- |
| 1           | 8                 |
| 2.4         | 7                 |
| 3.2         | 7                 |
| 4.0         | 6.5               |
| 5.          | .9                |
| 6           | 0.5               |



Prendre le script python [plotTableFromMarkdown.py](./plotTableFromMarkdown.py) et utiliser:

```
python plotTableFromMarkdown.py CahierExemple.md
```

- Essai pour des tables multiple (plus de 2 tables)

| Distance [m] | Altitude[m] |
| ------------ | ----------- |
| 1            | 5.          |
| 2.24m        | 4           |
| 3m           | 0.002       |
| 4.0          | .0222       |
| 5.           | .5          |
| 6            | 0.5         |

- Essai pour table à multiples colonnes

  | Pixel | Spectre étalon 1[nm] | Spectre étalon 2[nm] |
  | ----- | -------------------- | -------------------- |
  | 1     | 500.14nm             | 400.26nm             |
  | 2     | 600                  | 500                  |
  | 3     | 400                  | 300                  |
  | 4     | 200                  | 0                    |
  |       |                      |                      |