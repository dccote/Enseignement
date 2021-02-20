# La résistance de charge

Le résistance de charge (ou impédance de charge de façon plus générale) est un terme très général: il s'agit de la résistance qu'une partie de circuit (par exemple, le bloc d'alimentation) verra lorsqu'on le branchera sur un autre circuit (par exemple, un détecteur). Cette résistance détermine "la charge" (load en anglais) qui sera perçue et déterminera directement **le transfert de puissance entre ces deux éléments**. Nous allons rapidement comprendre pourquoi c'est important.

## Un exemple simple: transfert de puissance

Illustrons le tout avec un système très simple: un bloc d'alimentation branché dans un moteur.  Vous avez peut-être la réaction: "Mais je ne connais pas les moteurs! Ni les blocs d'alimentation en fait! Argghhh!".  Ce n'est pas important pour comprendre. En effet, on peut toujours simplifier les circuits: par exemple une source de tension, vous l'avez vu, est une source parfaite avec une résistance interne appelée "résistance de sortie".  À l'opposé, un moteur peut être simplifié comme étant "une résistance d'entrée" avec "le reste qui fait tourner le moteur, cependant, la partie importante: un bloc d'alimentation qu'on branche dans le moteur verra "la résistance d'entrée".

![image-20210220134321942](HOWTO-La résistance de charge.assets/image-20210220134321942.png)

Regardons ce qui se passe lorsque le bloc d'alimentation est connecté sur le moteur avec tous deux leurs résistance $R_\text{s}$ et $R_\text{m}$. Regardons les deux cas limites: supposons que la résistance du moteur $R_\text{m}$ est quasi-nulle ou extrêmement élevée et *regardons où la puissance est dissipée*.

Le courant dans le circuit est toujours $I = V_s/R_t$, où $R_t$ est a résistance totale donc $R_s + R_m$.

**Si $R_\text{m}$ est presque nulle**, alors le courant qui sortira du bloc d'alimentation sera donné par la résistance de la source: $I = V_s/R_s$.  Ce courant se propagera dans les résistances de la source et du moteur ($R_s$ et $R_m$) et dissipera une puissance égale à la perte de tension ($RI$) dans chacune fois le courant ($I$), donc $RI^2$. On obtient rapidement que la puissance dissipée dans la source est de $P_s = V^2/R_s$ alors qu'elle est $P_s = R_m V^2_s/R^2_s \equiv 0$ car $R_m$ est nulle.  Donc ce cas limite, le moteur ne retire aucune puissance électrique du moteur, donc évidemment, quel que soit le mécanisme interne pour transformer la puissamce électrique en mouvement de moteur, le moteur ne pourra rien faire car il n'a aucune puissance.

**Si $R_\text{m}$ est très élevée**, alors le courant qui sortira du bloc d'alimentation sera donné par la résistance du moteur: $I = V_s/R_m$ (donc le courant fourni est très faible).  Ce courant se propagera dans les résistances de la source et du moteur ($R_s$ et $R_m$) et on obtient rapidement que la puissance dissipée dans la source et dans la charge du moteur est  $P_s = R_s V^2_s/R_m^2$ donc essentiellement nulle alors qu'elle est $P_s = V^2_s/R_m$ qui est elle aussi presque nulle puisque encore une fois, le courant est très faible.  Dans ce cas limite, tout comme dans le premier, le moteur ne retire aucune puissance électrique du bloc d'alimentation, mais pour une raison différente: la résistance interne très élevée ne permet pas au bloc d'alimenation de fournir de courant. Encore une fois, évidemment, quel que soit le mécanisme interne pour transformer la puissamce électrique en mouvement de moteur, le moteur ne pourra rien faire car il n'a aucune puissance.

On peut faire un graphique très simple de la puissance dissipée dans la résistance interne du bloc d'alimentation et dans le moteur en fonction de la résistance du moteur:  $P_s = R_s V^2_s/(R_s + R_m)^2$ et $P_m = R_m V_s^2/(R_s + R_m)^2$.  SI on prend une résistance de source de 50 $\Omega$ et une tension de 15V, on obtient le graphique suivant:

![image-20210220143717499](HOWTO-La résistance de charge.assets/image-20210220143717499.png)

Quelles sont les grandes conclusion de ce graphique?

1. Si la résistance de charge est égale à celle de la source, la charge extrait le maximum de puissance de la source (ici, 1W, indiqué sur le graphique par la flèche).

2. Si la résistance de charge est égale à celle de la source, la charge et le bloc d'alimentation dissipe la même quantité de puissance (1W), pour un total de 2W pour le moteur et le bloc d'alimentaiton (courbe pointillée bleue).

3. Si la résistance de charge est très faible (la gauche du graphique), le bloc d'alimentation fournit beaucoup de courant qui ne fait que dissiper de la puissance à l'intérieur de ce bloc: ça ne nous sert pas beaucoup, il n'y a rien au moteur, on ne fait que chauffer le bloc d'alimentation pour rien, sans que notre moteur ne reçoive de puissance.

4. Si la résistance de charge est très grande (le droite du graphique), alors le bloc d'alimentation fournit très peu de courant et aucune puissance n'est dissipée nulle part: encore une fois, ça ne nous sert pas beaucoup, il n'y a rien au moteur.

5. Dans le cas où la résistance interne du bloc d'alimentation est quasi-nulle, alors toute la puissance est transférée au moteur parfaitement: le bloc ne consomme rien, il ne fait que transférer la puisssance. (Wow!).

    

Est-ce important? Supposons que vous faites un appareil à batterie.  L'énergie dans les batteries est limitée.  On veut transférer la puissance le mieux possible, on ne veut pas la perdre pour rien dans le bloc d'alimentation. Avec la dominance des appareils mobiles, la gestion de la puissance est importante. Une autre façon de voir la même situation: supposons que vous avez un moteur avec une résistance interne de 10 $\Omega$: sur le graphique, on voit que le moteur n'aura que 0.5W de puissance alors que le moteur dissipera 3.3 W ! Si vous payez l'électricité, vous devez payer pour environ 4W de puissance alors que vous ne "bénéficiez" que de 0.3W sur votre moteur! Il est donc avantageux d'avoir un bloc d'alimentation qui est "matché" à votre appareil pour utiliser la puissance efficacement.


## Input/output impédance

 Cette question de transfert de puissance est en fait partout: à tout moment, on "connecte" une partie de circuit à une autre partie de circuit. Si on ne se préoccupe pas des impédances d'entrée et de sortie et qu'elles ne sont pas appropriées (i.e. *matchées*), alors partout dans le circuit la puissance sera gaspillée dans des résistance internes qui ne contribuent pas à notre objectif final (à moins, bien sûr, que notre plan soit de chauffer la pièce).  Ainsi, si on fait un filtre RC que l'on veut mettre dans un circuit, on voudra tenter d'avoir une impédance égale à l'impédance de sortie du circuit après lequel on le branche. 

On peut généraliser la discussion en terme des impédances au lieu simplement des résistances.  On parlera d'une charge capacitive ou inductive, ou simplement résistive.  On utilise $R$, $-j/\omega C$, $j \omega L$ et on refait les calculs, on obtiendra essentiellement les mêmes résultats.

## Standards

En fait, puisque ce concept de transfert de puissance est central à toute conception de circuit, il existe plusieurs "standard":

1. Les blocs d'alimentation ont typiquement quelques Ohms de résistance interne
2. Beaucoup d'appareils ont des impédances d'entrée de 50$\Omega$.
3. L'équipement audio (haut-parleurs, micro) ont des impédances assez variables (8 $\Omega$ pour les haut-parleurs, mais souvent 600 $\Omega$, allez voir [SoundOnSound](https://www.soundonsound.com/techniques/understanding-impedance) pour une discussion) et c'est pourquoi il est important de bien les verifier: si un micro n'a pas la bonne impédance de sortie, alors le transfert de puissance (i.e. le son) sera trop faible ou aura trop de distortion par exemple.