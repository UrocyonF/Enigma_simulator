from string import ascii_uppercase, ascii_lowercase
from copy import deepcopy

import EnigmFonctionManu
import EnigmInputManu


# Liste utile pour vérifier et adapter le text entré par l'utilisateur
AccentA = ('á', 'à', 'â', 'ã', 'å', 'A')
AccentO = ('ó', 'ò', 'ô', 'õ', 'ö', 'O')
AccentE = ('é', 'è', 'ê', 'ë', 'E')
AccentI = ('í', 'ì', 'î', 'ï', 'I')
AccentU = ('ú', 'ù', 'û', 'ü', 'U')
AccentC = ('ç', 'C')
AccentY = ('ý', 'Y')
AccentN = ('ñ', 'N')
TAccents = (AccentA, AccentO, AccentE, AccentI, AccentU, AccentC, AccentY, AccentN)


# Définition de la class Rotor et de ses fonctions
class Rotor():
    def __init__(self, rotor={}):
        self.__DRotor = rotor
        self.__nrotation = 0

    def fAffiche(self):
        print(self.__DRotor, self.__nrotation)

    def fModifClass(self, rotor):
        self.__DRotor = rotor
        self.__nrotation = 0

    def fRtnRotor(self, entre):
        return(self.__DRotor[entre])

    def fRtnInvRotor(self, entre):
        for Litem in self.__DRotor.items():
            if Litem[1] == entre:
                return(Litem[0])

    def fTurnRotor(self, number, rota):
        self.__nrotation = rota
        for _ in range(number):
            for let in ascii_uppercase:
                if let == 'A':
                    atemp = self.__DRotor['A']
                    self.__DRotor['A'] = self.__DRotor['Z']
                else:
                    ntemp = self.__DRotor[let]
                    self.__DRotor[let] = atemp
                    atemp = ntemp


# Définition de la classe reliant tous les rotors
class AllRotor():
    def __init__(self, rotors=(), rota=[0, 0, 0]):
        self.__TDRotors = rotors
        self.__Lnrotation = rota

    def fAffiche(self):
        print(self.__TDRotors, self.__Lnrotation)

    def fModifClass(self, rotors, rota):
        self.__TDRotors = rotors
        self.__Lnrotation = rota

    def fUseRotors(self, entre):
        for i in range(3):
            entre = self.__TDRotors[i].fRtnRotor(entre)
        return(entre)

    def fUseInvRotors(self, entre):
        for i in range(2, -1, -1):
            entre = self.__TDRotors[i].fRtnInvRotor(entre)
        return(entre)

    def fRotation(self):
        if self.__Lnrotation[0] == 25:
            self.__TDRotors[0].fTurnRotor(1, 0)
            self.__Lnrotation[0] = 0
            if self.__Lnrotation[1] == 25:
                self.__TDRotors[1].fTurnRotor(1, 0)
                self.__Lnrotation[1] = 0
                if self.__Lnrotation[2] == 25:
                    self.__Lnrotation[2] = 0
                    self.__TDRotors[2].fTurnRotor(1, 0)
                else:
                    self.__Lnrotation[2] = self.__Lnrotation[2]+1
                    self.__TDRotors[2].fTurnRotor(1, self.__Lnrotation[2])
            else:
                self.__Lnrotation[1] = self.__Lnrotation[1]+1
                self.__TDRotors[1].fTurnRotor(1, self.__Lnrotation[1])
        else:
            self.__Lnrotation[0] = self.__Lnrotation[0]+1
            self.__TDRotors[0].fTurnRotor(1, self.__Lnrotation[0])


# Entré des paramètre utilisateur via les fonctions de EnigmInput et adaptation des listes obtenue
def fInputParametre():
    LDRotor, DReflecteur = [], {}
    DCablage = EnigmInputManu.InputConnexAvant()
    LTRotor = EnigmInputManu.InputRotor()
    LDecalageRotor = EnigmInputManu.InputDecalageRotor()
    TReflecteur = EnigmInputManu.InputReflecteur()
    for i in range(3):
        LDRotor.append(EnigmFonctionManu.fTupleToDico(LTRotor[i], ascii_uppercase))
    DReflecteur = EnigmFonctionManu.fTupleToDico(TReflecteur, ascii_uppercase)
    return(DCablage, LDRotor, LDecalageRotor, DReflecteur)


# Entré de la chaine de charactère qui va être crypté
def fInputTexte():
    LTextes = []
    STexte = EnigmFonctionManu.fVerifInputStr("\nDonner le texte sans chiffres: ")
    for caractere in STexte:
        if (caractere in ascii_uppercase) or (caractere in ascii_lowercase):
            LTextes.append(caractere.upper())
        else:
            for acc in TAccents:
                if caractere in acc:
                    LTextes.append(acc[-1])
    return(LTextes)


# Main fonction pour lancement directe
def main():
    # innitialisation
    stop = False
    DCablage, LDRotor, LDecalageRotor, DReflecteur = fInputParametre()
    ##print(DCablage, LDRotor, LDecalageRotor, DReflecteur)##
    CopieLDRotor, CopieLDecalageRotor = deepcopy(LDRotor), deepcopy(LDecalageRotor)
    CRotor1, CRotor2, CRotor3 = Rotor(LDRotor[0]), Rotor(LDRotor[1]), Rotor(LDRotor[2])
    for ind, rot in enumerate((CRotor1, CRotor2, CRotor3)):
        rot.fTurnRotor(LDecalageRotor[ind], LDecalageRotor[ind])
    CRotors = AllRotor((CRotor1, CRotor2, CRotor3), LDecalageRotor)
    # boucle principale
    while stop != True:
        # passage de l'entrée dans la machine
        LinputTextes = fInputTexte()
        LrtnTextes = []
        for l in LinputTextes:
            if l in DCablage:
                l = DCablage[l]
            l = CRotors.fUseRotors(l)
            l = DReflecteur[l]
            l = CRotors.fUseInvRotors(l)
            CRotors.fRotation()
            if l in DCablage:
                l = DCablage[l]
            LrtnTextes.append(l)
        for i in range(0, len(LrtnTextes)+2, 5):
            LrtnTextes.insert(i, ' ')
        print('Le texte en sorti est:'+''.join(LrtnTextes))
        # poursuite ou non de la boucle
        continu = EnigmFonctionManu.fVerifInputInt("\nContinuer (0), remettre le paramétrage initiale (1) ou arrêter (2): ", (0, 1, 2))
        if continu == 1:
            LDRotor, LDecalageRotor = deepcopy(CopieLDRotor), deepcopy(CopieLDecalageRotor)
            for ind, rot in enumerate((CRotor1, CRotor2, CRotor3)):
                rot.fModifClass(LDRotor[ind])
                rot.fTurnRotor(LDecalageRotor[ind], LDecalageRotor[ind])
            CRotors.fModifClass((CRotor1, CRotor2, CRotor3), LDecalageRotor)
        elif continu == 2:
            break
    print("\nMerci de votre utilisation")


# Lancer la fonction main si le programme est lancé directement
if __name__ == '__main__':
    main()