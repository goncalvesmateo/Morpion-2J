# Morpion 2J

Il s'agit d'un code Python qui implémente le jeu de Tic-Tac-Toe (ou Morpion) pour deux joueurs.

Deux plateaux sont affichés à chaque tour :
- Le plateau blanc est le plateau de jeu.
- Le plateau jaune est le plateau d'aide, il indique le numéro à entrer (de 1 à 9) pour positionner son symbole dans le plateau blanc.

Les joueurs choisissent leur symbole (un caractère ASCII sauf le caractère " ") et l'algorithme vérifie à chaque tour si le jeu est gagné par un des deux joueurs ou s'il y a égalité.
## Fonctions et Variables

1. Variables

- La variable boolJeu est une chaîne de caractères qui contient la valeur "O" (oui) ou "o". La boucle while s'exécute tant que boolJeu a l'une des deux valeurs "O" ou "o", ce qui permet de jouer plusieurs parties à la suite sans avoir à relancer le programme.

- La variable J1win est un booléen qui est initialisé à False. Elle sera mise à True si le joueur 1 remporte la partie.

- La variable J2win est également un booléen qui est initialisé à False et sera mise à True si le joueur 2 remporte la partie.

- La variable casesLibres compte le nombre de cases vides.

- La variable caseValide est initialisée à False et est utilisée pour vérifier si la case saisie par le joueur est valide (c'est-à-dire si elle existe ou si elle n'est pas occupée par l'adversaire).

2. Fonctions

- La fonction plateau() affiche le plateau de jeu.

- La fonction winVerify(x) vérifie si un joueur a gagné la partie.

- La fonction case(x) est utilisée pour remplir une case libre. Si le joueur entre un nombre en dehors de l'intervalle [1, 9], le caractère sera saisi au milieu du plateau.

- Le programme efface la console à chaque tour à l'aide de la commande os.system('cls') pour que le plateau soit toujours affiché en haut de la console.


## Screenshots

![J1wins](https://media.discordapp.net/attachments/1077695127323152524/1077695147678113885/image.png)

![J2wins](https://media.discordapp.net/attachments/1077695127323152524/1077697092740460574/image.png)

![Stalemate](https://media.discordapp.net/attachments/1077695127323152524/1077697907324620810/image.png)
## Logiciels utilisés

Les IDE utilisés pour la réalisation de ce code sont Thonny et Visual Studio Code.
## Documentation

Ce code Python utilise les bibliothèques "colorama" et "os"

[Bibliothèque "Colorama"](https://pypi.org/project/colorama/)

[Module "os"](https://docs.python.org/fr/3/library/os.html)

