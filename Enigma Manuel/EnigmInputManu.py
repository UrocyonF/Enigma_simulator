from random import randint, sample, choice
from string import ascii_uppercase

import EnigmFonctionManu


# Toutes les tuples utilent pour la suite
RotorI = ('E', 'K', 'M', 'F', 'L', 'G', 'D', 'Q', 'V', 'Z', 'N', 'T', 'O', 'W', 'Y', 'H', 'X', 'U', 'S', 'P', 'A', 'I', 'B', 'R', 'C', 'J')
RotorII = ('A', 'J', 'D', 'K', 'S', 'I', 'R', 'U', 'X', 'B', 'L', 'H', 'W', 'T', 'M', 'C', 'Q', 'G', 'Z', 'N', 'P', 'Y', 'F', 'V', 'O', 'E')
RotorIII = ('B', 'D', 'F', 'H', 'J', 'L', 'C', 'P', 'R', 'T', 'X', 'V', 'Z', 'N', 'Y', 'E', 'I', 'W', 'G', 'A', 'K', 'M', 'U', 'S', 'Q', 'O')
RotorIV = ('E', 'S', 'O', 'V', 'P', 'Z', 'J', 'A', 'Y', 'Q', 'U', 'I', 'R', 'H', 'X', 'L', 'N', 'F', 'T', 'G', 'K', 'D', 'C', 'M', 'W', 'B')
RotorV = ('V', 'Z', 'B', 'R', 'G', 'I', 'T', 'Y', 'U', 'P', 'S', 'D', 'N', 'H', 'L', 'X', 'A', 'W', 'M', 'J', 'Q', 'O', 'F', 'E', 'C', 'K')
RotorVI = ('J', 'P', 'G', 'V', 'O', 'U', 'M', 'F', 'Y', 'Q', 'B', 'E', 'N', 'H', 'Z', 'R', 'D', 'K', 'A', 'S', 'X', 'L', 'I', 'C', 'T', 'W')
RotorVII = ('N', 'Z', 'J', 'H', 'G', 'R', 'C', 'X', 'M', 'Y', 'S', 'W', 'B', 'O', 'U', 'F', 'A', 'I', 'V', 'L', 'P', 'E', 'K', 'Q', 'D', 'T')
RotorVIII = ('F', 'K', 'Q', 'H', 'T', 'L', 'X', 'O', 'C', 'B', 'J', 'S', 'P', 'D', 'Z', 'R', 'A', 'M', 'E', 'W', 'N', 'I', 'U', 'Y', 'G', 'V')
TNomRotor = (RotorI, RotorII, RotorIII, RotorIV, RotorV, RotorVI, RotorVII, RotorVIII)

ReflectorA = ('E', 'J', 'M', 'Z', 'A', 'L', 'Y', 'X', 'V', 'B', 'W', 'F', 'C', 'R', 'Q', 'U', 'O', 'N', 'T', 'S', 'P', 'I', 'K', 'H', 'G', 'D')
ReflectorB = ('Y', 'R', 'U', 'H', 'Q', 'S', 'L', 'D', 'P', 'X', 'N', 'G', 'O', 'K', 'M', 'I', 'E', 'B', 'F', 'Z', 'C', 'W', 'V', 'J', 'A', 'T')
ReflectorC = ('F', 'V', 'P', 'J', 'I', 'A', 'O', 'Y', 'E', 'D', 'R', 'Z', 'X', 'W', 'G', 'C', 'T', 'K', 'U', 'Q', 'S', 'B', 'N', 'M', 'H', 'L')
TNomReflector = (ReflectorA, ReflectorB, ReflectorC)


# Fonction pour entrer les paramètres de connexion à l'avant de la machine
def InputConnexAvant():
    DConnexionAvant, LLettreConnexion = {}, []
    print("\nIl faut lier les connexions avant entre les lettres du clavier")
    autoconnect = EnigmFonctionManu.fVerifInputInt("Connecter automatiquement (1) ou manuellement (0): ", (0, 1))
    nombrecable = EnigmFonctionManu.fVerifInputInt("Combien de cables à connecter (entre 0 et 10): ", range(0, 12))
    if autoconnect == 0:
        for _ in range(nombrecable):
            print("Il faut donner 2 lettres en majuscule à connecter")
            LLettre = EnigmFonctionManu.fInputDeuxLettre("Donner deux lettres différentes en majuscule à la suite: ", ascii_uppercase, LLettreConnexion)
            LLettreConnexion.append(LLettre[0])
            LLettreConnexion.append(LLettre[1])
            DConnexionAvant[LLettre[0]] = LLettre[1]
            DConnexionAvant[LLettre[1]] = LLettre[0]
    else:
        for _ in range(nombrecable):
            lettre1 = choice(ascii_uppercase)
            while lettre1 in LLettreConnexion:
                lettre1 = choice(ascii_uppercase)
            LLettreConnexion.append(lettre1)
            lettre2 = choice(ascii_uppercase)
            while lettre2 in LLettreConnexion:
                lettre2 = choice(ascii_uppercase)
            LLettreConnexion.append(lettre2)
            DConnexionAvant[lettre1] = lettre2
            DConnexionAvant[lettre2] = lettre1
    return(DConnexionAvant)


# Fonctoin pour entrer les rotors qui vont être utilisé
def InputRotor():
    global TNomRotor
    numrotor, LTRotor = [], []
    print("\nIl faut ensuite choisir les 3 rotors à utiliser")
    autoconnect = EnigmFonctionManu.fVerifInputInt("Le faire automatiquement (1) ou manuellement (0): ", (0, 1))
    if autoconnect == 0:
        numrotor = EnigmFonctionManu.fInputTroisNombre("Donner 3 nombres à la suite entre 1 et 8: ", range(1, 9))
    else:
        numrotor = sample(range(1, 9), 3)
    for j in range(3):
        LTRotor.append(TNomRotor[numrotor[j]-1])
    return(LTRotor)


# Fonction pour entrer le décalage innitiale des rotors
def InputDecalageRotor():
    print("\nIl faut enfin donner le décalage des rotors")
    autoconnect = EnigmFonctionManu.fVerifInputInt("Le faire automatiquement (1) ou manuellement (0): ", (0, 1))
    if autoconnect == 0:
        print("Il va falloir donner trois nombre correspondant au décalage du rotor")
        LDecalage = EnigmFonctionManu.fInputTroisNombre("Donner 3 nombres à la suite entre 0 et 25: ", range(26))
    else:
        LDecalage = [randint(0, 25) for _ in range(3)]
    return(LDecalage)


# Fonction pour entrer les rélfecteurs à utilisé
def InputReflecteur():
    global TNomReflector
    print("\nIl faut ensuite choisir le rotor réflecteur")
    autoconnect = EnigmFonctionManu.fVerifInputInt("Le faire automatiquement (1) ou manuellement (0): ", (0, 1))
    if autoconnect == 0:
        numrot = EnigmFonctionManu.fVerifInputInt("Numéro du réflecteur (de 1 à 3): ", (1, 2, 3))
    else:
        numrot = randint(1, 3)
    return(TNomReflector[numrot-1])


# Sert à s'assurer que rien ne se fait si lancé
if __name__ == "__main__":
    pass