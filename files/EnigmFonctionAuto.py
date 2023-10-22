"""
Copyright (c) 2022, UrocyonF
All rights reserved.

This source code is licensed under the BSD-style license found in the
LICENSE file in the root directory of this source tree. 

Author: UrocyonF
Date: 2021 - 2022
"""
# Function to request 3 numbers in a single input (+ input protected as much as possible)
# we enter the input string, the range of the 3 numbers and if they can be similar or no
def fInputTroisNombre(inputstring, inputrange, meme):
    returnlist = []
    inputlist = inputstring.strip('()').replace(',', '').split(" ")
    if len(inputlist) != 3:
        return(False, "Only three numbers (no spaces at the end but between them)")
    for val in inputlist:
        try:
            if int(val) not in range(inputrange[0], inputrange[1]):
                return(False, f'The numbers are not in the correct range ({inputrange[0]} to {inputrange[1]-1})')
            if meme == False:
                if not(int(val) in returnlist):
                    returnlist.append(int(val))
                else:
                    return(False, "A number is entered more than once")
            else:
                returnlist.append(int(val))
        except ValueError:
            return(False, "Numbers are not integers")
    return(True, returnlist)


# Function for displaying rotors according to their offsets
# we give a rotor and its offset and the function returns the rotor once rotated
def fCalculPosRotor(rotor, decalage):
    if decalage < 23:
        return((rotor[decalage-2], rotor[decalage-1], rotor[decalage], rotor[decalage+1], rotor[decalage+2]))
    elif decalage == 24:
        return((rotor[decalage-2], rotor[decalage-1], rotor[decalage], rotor[decalage+1], rotor[0]))
    else:
        return((rotor[decalage-2], rotor[decalage-1], rotor[decalage], rotor[0], rotor[1]))


# Function for displaying 1-digit numbers by putting them as 2-digit numbers
def fEasyAffichNum(num):
    if num < 10:
        return(f'0{num}')
    else:
        return(f'{num}')


# Function that turns a tuple into a dictionary, giving each letter of the alphabet an element of the tuple
def fTupleToDico(Tuple, alphabet):
    rtnDico = {}
    for ind, lettre in enumerate(alphabet):
        rtnDico[lettre] = Tuple[ind]
    return(rtnDico)


# Function that joins characters by 4 in a character string
# ex: "AAAAAA" -> "AAAA AA"
def fPuissanceTexte(texte):
    LrtnTextes = []
    for i in range(0, len(texte)+1, 4):
        if i+4 < len(texte):
            LrtnTextes.append(''.join(texte[i:i+4]))
        else:
            LrtnTextes.append(''.join(texte[i:]))
    return(LrtnTextes)


if __name__ == '__main__':
    pass
