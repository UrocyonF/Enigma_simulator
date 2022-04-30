import random


LettreAlphabet=('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')

RotorI=((1, 2), (2, 4), (3, 6), (4, 8), (5, 10), (6, 12), (7, 3), (8, 16), (9, 18), (10, 20), (11, 24), (12, 22), (13, 26), (14, 14), (15, 25), (16, 5), (17, 9), (18, 23), (19, 7), (20, 1), (21, 11), (22, 13), (23, 21), (24, 19), (25, 17), (26, 15))
RotorII=((1, 2), (2, 4), (3, 6), (4, 8), (5, 10), (6, 12), (7, 3), (8, 16), (9, 18), (10, 20), (11, 24), (12, 22), (13, 26), (14, 14), (15, 25), (16, 5), (17, 9), (18, 23), (19, 7), (20, 1), (21, 11), (22, 13), (23, 21), (24, 19), (25, 17), (26, 15))
RotorIII=((1, 2), (2, 4), (3, 6), (4, 8), (5, 10), (6, 12), (7, 3), (8, 16), (9, 18), (10, 20), (11, 24), (12, 22), (13, 26), (14, 14), (15, 25), (16, 5), (17, 9), (18, 23), (19, 7), (20, 1), (21, 11), (22, 13), (23, 21), (24, 19), (25, 17), (26, 15))
RotorIV=((1, 5), (2, 19), (3, 15), (4, 22), (5, 16), (6, 26), (7, 10), (8, 1), (9, 25), (10, 17), (11, 21), (12, 9), (13, 18), (14, 8), (15, 24), (16, 12), (17, 14), (18, 6), (19, 20), (20, 7), (21, 11), (22, 4), (23, 3), (24, 13), (25, 23), (26, 2))
RotorV=((1, 10), (2, 16), (3, 7), (4, 22), (5, 15), (6, 21), (7, 13), (8, 6), (9, 25), (10, 17), (11, 2), (12, 5), (13, 14), (14, 8), (15, 26), (16, 18), (17, 4), (18, 11), (19, 1), (20, 19), (21, 24), (22, 12), (23, 9), (24, 3), (25, 20), (26, 23))
RotorVI=((1, 10), (2, 16), (3, 7), (4, 22), (5, 15), (6, 21), (7, 13), (8, 6), (9, 25), (10, 17), (11, 2), (12, 5), (13, 14), (14, 8), (15, 26), (16, 18), (17, 4), (18, 11), (19, 1), (20, 19), (21, 24), (22, 12), (23, 9), (24, 3), (25, 20), (26, 23))
RotorVII=((1, 14), (2, 26), (3, 10), (4, 8), (5, 7), (6, 18), (7, 3), (8, 24), (9, 13), (10, 25), (11, 19), (12, 23), (13, 2), (14, 15), (15, 21), (16, 6), (17, 1), (18, 9), (19, 22), (20, 12), (21, 16), (22, 5), (23, 11), (24, 17), (25, 4), (26, 20))
RotorVIII=((1, 6), (2, 11), (3, 17), (4, 8), (5, 20), (6, 12), (7, 24), (8, 15), (9, 3), (10, 2), (11, 10), (12, 19), (13, 16), (14, 4), (15, 26), (16, 18), (17, 1), (18, 13), (19, 5), (20, 23), (21, 14), (22, 9), (23, 21), (24, 25), (25, 7), (26, 22))

ReflectorA=(('a', 'e'), ('b', 'j'), ('c', 'm'), ('d', 'z'), ('f', 'l'), ('g', 'y'), ('h', 'x'), ('i', 'v'), ('k', 'w'), ('n', 'r'), ('o', 'q'), ('p', 'u'), ('s', 't'))
ReflectorB=(('a', 'y'), ('b', 'r'), ('c', 'u'), ('d', 'h'), ('e', 'q'), ('f', 's'), ('g', 'l'), ('i', 'p'), ('j', 'x'), ('k', 'n'), ('m', 'o'), ('t', 'z'), ('v', 'w'))
ReflectorC=(('a', 'f'), ('b', 'v'), ('c', 'p'), ('d', 'j'), ('e', 'i'), ('g', 'o'), ('h', 'y'), ('k', 'r'), ('l', 'z'), ('m', 'x'), ('n', 'w'), ('q', 't'), ('u', 's'))


NumLettreAlphabet=[]

for e in range(0,len(LettreAlphabet)):
    NumLettreAlphabet.append(e+1)
    

def InputConnextAvant():
    global LettreAlphabet,NumLettreAlphabet
    ListeConnexionAvant=[]
    LettreConnexionA=[]
    LettreConnexionB=[]
    print("Il faut lier les connexions avant entre les lettres du clavier")
    AutoConnect=int(input("Le faire automatiquement (1) ou manuellement (0): "))
    while not (AutoConnect==1 or AutoConnect==0):
        print("Il faut choisir (1 ou 0)")
        AutoConnect=int(input("Connecter automatiquement (1) ou manuellement (0): "))
    NombreCable=int(input("Combien de cables à connecter (entre 1 et 10): "))
    while (NombreCable<1) or (NombreCable>10):
        print("Il faut choisir (de 1 à 10)")
        NombreCable=int(input("Combien de cables à connecter (entre 1 et 10): "))
    if AutoConnect==0:
        for f in range (0,NombreCable):
            print("Donner 2 lettres à connecter (mettre '-' arreter de connecter)")
            LettreA=str(input("Première lettre: "))
            if LettreA == '-':
                break
            while (not (LettreA in LettreAlphabet)) or (LettreA in LettreConnexionA):
                LettreA=str(input("Il faut donner une simple première lettre de l'alphabet qui n'est pas déjà lié: "))
            LettreB=str(input("Deuxième lettre: "))
            while (not (LettreB in LettreAlphabet)) or (LettreB in LettreConnexionB) or (LettreB==LettreA):
                LettreB=str(input("Il faut donner une simple deuxième lettre de l'alphabet qui n'est pas déjà lié: "))
            LettreConnexionA.append(LettreA)
            LettreConnexionA.append(LettreB)
            LettreConnexionB.append(LettreA)
            LettreConnexionB.append(LettreB)
            ListeConnexionAvant.append([LettreA,LettreB])
    else:
        for g in range (0,NombreCable):
            LettreA=random.choice(LettreAlphabet)
            while LettreA in LettreConnexionA:
                LettreA=random.choice(LettreAlphabet)
            LettreB=random.choice(LettreAlphabet)
            while (LettreB in LettreConnexionB) or (LettreB==LettreA):
                LettreB=random.choice(LettreAlphabet)
            LettreConnexionA.append(LettreA)
            LettreConnexionA.append(LettreB)
            LettreConnexionB.append(LettreA)
            LettreConnexionB.append(LettreB)
            ListeConnexionAvant.append([LettreA,LettreB])
    return(ListeConnexionAvant)


