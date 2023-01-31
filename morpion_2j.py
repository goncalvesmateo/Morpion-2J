#######################
## Morpion 2 joueurs ##
#######################

# GitHub : @goncalvesmateo

# Bibliothèques importées
from colorama import Fore, Style    # Couleur du texte
import os                           # Effacer la console python

boolJeu = "O"
pointsJ1 = 0
pointsJ2 = 0

while boolJeu == "O" or boolJeu == "o":
    os.system('cls')
    # Booléens qui désigneront le joueur gagnant
    J1win = False
    J2win = False

    # Entier qui comptera le nombre de cases vides
    casesLibres = 9

    # Booléen qui verifiera si la case saisi est valide (si elle est vide)
    caseValide = False

    # Croix des joueurs
    # Définis initialement avec 0 caractère
    J1perso = ""
    J2perso = ""

    # Tableau du plateau de jeu (servira pour l'affichage des carcatères
    Morpion = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

    # Affiche le plateau de jeu ainsi que l'aide sur le choix de la case
    def plateau():
        os.system('cls')
        print(Fore.LIGHTCYAN_EX + Style.BRIGHT + "--+ Jeu du morpion 2 joueurs +--" + Style.RESET_ALL)			# Nom du jeu écrit en cyan clair et en gras
        print()																									# Espace pour l'esthétique
        print("J1 :",J1perso,"|",pointsJ1,"-",pointsJ2,"|","J2 :",J2perso)  									# Affichage des caractères choisis
        print("Encore",casesLibres,"cases libres")  															# Affichage du nombre de cases libres
        print()																									# Espace pour l'esthétique
        
        # Le plateau d'aide est ici affiché en jaune clair
        print(Morpion[6],"|",Morpion[7],"|",Morpion[8]," | " + Fore.YELLOW + " 7 | 8 | 9" + Style.RESET_ALL)	# Ligne supérieure
        print("--+---+--  | " + Fore.YELLOW + " --+---+--" + Style.RESET_ALL)									# Délimitation des cases
        print(Morpion[3],"|",Morpion[4],"|",Morpion[5]," | " + Fore.YELLOW + " 4 | 5 | 6" + Style.RESET_ALL)	# Ligne centrale
        print("--+---+--  | " + Fore.YELLOW + " --+---+--" + Style.RESET_ALL)									# Délimitation des cases
        print(Morpion[0],"|",Morpion[1],"|",Morpion[2]," | " +  Fore.YELLOW + " 1 | 2 | 3" + Style.RESET_ALL)	# Ligne inférieure
        print()																									# Espace pour l'esthétique

    # Vérifie si le jeu est gagné par un des deux joueurs ou s'il y a égalité
    def winVerify(x):
        # Définit toutes les conditions de victoire (une ligne verticale, horizontale ou diagonale)
        y = ((Morpion[0] == x and Morpion[1] == x and Morpion[2] == x) or (Morpion[3] == x and Morpion[4] == x and Morpion[5] == x) or (Morpion[6] == x and Morpion[7] == x and Morpion[8] == x) or (Morpion[0] == x and Morpion[3] == x and Morpion[6] == x) or (Morpion[1] == x and Morpion[4] == x and Morpion[7] == x) or (Morpion[2] == x and Morpion[5] == x and Morpion[8] == x) or (Morpion[0] == x and Morpion[4] == x and Morpion[8] == x) or (Morpion[2] == x and Morpion[4] == x and Morpion[6] == x))
        return (y)

    # Utilise une case libre
    # Le caractère sera saisi au milieu du plateau si le joueur entre un nombre hors de l'intervalle [1, 9]
    def case(x):
        if x > 9 or x < 1:
            x = 5
        return (x)

    # Les deux joueurs choisisssent un seul caractère qui fera office de choix et de rond
    print(Fore.LIGHTCYAN_EX + Style.BRIGHT + "--+ Jeu du morpion 2 joueurs +--" + Style.RESET_ALL)
    print(Fore.RED + "----+ Choix des caractères +----" + Style.RESET_ALL)
    print()
    while len(J1perso) != 1 or J1perso == " ":
        J1perso = input("J1 - Choisissez un caractère : ")
        if len(J1perso) != 1 or J1perso == " ":
            print("Veuillez saisir un seul caractère.")
            print()
    print()

    while len(J2perso) != 1 or J2perso == " ":
        J2perso = input("J2 - Choisissez un caractère : ")
        if len(J2perso) != 1 or J2perso == " ":
            print("Veuillez saisir un seul caractère.")
            print()
        # Le joueur 2 ne doit pas choisir le même caractère que le joueur 1
        if J2perso == J1perso:
            print("Ce caractère est déja utilisé")
            print()
            J2perso = ""

    # Tant que les deux joueurs n'ont pas gagné
    while J1win == False and J2win == False:
        
        # Choix de la case pour le joueur 1
        caseValide = False
        if J2win == False or casesLibres > 0:
            while True:
                try:
                    plateau()
                    J1tour = int(input("J1 - Choisissez une case libre : "))
                    break
                except ValueError:
                    plateau()
            J1tour = case(J1tour)
            while caseValide == False:
                
                # Si la case existe et est vide
                if Morpion[J1tour - 1] == " ":
                    
                    Morpion[J1tour - 1] = J1perso		# Affiche le caractère du joueur 1 dans la case
                    casesLibres = casesLibres - 1		# Le nombre de cases vides diminue
                    J1win = winVerify(J1perso)			# Vérifie si le jeu est gagné ou non
                    caseValide = True
                else:
                    plateau()
                    J1tour = int(input("J1 - Entrée invalide, choisissez une case libre : "))
                    
        # Le jeu s'arrète si toutes les cases sont utilisées ou si le joueur 1 a gagné
        if casesLibres == 0 or J1win == True:
            break

        # Choix de la case pour le joueur 2
        caseValide = False
        if J1win == False or casesLibres > 0:
            while True:
                try:
                    plateau()
                    J2tour = int(input("J2 - Choisissez une case libre : "))
                    break
                except ValueError:
                    plateau()
            J2tour = case(J2tour)
            while caseValide == False:
                
                # Si la case existe et est vide
                if Morpion[J2tour - 1] == " ":
                    
                    Morpion[J2tour - 1] = J2perso		# Affiche le caractère du joueur 2 dans la case
                    casesLibres = casesLibres - 1		# Le nombre de cases vides diminue
                    J2win = winVerify(J2perso)			# Vérifie si le jeu est gagné ou non
                    caseValide = True
                else:
                    plateau()
                    J2tour = int(input("J2 - Entrée invalide, choisissez une case libre : "))
        
        # Le jeu s'arrète si toutes les cases sont utilisées ou si le joueur 2 a gagné
        if casesLibres == 0 or J2win == True:
            break

    # Affiche un message de victoire ou d'égalité
    if J1win == True:
        plateau()
        print(Fore.LIGHTGREEN_EX + "Le joueur 1 à gagné." + Style.RESET_ALL)
        pointsJ1 += 1
    elif J2win == True:
        plateau()
        print(Fore.LIGHTRED_EX + "Le joueur 2 à gagné." + Style.RESET_ALL)
        pointsJ2 += 1
    else:
        plateau()
        print(Fore.LIGHTBLUE_EX + "Égalité" + Style.RESET_ALL)

    # Demande si l'on souhaite refaire une partie
    boolJeu = input("Refaire une partie ? [O:N] ")
    print()

# Détermine le vainqueur en fonction des points
if pointsJ1 > pointsJ2:
    print(Fore.LIGHTGREEN_EX + "Le jeu est terminé, le joueur 1 l'emporte",pointsJ1,"à",pointsJ2, Style.RESET_ALL)
elif pointsJ1 < pointsJ2:
    print(Fore.LIGHTRED_EX + "Le jeu est terminé, le joueur 2 l'emporte",pointsJ2,"à",pointsJ1, Style.RESET_ALL)
else:
    print(Fore.LIGHTBLUE_EX + "Le jeu est terminé, il y a match nul" + Style.RESET_ALL)