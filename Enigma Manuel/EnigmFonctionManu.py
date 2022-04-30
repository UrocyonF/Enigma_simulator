
# Permet de vérfier si un input est bien un entier et répond à une condition
def fVerifInputInt(strdemande, condition):
    rtndemande, conditionOK = 0, False
    while conditionOK == False:
        try:
            rtndemande = int(input(strdemande))
            if rtndemande in condition:
                conditionOK = True
        except ValueError:
            print("Il faut donner un entier")
    return(rtndemande)


# Permet de vérfier si un input est bien une chaine de characteres
def fVerifInputStr(strdemande):
    rtndemande, conditionOK = 0, False
    while conditionOK == False:
        try:
            rtndemande = str(input(strdemande))
            conditionOK = True
        except ValueError:
            print("Il faut donner une chaine de caractère")
    return(rtndemande)


# Permet de demander 3 nombre en un seul input (+saisi protégé)
def fInputTroisNombre(strdemande, range):
    numberOK=0
    while numberOK != 3:
        inputstring = str(input(strdemande))
        numberOK, notOK, returnlist = 0, False, []
        inputlist = inputstring.split(" ")
        if len(inputlist) == 3:
            for val in inputlist:
                try:
                    if (int(val) in range) and (not (int(val) in returnlist)):
                        returnlist.append(int(val))
                        numberOK += 1
                    else:
                        notOK = True
                except ValueError:
                    notOK = True
        else:
            notOK = True
        if notOK == True:
            print("Seulement trois nombre avec un espace entre eux")
    return(returnlist)


# Permet de demander 2 lettres en un seul input (+saisi protégé)
def fInputDeuxLettre(strdemande, alphabet, previouslettre):
    numberOK=0
    while numberOK != 2:
        inputstring = fVerifInputStr(strdemande)
        numberOK, notOK = 0, False
        inputlist = inputstring.split(" ")
        if len(inputlist) == 2:
            for ind, val in enumerate(inputlist):
                if (val in alphabet) and (not val in previouslettre) and (val != inputlist[ind-1]):
                    numberOK += 1
                else:
                    notOK = True
        else:
            notOK = True
        if notOK == True:
            print("Seulement deux lettres en majuscule avec un espace entre elles")
    return(inputlist)


# Transforme un tuple et un dicotionaire donnant à chaque lettre de l'alphabet un élément du tuple
def fTupleToDico(Tuple, alphabet):
    rtnDico = {}
    for ind, lettre in enumerate(alphabet):
        rtnDico[lettre] = Tuple[ind]
    return(rtnDico)
