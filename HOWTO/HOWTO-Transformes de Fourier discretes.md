Introduction
============

La transformée de Fourier est un outil mathématique qui permet de
représenter une fonction (dans le temps ou l'espace par exemple) par une autre fonction qui contient la même
information totale, mais qui l'exprime sous la forme d'une somme de composantes harmoniques (en fréquences temporelles ou spatiales). On peut parler de série
temporelle et de son spectre par exemple, les deux contenant la même
information mais la présentant différemment. Le document présente les
notions pratiques de base pour pouvoir adéquatement analyser un signal
et obtenir son spectre de Fourier, étalonné correctement.

La connaissance et la maitrise de cette transformation en science est importante: nous mesurons souvent dans le temps, mais l'origine des phénomènes a souvent une composante oscillatoire (par exemple, autour d'un point d'équilibre, le comportement de rappel est souvent une oscillation harmonique, ou encore les émissions provenant des atomes sont des ondes à des fréquences spécifiques, etc…). Ainsi, la description dans l'espace de Fourier est souvent un élément clef pour comprendre ou mesurer un phénomène.

Définitions
===========

Il y a plusieurs définitions de la transformée de Fourier.  Une des définitions pour une fonction $f(x)$
est donné par: 

$$
\label{defFourier} F(k) = \int_{-\infty}^{+\infty} f(x) e^{ikx} dx,
$$

et sa transformée inverse est ainsi:
$$
f(x) = \frac{1}{2\pi} \int_{-\infty}^{+\infty} F(k) e^{-ikx} dk.
$$
La
variable $k​$ est la variable conjuguée de $x​$ et correspond à une
fréquence angulaire $k=2 \pi \nu​$, la fonction $F(k)​$ est souvent
appelée le spectre de $f(x)​$. Notons que la variable $x​$ peut-être une
variable d’espace ($m​$) ou de temps ($s​$). Ainsi, la variable conjuguée
$k​$ aura respectivement des unités de $\mathrm{rad} \cdot m^{-1}​$ ou
$\mathrm{rad} \cdot s^{-1}​$, et la variable $\nu​$ aura des unités de
$m^{-1}​$ ou $s^{-1}​$. Pour calculer cette transformation, la fonction
$f(x)​$ doit être connue sur l’intervalle complet de $-\infty​$ à
$+\infty​$.

> Peut-être vous demandez-vous pourquoi l'équation $(\ref{defFourier})$ est complexe?

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
    $\nu_{\mathrm{max}}​$.

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



# Les phaseurs, les fréquences négatives, la phase

1. La notation phaseur n'a rien de sorcier: elle est simplement plus facile à manipuler: l'intégrale de $e^{ix} dx$ est plus facile et plus courte que $(\cos(x)+i\sin(x))dx$ . Inversement, plutôt que de travailler avec des sinus et des cosinus, on ré-écrit en notation phaseur.

2. Elle est tellement plus facile que c'est la norme, et c'est tellement la norme qu'on n'écrit même plus le complexe conjugué dans les équations en ne faisant l'integrale que sur les fréquences positives. En effet, on devrait vraiment toujours écrire:

   $$
   f(x) = \frac{1}{2\pi} \int_{0}^{+\infty} F(k) e^{-ikx} dk + \text{c.c.}
   $$

   Cependant, on ne le fait pas: on fait l'intégrale de $-\infty$ à
   $+\infty$ et on dit que $F(k)$ est hermétienne, c'est à dire $F(-k) = F^*(k)​$. C'est une supposition implicite qui est répandue et plus personne ne le répète après le deuxième cours de physique mathématique à la première session.

3. Sachant cela, on se retrouve avec des fréquences positives et négatives pour décrire une oscillation  sinusoidale car si on prend l'exemple le plus simple d'une oscillation harmonique à une fréquence spécifique constante $k_\circ$, on obtient :

   $$
   F(k) = \frac{1}{2\pi}\int_{-\infty}^{+\infty} \cos(k_\circ x) e^{ikx} dx,
   $$
   $$
   F(k) = \frac{1}{2\pi}\int_{-\infty}^{+\infty} \frac{e^{ik_\circ x}+e^{-ik_\circ x}}{2} e^{ikx} dx,
   $$

   $$
   F(k) = \frac{1}{2\pi}\int_{-\infty}^{+\infty} \frac{e^{i(k_\circ+k) x}}{2}+\frac{1}{2\pi}\int_{-\infty}^{+\infty}\frac{e^{-i(k_\circ-k) x}}{2} dx,
   $$
   $$
   F(k) = \delta(k+k_\circ) + \delta(k-k_\circ),
   $$

   On dit qu'il y a une composante à $+k_\circ$ et $-k_\circ$. Le sens profond n'est rien de plus que la somme des composantes exponentielles doit toujours donner une fonction réelle, donc on se doit d'avoir les deux composantes, et leurs amplitudes doivent être complexes conjuguées.

