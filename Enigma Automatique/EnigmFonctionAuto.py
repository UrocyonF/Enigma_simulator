
# Fonction pour demander 3 nombres en un seul input (+ saisi protégé)
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
def fCalculPosRotor(rotor, decalage):
    if decalage < 23:
        return(rotor[decalage-2], rotor[decalage-1], rotor[decalage], rotor[decalage+1], rotor[decalage+2])
    elif decalage == 24:
        return(rotor[decalage-2], rotor[decalage-1], rotor[decalage], rotor[decalage+1], rotor[0])
    else:
        return(rotor[decalage-2], rotor[decalage-1], rotor[decalage], rotor[0], rotor[1])


# Fonction pour l'affichage des nombre à 1 chiffre en nombre à 2 chiffres
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


# Sert à rien
if __name__ == '__main__':
    pass
