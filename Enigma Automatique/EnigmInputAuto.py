from random import randint, sample, choice
from string import ascii_uppercase
from ast import literal_eval

import EnigmFonctionAuto


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


# Fonction pour vérifier l'entrée des paramètres de connexion à l'avant de la machine (vérification des entrées)
def InputConnexAvant(SCablage):
    LLettreConnexion = []
    try:
        DCablage = literal_eval(SCablage)
        if type(DCablage) != dict:
            return(False, "Le câblage n'est pas au bon format (dictionaire demandé)")
        elif len(DCablage.keys()) > 24:
            return(False, "Le dictionnaire doit contenir au plus 12 couples")
        for key, value in DCablage.items():
            if not(key in ascii_uppercase) or not(value in ascii_uppercase):
                return(False, "Les lettres doivent être des majuscules")
            elif key == value:
                return(False, "Les deux lettres ne peuvent pas être identiques")
            elif DCablage[value] != key:
                return(False, "La lettre " + key + " est connectée à la lettre " + value + " mais pas à l'inverse")
            elif (key, value) in LLettreConnexion:
                return(False, "La lettre " + key + " ou " + value + " est utilisée plusieurs fois")
            LLettreConnexion.append((key, value))
        return(True, DCablage)
    except:
        return(False, "Le câblage n'est pas au bon format (dictionaire demandé)")


# Fonction pour l'entrée des rotors qui vont être utilisé (vérification des entrées)
def InputRotor(STRotor):
    verif, retour = EnigmFonctionAuto.fInputTroisNombre(STRotor, (1, 10), False)
    if verif == True:
        return(verif, subTransfoInputRotor(retour), retour)
    return(verif, retour, "")


# Fonction pour l'entrée du décalage innitiale des rotors (vérification des entrées)
def InputDecalageRotor(SDecalageRotor):
    verif, retour = EnigmFonctionAuto.fInputTroisNombre(SDecalageRotor, (0, 26), True)
    return(verif, retour)


# Fonction pour l'entrée des rélfecteurs à utilisé (vérification des entrées)
def InputReflecteur(SReflecteur):
    global TNomReflector
    verif = False
    try:
        retour = literal_eval(SReflecteur)
        if type(retour) == int:
            if retour in range(1, 4):
                verif = True
            else:
                verif, retour = False, "Le nombre doit être compris entre 1 et 3"
        else:
            verif, retour = False, "Le nombre n'est pas au bon format (entier demandé)"
    except:
        verif, retour = False, "L'entrée n'est pas au bon format"
    if verif == True:
        return(verif, TNomReflector[retour-1], retour)
    return(verif, retour, "")


# Fonction pour entrer les rotors qui vont être utilisés en automatisé
def subInputConnexAvant(LettreAlphabet):
    DConnexionAvant, LLettreConnexion = {}, []
    for _ in range(randint(0, 12)):
        lettre1 = choice(LettreAlphabet)
        while lettre1 in LLettreConnexion:
            lettre1 = choice(LettreAlphabet)
        LLettreConnexion.append(lettre1)
        lettre2 = choice(LettreAlphabet)
        while lettre2 in LLettreConnexion:
            lettre2 = choice(LettreAlphabet)
        LLettreConnexion.append(lettre2)
        DConnexionAvant[lettre1] = lettre2
        DConnexionAvant[lettre2] = lettre1
    return(DConnexionAvant)


# Fonction pour entrer les rotors qui vont être utilisés en automatisé
def subInputRotor():
    numrotor = []
    numrotor = sample(range(1, 9), 3)
    return(numrotor)

# Foncition pour mettre sous le bon format les rotors(num -> tuple) #
def subTransfoInputRotor(numrotor):
    global TNomRotor
    LTRotor = []
    for j in range(3):
        LTRotor.append(TNomRotor[int(numrotor[j])-1])
    return(LTRotor)


# Fonction pour entrer le décalage innitiale des rotors automatisé
def subInputDecalageRotor():
    LDecalage = [randint(0, 25) for _ in range(3)]
    return(LDecalage)


# Fonction pour entrer les rélfecteurs à utilisé en automatisé
def subInputReflecteur():
    numrot = randint(1, 3)
    return(numrot)

# Fonction pour mettre sous le bon format les rélfecteurs (num -> tuple) #
def subTransfoInputReflecteur(numrot):
    global TNomReflector
    return(TNomReflector[int(numrot)-1])


# Sert à rien
if __name__ == "__main__":
    pass
