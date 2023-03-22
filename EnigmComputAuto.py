"""
Copyright (c) 2023, UrocyonF
All rights reserved.

This source code is licensed under the BSD-style license found in the
LICENSE file in the root directory of this source tree. 

Author: UrocyonF
Date: 2021 - 2022
"""

from string import ascii_uppercase, ascii_lowercase

import EnigmFonctionAuto


# Liste utilent pour vérifier et adapter le texte entré par l'utilisateur
#pour enlever les accents dans le texte d'input
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

    def fRtnRotor(self, entre):
        return(self.__DRotor[entre])

    def fRtnInvRotor(self, entre):
        for Litem in self.__DRotor.items():
            if Litem[1] == entre:
                return(Litem[0])

    # Fonction pour faire tourner le rotor un nobre "number" de foix
    def fTurnRotor(self, number):
        for _ in range(number):
            for let in ascii_uppercase:
                if let == 'A':
                    atemp = self.__DRotor['A']
                    self.__DRotor['A'] = self.__DRotor['Z']
                else:
                    ntemp = self.__DRotor[let]
                    self.__DRotor[let] = atemp
                    atemp = ntemp


# Définition de la classe liant tous les rotors
class AllRotor():
    def __init__(self, rotors=(), rota=[0, 0, 0]):
        self.__TDRotors = rotors
        self.__Lnrotation = rota

    # Fonction qui nous retourne la lettre correspondant à une entrée pour un rotor et le fait tourner
    def fUseRotors(self, entre):
        for i in range(3):
            entre = self.__TDRotors[i].fRtnRotor(entre)
        return(entre)

    # Fonction qui nous retourne la lettre correspondant à une sortie pour un rotor et le fait tourner
    #fait la même chose que la fonction précédante mais à l'inverse (en partant des sorties)
    def fUseInvRotors(self, entre):
        for i in range(2, -1, -1):
            entre = self.__TDRotors[i].fRtnInvRotor(entre)
        return(entre)

    # Fonction pour faire tourner les rotors
    #fait tourner le premier rotor jusqu'à ce qu'il est fait un tour et fait alors tourner le suivant, ect...
    def fRotation(self):
        if self.__Lnrotation[0] == 25:
            self.__TDRotors[0].fTurnRotor(1)
            self.__Lnrotation[0] = 0
            if self.__Lnrotation[1] == 25:
                self.__TDRotors[1].fTurnRotor(1)
                self.__Lnrotation[1] = 0
                if self.__Lnrotation[2] == 25:
                    self.__Lnrotation[2] = 0
                    self.__TDRotors[2].fTurnRotor(1)
                else:
                    self.__Lnrotation[2] = self.__Lnrotation[2]+1
                    self.__TDRotors[2].fTurnRotor(1)
            else:
                self.__Lnrotation[1] = self.__Lnrotation[1]+1
                self.__TDRotors[1].fTurnRotor(1)
        else:
            self.__Lnrotation[0] = self.__Lnrotation[0]+1
            self.__TDRotors[0].fTurnRotor(1)


# Entré de la chaine de charactère qui va être crypté
#met le string sous le bon format (minuscule -> majuscule, accent -> pas accent, pas d'autre caractère)
def fInputTexte(STexte):
    LTextes = []
    for caractere in STexte:
        if (caractere in ascii_uppercase) or (caractere in ascii_lowercase):
            LTextes.append(caractere.upper())
        else:
            for acc in TAccents:
                if caractere in acc:
                    LTextes.append(acc[-1])
    return(LTextes)


# Fonction pour mettre les variables au bon format (liste -> dictionnaire) avec des lettres en majuscule
#sert à la création des rotors
def fsubInputRealParametre(LTRotor, TReflecteur):
    LDRotor, DReflecteur = [], {}
    for i in range(3):
        LDRotor.append(EnigmFonctionAuto.fTupleToDico(LTRotor[i], ascii_uppercase))
    DReflecteur = EnigmFonctionAuto.fTupleToDico(TReflecteur, ascii_uppercase)
    return(LDRotor, DReflecteur)


# main fonction qui fait tout l'encryption
#on donne les paramètres (les et dico des rotors, connexion...) et le texte à encrypter
#fait appel aux fonction et class du dessus et renvoie alors le texte en sortie de la machine (en string)
def main(DCablage, LDRotor, LDecalageRotor, DReflecteur, LinputTextes):
    CRotor1, CRotor2, CRotor3 = Rotor(
        LDRotor[0]), Rotor(LDRotor[1]), Rotor(LDRotor[2])
    for ind, rot in enumerate((CRotor1, CRotor2, CRotor3)):
        rot.fTurnRotor(LDecalageRotor[ind])
    CRotors = AllRotor((CRotor1, CRotor2, CRotor3), LDecalageRotor)
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
    texte = ''.join(LrtnTextes)
    return(' '.join(EnigmFonctionAuto.fPuissanceTexte(texte)))


if __name__ == '__main__':
    pass