def InputRotor():
    global RotorI,RotorII,RotorIII,RotorIV,RotorV,RotorVI,RotorVII,RotorVIII
    NumRotor=[]
    ListeRotor=[]
    AutoConnect=42
    print("Il faut ensuite choisir les 3 rotors à utiliser")
    AutoConnect=int(input("Le faire automatiquement (1) ou manuellement (0): "))
    while not (AutoConnect==1 or AutoConnect==0):
        print("Il faut choisir (1 ou 0)")
        AutoConnect=int(input("Choix automatiquement (1) ou manuellement (0): "))
    if AutoConnect==0:   
        for h in range (0,3):
            Num=int(input("Donner le numéro du rotor (de 1 à 8): "))
            while Num in NumRotor:
                Num=int(input("Donner un numéro de rotor pas déjà utilisé(de 1 à 8): "))
            NumRotor.append(Num)
    else:
        for i in range (0,3):
            Num=random.randint(1,8)
            while Num in NumRotor:
                Num=random.randint(1,8)
            NumRotor.append(Num)
    for j in range (0,3):
        if NumRotor[j]==1:
            ListeRotor.append(list(RotorI))
        elif NumRotor[j]==2:
            ListeRotor.append(list(RotorII))
        elif NumRotor[j]==3:
            ListeRotor.append(list(RotorIII))
        elif NumRotor[j]==4:
            ListeRotor.append(list(RotorIV))
        elif NumRotor[j]==5:
            ListeRotor.append(list(RotorV))
        elif NumRotor[j]==6:
            ListeRotor.append(list(RotorVI))
        elif NumRotor[j]==7:
            ListeRotor.append(list(RotorVII))
        else:
            ListeRotor.append(list(RotorVIII))
    return(ListeRotor)

#les rotors sont des listes de tuple y faut en faire des list de list avant de les renvoyer

def InputReflecteur():
    global ReflectorA,ReflectorB,ReflectorC
    ListeConnexionRetour=[]
    AutoConnect=42
    print("Il faut ensuite choisir le rotor réflecteur")
    AutoConnect=int(input("Le faire automatiquement (1) ou manuellement (0): "))
    while not (AutoConnect==1 or AutoConnect==0):
        print("Il faut choisir (1 ou 0)")
        AutoConnect=int(input("Choix automatiquement (1) ou manuellement (0): "))
    if AutoConnect==0:
        NumRot=int(input("Numéro du réflecteur (de 1 à 3): "))
        while not (NumRot in [1,2,3]):
            NumRot=int(input("Il faut choisir le numéro du rotor (de 1 à 3): "))
    else:
        NumRot=random.randint(1,3)
    if NumRot==1:
        ListeConnexionRetour=ReflectorA
    elif NumRot==2:
        ListeConnexionRetour=ReflectorB
    else:
        ListeConnexionRetour=ReflectorC
    return(ListeConnexionRetour)


def InputDecalageRotor():
    global NumLettreAlphabet
    ListeOrdreRotor=[]
    ListeOrdreOK=0
    NombreTropGrand=0
    print("Il faut enfin donner le décalage des rotors")
    OrdreRotor=str(input("Donner 3 chiffres entre 1 et 26: "))
    while ListeOrdreOK!=1:
        for k in range (0,len(OrdreRotor)):
            try:
                Caractere=int(OrdreRotor[k])
            except ValueError:
                Caractere=100
            if Caractere in NumLettreAlphabet:
                if k!=len(OrdreRotor)-1:
                    try:
                        CaractereSuivant=int(OrdreRotor[k+1])
                    except ValueError:
                        CaractereSuivant=100
                else:
                    CaractereSuivant=100
                if k!=0:
                    try:
                        CaracterePrecedent=int(OrdreRotor[k-1])
                    except ValueError:
                        CaracterePrecedent=100
                else:
                    CaracterePrecedent=100
                if (CaractereSuivant in NumLettreAlphabet) or (CaractereSuivant==0):
                    ListeOrdreRotor.append(Caractere*10+CaractereSuivant)
                elif not (CaracterePrecedent in NumLettreAlphabet):
                    ListeOrdreRotor.append(Caractere)
        for l in range (0,len(ListeOrdreRotor)):
            if ListeOrdreRotor[l]>26:
                NombreTropGrand=1
        if (len(ListeOrdreRotor)!=3) or (NombreTropGrand==1):
            NombreTropGrand=0
            ListeOrdreRotor=[]
            OrdreRotor=str(input("Il faut donner seulement trois nombres entre 1 et 26: "))
        else:
            ListeOrdreOK=1
    return(ListeOrdreRotor)

