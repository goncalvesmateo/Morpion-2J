#######################
## Morpion 2 joueurs ##
##     Par M26G      ##
#######################
# GitHub : @goncalvesmateo

# Booléens qui désigneront le joueur gagnant
J1win = False
J2win = False

# Entier qui comptera le nombre de cases vides
casesLibres = 9

# Booléen qui verifiera si la case saisi est valide (si elle est libre et qu'elle existe)
caseValide = False

# Croix des joueurs (définis initialement avec 0 caractère)
J1perso = ""
J2perso = ""

# Tableau du plateau de jeu (servira pour l'affichage des carcatères
Morpion = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

# Affiche le plateau de jeu ainsi que l'aide sur le choix de la case
def plateau():
    print("Jeu du morpion 2 joueurs")													# Nom du jeu
    print("J1 : ",J1perso," | J2 : ",J2perso," | Encore",casesLibres,"cases libres")	# Affichage des caractères choisis et du nombre de cases libres
    print()																				# Espace pour l'esthétique
    print(Morpion[6],"|",Morpion[7],"|",Morpion[8]," | ",7,"|",8,"|",9)					# Ligne supérieure
    print("--+---+--  |  --+---+--")													# Délimitation des cases
    print(Morpion[3],"|",Morpion[4],"|",Morpion[5]," | ",4,"|",5,"|",6)					# Ligne centrale
    print("--+---+--  |  --+---+--")													# Délimitation des cases
    print(Morpion[0],"|",Morpion[1],"|",Morpion[2]," | ",1,"|",2,"|",3)					# Ligne inférieure
    print()																				# Espace pour l'esthétique

# Vérifie si le jeu est gagné par un des deux joueurs ou s'il y a égalité
def winVerify(x):
    # Définit toutes les conditions de victoire (une ligne verticale, horizontale ou diagonale)
    y = ((Morpion[0] == x and Morpion[1] == x and Morpion[2] == x) or (Morpion[3] == x and Morpion[4] == x and Morpion[5] == x) or (Morpion[6] == x and Morpion[7] == x and Morpion[8] == x) or (Morpion[0] == x and Morpion[3] == x and Morpion[6] == x) or (Morpion[1] == x and Morpion[4] == x and Morpion[7] == x) or (Morpion[2] == x and Morpion[5] == x and Morpion[8] == x) or (Morpion[0] == x and Morpion[4] == x and Morpion[8] == x) or (Morpion[2] == x and Morpion[4] == x and Morpion[6] == x))
    return (y)

# Utilise une case libre
def case(x):
    if x > 9 or x < 1:
        x = 5
    return (x)

# Les deux joueurs choisisssent un seul caractère qui fera office de choix et de rond
while len(J1perso) != 1:
    J1perso = input("J1 - Choisissez un caractère : ")
    if len(J1perso) != 1:
        print("Un seul caractère svp")
print()

while len(J2perso) != 1:
    J2perso = input("J2 - Choisissez un caractère : ")
    if len(J2perso) != 1:
        print("Un seul caractère svp")
    # Le joueur 2 ne doit pas choisir le même caractère que le joueur 1
    if J2perso == J1perso:
        print("Caractère déja utilisé")
        J2perso = ""
print()

# Tant que les deux joueurs n'ont pas gagné
while J1win == False and J2win == False:
    
    # Choix de la case pour le joueur 1
    caseValide = False
    if J2win == False or casesLibres > 0:
        plateau()
        J1tour = int(input("J1 - Choisir une case libre : "))
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
                J1tour = int(input("J1 - Entrée invalide, choisir une case libre : "))
                
    # Le jeu s'arrète si toutes les cases sont utilisées ou si le joueur 1 a gagné
    if casesLibres == 0 or J1win == True:
        break

    # Choix de la case pour le joueur 2
    caseValide = False
    if J1win == False or casesLibres > 0:
        plateau()
        J2tour = int(input("J2 - Choisir une case libre : "))
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
                J2tour = int(input("J2 - Entrée invalide, choisir une case libre : "))
    
    # Le jeu s'arrète si toutes les cases sont utilisées ou si le joueur 2 a gagné
    if casesLibres == 0 or J2win == True:
        break

# Affiche un message de victoire ou d'égalité
if J1win == True:
    plateau()
    print("Joueur 1 à gagné.")
elif J2win == True:
    plateau()
    print("Joueur 2 à gagné.")
else:
    plateau()
    print("Égalité")