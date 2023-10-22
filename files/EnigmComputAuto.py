"""
Copyright (c) 2022, UrocyonF
All rights reserved.

This source code is licensed under the BSD-style license found in the
LICENSE file in the root directory of this source tree. 

Author: UrocyonF
Date: 2021 - 2022
"""
from string import ascii_uppercase, ascii_lowercase

import files.EnigmFonctionAuto as EnigmFonctionAuto


# List useful to check and adapt the text entered by the user
# to remove accents in input text
AccentA = ('á', 'à', 'â', 'ã', 'å', 'A')
AccentO = ('ó', 'ò', 'ô', 'õ', 'ö', 'O')
AccentE = ('é', 'è', 'ê', 'ë', 'E')
AccentI = ('í', 'ì', 'î', 'ï', 'I')
AccentU = ('ú', 'ù', 'û', 'ü', 'U')
AccentC = ('ç', 'C')
AccentY = ('ý', 'Y')
AccentN = ('ñ', 'N')
TAccents = (AccentA, AccentO, AccentE, AccentI, AccentU, AccentC, AccentY, AccentN)


# Definition of the Rotor class and its functions
class Rotor():
    def __init__(self, rotor={}):
        self.__DRotor = rotor

    def fRtnRotor(self, entre):
        return(self.__DRotor[entre])

    def fRtnInvRotor(self, entre):
        for Litem in self.__DRotor.items():
            if Litem[1] == entre:
                return(Litem[0])

    # Function to spin the rotor a "number" of times
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


# Definition of the class binding all the rotors
class AllRotor():
    def __init__(self, rotors=(), rota=[0, 0, 0]):
        self.__TDRotors = rotors
        self.__Lnrotation = rota

    # Function that returns the letter corresponding to an input for a rotor and makes it rotate
    def fUseRotors(self, entre):
        for i in range(3):
            entre = self.__TDRotors[i].fRtnRotor(entre)
        return(entre)

    # Function that returns the letter corresponding to an output for a rotor and makes it rotate
    # does the same thing as the previous function but in reverse (starting from the outputs)
    def fUseInvRotors(self, entre):
        for i in range(2, -1, -1):
            entre = self.__TDRotors[i].fRtnInvRotor(entre)
        return(entre)

    # Function to spin the rotors
    # spin the first rotor until it's done one turn and then spin the next one...
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


# Enter the character string that will be encrypted
# put the string in the correct format (lowercase -> uppercase, accent -> no accent, no other characters)
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


# Function to put variables in the correct format (list -> dictionary) with uppercase letters
# is used to create rotors
def fsubInputRealParametre(LTRotor, TReflecteur):
    LDRotor, DReflecteur = [], {}
    for i in range(3):
        LDRotor.append(EnigmFonctionAuto.fTupleToDico(LTRotor[i], ascii_uppercase))
    DReflecteur = EnigmFonctionAuto.fTupleToDico(TReflecteur, ascii_uppercase)
    return(LDRotor, DReflecteur)


# Main function that does all the encryption
# we give the parameters (the and dictionary of the rotors, connection...) and the text to encrypt
# calls the function and class above and then returns the text output from the machine (in string)
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
