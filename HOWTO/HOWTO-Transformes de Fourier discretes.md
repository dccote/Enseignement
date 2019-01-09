Introduction
============

La transformée de Fourier est un outil mathématique qui permet de
représenter une fonction par une autre fonction qui contient la même
information totale, mais d’une façon différente. On peut parler de série
temporelle ou de son spectre par exemple, les deux contenant la même
information mais la présentant différemment. Le document présente les
notions pratiques de base pour pouvoir adéquatement analyser un signal
et obtenir son spectre de Fourier, calibré correctement.

Définitions
===========

La transformée de Fourier est définie pour une fonction connue $f(x)$
comme: 


$$
F(k) = \int_{-\infty}^{+\infty} f(x) e^{ikx} dx
$$

et sa transformée inverse est ainsi:
$$
f(x) = \frac{1}{2\pi} \int_{-\infty}^{+\infty} F(k) e^{-ikx} dk
$$
La
variable $k$ est la variable conjuguée de $x$ et correspond à une
fréquence angulaire $k=2 \pi \nu$, la fonction $F(k)$ est souvent
appelée le spectre de $f(x)$. Notons que la variable $x$ peut-être une
variable d’espace ($m$) ou de temps ($s$). Ainsi, la variable conjuguée
$k$ aura respectivement des unités de $\mathrm{rad} \cdot m^{-1}$ ou
$\mathrm{rad} \cdot s^{-1}$, et la variable $\nu$ aura des unités de
$m^{-1}$ ou $s^{-1}$. Pour calculer cette transformation, la fonction
$f(x)$ doit être connue sur l’intervalle complet de $-\infty$ à
$+\infty$.

Au laboratoire, on peut mesurer des signaux par échantillonnage discret:
plutôt que d’avoir la représentation continue du signal, on ne connait
la valeur de la fonction qu’à certains points discrets
$x_j = j \Delta x$. On écrira parfois simplement $f[x_i]$, pour rappeler
la syntaxe informatique pour l’accès d’un tableau. On définit la
transformée de Fourier discrète comme:

$$
F[\nu_i] = \sum_{j=0}^{N-1} f[x_j] e^{i 2 \pi \nu_i x_j}
$$
et sa transformée inverse:

$$
f[x_i] = \frac{1}{N} \sum_{j=0}^{N-1} F[\nu_j] e^{-i 2 \pi \nu_j x_i}.
$$

Ainsi, avec un tableau de données $f$ contenant $N$ points, on peut
obtenir un second tableau $F$ contenant aussi $N$ points. Si
l’espacement entre les points de $f$ est de $\Delta X$, l’étendue du
tableau est de $N \Delta X$. Après transformation de Fourier, le tableau
en $F$ sera défini de $] -\nu_{\mathrm{max}}, \nu_{\mathrm{max}} ]$ avec
: 

$$
\begin{aligned}
\Delta \nu  & = & \frac{1}{N \Delta X} \\ 
\nu_{\mathrm{max}}  & = & \frac{1}{2 \Delta X} \end{aligned}
$$

Notez:

1.  La transformée de Fourier discrète est définie sur les fréquences
    négatives et positives, de $-\nu_{\mathrm{max}}$ à
    $\nu_{\mathrm{max}}$.

2.  Avec une fonction réelle $f(x)$, les composantes négatives et
    positives des fréquences seront identiques et réelles.

3.  La composante $F[0]$ est la composante continue, ou DC, ou dit
    autrement la moyenne du signal $f[x]$.

4.  La grande majorité des programmes (MATLAB, Mathematica, etc...)
    retourne le tableau en commençant par les composantes positives
    suivi par les composantes négatives.

5.  La grande majorité des programmes (MATLAB, Mathematica, etc...)
    travaille dans l’espace de Fourier avec $\nu$, et non $k=2 \pi \nu​$.
    Ceci correspond mieux à la réalité (i.e. les fréquences sont des
    vraies fréquences, comme par exemple 60 Hz est 60 Hz, pas 376 rad
    Hz).

6.  Les composantes $\nu_{\mathrm{max}} $ et $-\nu_{\mathrm{max}} $ sont
    identiques et sont au $N/2$-ième point du tableau.

7.  La première composante du tableau est celle correspondant à
    $0 \Delta \nu$, suivies de $\Delta \nu$, $2 \Delta \nu$, etc...
    jusqu’à $(N/2) \Delta \nu$. Le dernier point du tableau est
    $- \Delta \nu$, l’avant dernier est $-2\Delta \nu$, précédé par
    $-3 \Delta \nu$. Vous pourrez vérifier que le point que le dernier
    point du tableau est égal au deuxième, etc...

![Illustration d'un signal numérique et de sa transformée de Fourier,
tels que conservés dans un logiciel comme
MATLAB.[]{data-label="fig:signalEtFFT"}](assets/Numerisation.pdf){width="4in"}