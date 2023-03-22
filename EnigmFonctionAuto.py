"""
Copyright (c) 2023, UrocyonF
All rights reserved.

This source code is licensed under the BSD-style license found in the
LICENSE file in the root directory of this source tree. 

Author: UrocyonF
Date: 2021 - 2022
"""

# Fonction pour demander 3 nombres en un seul input (+ saisi protégé au maximum)
#on entre le string d'input, la range des 3 nombres et si ils peuvent similaire ou non
def fInputTroisNombre(inputstring, inputrange, meme):
    returnlist = []
    inputlist = inputstring.strip('()').replace(',', '').split(" ")
    if len(inputlist) != 3:
        return(False, "Seulement trois nombres (sans espace à la fin mais entre eux)")
    for val in inputlist:
        try:
            if int(val) not in range(inputrange[0], inputrange[1]):
                return(False, f'Les nombres ne sont pas dans le bon intervalle ({inputrange[0]} à {inputrange[1]-1})')
            if meme == False:
                if not(int(val) in returnlist):
                    returnlist.append(int(val))
                else:
                    return(False, "Un nombre est saisi plusieurs fois")
            else:
                returnlist.append(int(val))
        except ValueError:
            return(False, "Les nombres ne sont pas des entiers")
    return(True, returnlist)


# Fonction pour l'affichage des rotors selon leurs décalages
#on donne un rotor et le décalage de celui-ci et la fonction nous retourne le rotor un fois tourné
def fCalculPosRotor(rotor, decalage):
    if decalage < 23:
        return(rotor[decalage-2], rotor[decalage-1], rotor[decalage], rotor[decalage+1], rotor[decalage+2])
    elif decalage == 24:
        return(rotor[decalage-2], rotor[decalage-1], rotor[decalage], rotor[decalage+1], rotor[0])
    else:
        return(rotor[decalage-2], rotor[decalage-1], rotor[decalage], rotor[0], rotor[1])


# Fonction pour l'affichage des nombre à 1 chiffre en les mettant sous forme de nombre à 2 chiffres
def fEasyAffichNum(num):
    if num < 10:
        return(f'0{num}')
    else:
        return(f'{num}')


# Fonction qui transforme un tuple en un dicotionaire, en donnant à chaque lettre de l'alphabet un élément du tuple
def fTupleToDico(Tuple, alphabet):
    rtnDico = {}
    for ind, lettre in enumerate(alphabet):
        rtnDico[lettre] = Tuple[ind]
    return(rtnDico)


# Fonction qui réunie des charactère par 4 dans une chaine de charactère
#ex: "AAAAAA" -> "AAAA AA"
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
