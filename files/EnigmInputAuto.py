"""
Copyright (c) 2023, UrocyonF
All rights reserved.

This source code is licensed under the BSD-style license found in the
LICENSE file in the root directory of this source tree. 

Author: UrocyonF
Date: 2021 - 2022
"""

from random import randint, sample, choice
from string import ascii_uppercase
from ast import literal_eval
from pyzbar import pyzbar
from PIL import Image

import qrcode

import files.EnigmFonctionAuto as EnigmFonctionAuto


# All tuples to choose from (all 8 rotors and 3 reflectors available)
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

# Definition for the creation of the QRcode (with an acceptable loss rate of 25%)
# with an acceptable loss rate of 25% and a classic display
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_Q,
    box_size=10,
    border=1,
)


# Function to verify the connection parameters entry at the front of the machine (input verification)
def InputConnexAvant(SCablage):
    LLettreConnexion = []
    try:
        DCablage = literal_eval(SCablage)
        if type(DCablage) != dict:
            return(False, "The wiring is not in the correct format (dictionary requested)")
        elif len(DCablage.keys()) > 24:
            return(False, "The dictionary must contain at most 12 pairs")
        for key, value in DCablage.items():
            if not(key in ascii_uppercase) or not(value in ascii_uppercase):
                return(False, "Letters must be capitals")
            elif key == value:
                return(False, "The two letters cannot be the same")
            elif DCablage[value] != key:
                return(False, "Letter " + key + " is connected to the letter " + value + " but not vice versa")
            elif (key, value) in LLettreConnexion:
                return(False, "Letter " + key + " or " + value + " is used multiple times")
            LLettreConnexion.append((key, value))
        return(True, DCablage)
    except:
        return(False, "The wiring is not in the correct format (dictionary requested)")


# Function for the input of the rotors that are going to be used (input check)
# we give a string to check to have 3 numbers between 1 and 9 (rotor number)
def InputRotor(STRotor):
    verif, retour = EnigmFonctionAuto.fInputTroisNombre(STRotor, (1, 10), False)
    if verif:
        return(verif, subTransfoInputRotor(retour), retour)
    return(verif, retour, "")


# Function for entering the initial offset of the rotors (input check)
# we give a string to check to have 3 numbers between 0 and 26 (initial offset of the rotors)
def InputDecalageRotor(SDecalageRotor):
    verif, retour = EnigmFonctionAuto.fInputTroisNombre(SDecalageRotor, (0, 26), True)
    return(verif, retour)


# Function for input of reflectors to be used (input check)
def InputReflecteur(SReflecteur):
    global TNomReflector
    verif = False
    try:
        retour = literal_eval(SReflecteur)
        if type(retour) == int:
            if retour in range(1, 4):
                verif = True
            else:
                retour = "The number must be between 1 and 3"
        else:
            retour = "The number is not in the correct format (integer requested)"
    except:
        retour = "The input is not in the correct format"
    if verif:
        return(verif, TNomReflector[retour-1], retour)
    return(verif, retour, "")


# Function to create the front connections (plugboard) randomly
# we will return a dictionary where each one will be linked to anothe
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


# Function to choose 3 rotors randomly
# we will return 3 digits where each can only appear once
def subInputRotor():
    numrotor = []
    numrotor = sample(range(1, 9), 3)
    return(numrotor)

# Function to put the rotors in the right format (int -> tuple)
def subTransfoInputRotor(numrotor):
    global TNomRotor
    LTRotor = []
    for j in range(3):
        LTRotor.append(TNomRotor[int(numrotor[j])-1])
    return(LTRotor)


# Function to choose 3 random rotor offsets
# we will return 3 numbers (between 0 and 25) which can appear several times
def subInputDecalageRotor():
    LDecalage = [randint(0, 25) for _ in range(3)]
    return(LDecalage)


# Function to choose 1 reflector randomly
# we will return 1 digit (between 0 and 3)
def subInputReflecteur():
    numrot = randint(1, 3)
    return(numrot)

# Function to put reflectors in the correct format (int -> tuple)
def subTransfoInputReflecteur(numrot):
    global TNomReflector
    return(TNomReflector[int(numrot)-1])


# Function for creating a QRcode in auto
# we give the data and the name of the image that will be created
def DataToQRcode(data,name):
    try:
        qr.clear()
        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        img.save(f'QRcode/{name}.png')
        return("Recording completed", True)
    except:
        return("An error has occurred", False)


# Function for reading a QRcode in car
def QRcodeToData(file):
    try:
        image = Image.open(file)
        qr_code = pyzbar.decode(image)[0]
        data= qr_code.data.decode("utf-8")
        return("Reading successful", data)
    except:
        return("An error has occurred", False)


if __name__ == "__main__":
    pass