import random

NumLettreAlphabet=[]
ListeLettres=[]
ListeTraduction=[]

ListeConnexionAvant=[]
LettreConnexionA=[]
LettreConnexionB=[]

ListeRotor=[]
ListeExRotor=[]
NumRotor=[]

ListeConnexionRetour=[]
NumConnexionRetourA=[]
NumConnexionRetourB=[]

ListeOrdreRotor=[]
ListeExOrdreRotor=[]
NombreTropGrand=0
ListeOrdreOK=0

Rotor1=[]
Rotor2=[]
Rotor3=[]

Alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
AccentA=['á','à','â','ã','å','@','æ']
AccentO=['ó','ò','ô','õ','ö','ø','œ']
AccentE=['é','è','ê','ë','&']
AccentI=['í','ì','î','ï']
AccentU=['ú','ù','û','ü']
AccentC=['ç']
AccentY=['ý']
AccentN=['ñ']

RotorI=[[1, 5], [2, 11], [3, 13], [4, 6], [5, 12], [6, 7], [7, 4], [8, 17], [9, 22], [10, 26], [11, 14], [12, 20], [13, 15], [16, 23], [14, 25], [15, 8], [17, 24], [18, 21], [19, 19], [20, 16], [21, 1], [22, 9], [23, 2], [24, 18], [25, 3], [26, 10]]
RotorII=[[1, 1], [2, 10], [3, 4], [4, 11], [5, 19], [6, 9], [7, 18], [8, 21], [9, 24], [10, 2], [11, 12], [12, 8], [13, 23], [14, 20], [15, 13], [16, 3], [17, 17], [18, 7], [19, 26], [20, 14], [21, 16], [22, 25], [23, 6], [24, 22], [25, 15], [26, 5]]
RotorIII=[[1, 2], [2, 4], [3, 6], [4, 8], [5, 10], [6, 12], [7, 3], [8, 16], [9, 18], [10, 20], [11, 24], [12, 22], [13, 26], [14, 14], [15, 25], [16, 5], [17, 9], [18, 23], [19, 7], [20, 1], [21, 11], [22, 13], [23, 21], [24, 19], [25, 17], [26, 15]]
RotorIV=[[1, 5], [2, 19], [3, 15], [4, 22], [5, 16], [6, 26], [7, 10], [8, 1], [9, 25], [10, 17], [11, 21], [12, 9], [13, 18], [14, 8], [15, 24], [16, 12], [17, 14], [18, 6], [19, 20], [20, 7], [21, 11], [22, 4], [23, 3], [24, 13], [25, 23], [26, 2]]
RotorV=[[1, 22], [2, 26], [3, 2], [4, 18], [5, 7], [6, 9], [7, 20], [8, 25], [9, 21], [10, 16], [11, 19], [12, 4], [13, 14], [14, 8], [15, 12], [16, 24], [17, 1], [18, 23], [19, 13], [20, 10], [21, 17], [22, 15], [23, 6], [24, 5], [25, 3], [26, 11]]
RotorVI=[[1, 10], [2, 16], [3, 7], [4, 22], [5, 15], [6, 21], [7, 13], [8, 6], [9, 25], [10, 17], [11, 2], [12, 5], [13, 14], [14, 8], [15, 26], [16, 18], [17, 4], [18, 11], [19, 1], [20, 19], [21, 24], [22, 12], [23, 9], [24, 3], [25, 20], [26, 23]]
RotorVII=[[1, 14], [2, 26], [3, 10], [4, 8], [5, 7], [6, 18], [7, 3], [8, 24], [9, 13], [10, 25], [11, 19], [12, 23], [13, 2], [14, 15], [15, 21], [16, 6], [17, 1], [18, 9], [19, 22], [20, 12], [21, 16], [22, 5], [23, 11], [24, 17], [25, 4], [26, 20]]
RotorVIII=[[1, 6], [2, 11], [3, 17], [4, 8], [5, 20], [6, 12], [7, 24], [8, 15], [9, 3], [10, 2], [11, 10], [12, 19], [13, 16], [14, 4], [15, 26], [16, 18], [17, 1], [18, 13], [19, 5], [20, 23], [21, 14], [22, 9], [23, 21], [24, 25], [25, 7], [26, 22]]

ReflectorA=[['a','e'],['b','j'],['c','m'],['d','z'],['f','l'],['g','y'],['h','x'],['i','v'],['k','w'],['n','r'],['o','q'],['p','u'],['s','t']]
ReflectorB=[['a','y'],['b','r'],['c','u'],['d','h'],['e','q'],['f','s'],['g','l'],['i','p'],['j','x'],['k','n'],['m','o'],['t','z'],['v','w']]
ReflectorC=[['a','f'],['b','v'],['c','p'],['d','j'],['e','i'],['g','o'],['h','y'],['k','r'],['l','z'],['m','x'],['n','w'],['q','t'],['u','s']]

Stop=0


def fRotationRotor(Rotor):
    for i in range (0,len(Rotor)):
        connect=Rotor[i]
        if connect[1]==26:
            connect[1]=1
        else:
            connect[1]+=1
    return(Rotor)


def fCopyRotor(Rotor):
    CopyRotor=[]
    if type(Rotor[0])==list:
        if type(Rotor[0][0])==list:
            if type(Rotor[0][0][0])==list:
                print('copy pas possible')
            else:
                for a in range (0,len(Rotor)):
                    MiCopyRot=[]
                    for b in range (0,len(Rotor[a])):
                        MiCopyRot.append(Rotor[a][b].copy())
                    CopyRotor.append(MiCopyRot)
        else:
            for c in range(0,len(Rotor)):
                CopyRotor.append(Rotor[c])              
    else:
        CopyRotor=Rotor[:]
    return(CopyRotor)


for e in range(0,len(Alphabet)):
    NumLettreAlphabet.append(e+1)
    

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
        while (not (LettreA in Alphabet)) or (LettreA in LettreConnexionA):
            lettreA=str(input("Il faut donner une simple première lettre de l'alphabet qui n'est pas déjà lié: "))
        LettreB=str(input("Deuxième lettre: "))
        while (not (LettreB in Alphabet)) or (LettreB in LettreConnexionB) or (LettreB==LettreA):
            LettreB=str(input("Il faut donner une simple deuxième lettre de l'alphabet qui n'est pas déjà lié: "))
        LettreConnexionA.append(LettreA)
        LettreConnexionA.append(LettreB)
        LettreConnexionB.append(LettreA)
        LettreConnexionB.append(LettreB)
        ListeConnexionAvant.append([LettreA,LettreB])
else:
    for g in range (0,NombreCable):
        LettreA=random.choice(Alphabet)
        while LettreA in LettreConnexionA:
            LettreA=random.choice(Alphabet)
        LettreB=random.choice(Alphabet)
        while (LettreB in LettreConnexionB) or (LettreB==LettreA):
            LettreB=random.choice(Alphabet)
        LettreConnexionA.append(LettreA)
        LettreConnexionA.append(LettreB)
        LettreConnexionB.append(LettreA)
        LettreConnexionB.append(LettreB)
        ListeConnexionAvant.append([LettreA,LettreB])


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
        ListeRotor.append(RotorI)
    elif NumRotor[j]==2:
        ListeRotor.append(RotorII)
    elif NumRotor[j]==3:
        ListeRotor.append(RotorIII)
    elif NumRotor[j]==4:
        ListeRotor.append(RotorIV)
    elif NumRotor[j]==5:
        ListeRotor.append(RotorV)
    elif NumRotor[j]==6:
        ListeRotor.append(RotorVI)
    elif NumRotor[j]==7:
        ListeRotor.append(RotorVII)
    else:
        ListeRotor.append(RotorVIII)


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


for m in range (0,3):
    Rotor=ListeRotor[m]
    for n in range (0,ListeOrdreRotor[m]-1):
        Rotor=fRotationRotor(Rotor)
    if m==0:
        Rotor1=Rotor
    if m==1:
        Rotor2=Rotor
    if m==2:
        Rotor3=Rotor
ListeRotor=[Rotor1,Rotor2,Rotor3]


print("\n------------------------\n")
print("En résumé on a:")
print("Les connexions avant sont: ",ListeConnexionAvant)
print("Les rotors choisit sont: ",ListeRotor)
print("L'ordre des rotors est: ",ListeOrdreRotor)
print("Les connexions du réflecteur sont: ",ListeConnexionRetour)


while Stop==0:
    ListeLettreFinal=[]
    ListeExOrdreRotor=fCopyRotor(ListeOrdreRotor)
    ListeExRotor=fCopyRotor(ListeRotor)
    TexteATrad=str(input("Donner le texte sans majuscule ni chiffre: "))
    for n in range (0,len(TexteATrad)):
        Caractere=TexteATrad[n]
        if Caractere in Alphabet:
            ListeLettres.append(Caractere)
        if Caractere in AccentA:
            if Caractere==AccentA[6]:
                ListeLettres.append('a')
                ListeLettres.append('e')
            else:
                ListeLettres.append('a')
        if Caractere in AccentO:
            if Caractere==AccentO[6]:
                ListeLettres.append('o')
                ListeLettres.append('e')
            else:
                ListeLettres.append('o')
        if Caractere in AccentE:
            if Caractere==AccentE[4]:
                ListeLettres.append('e')
                ListeLettres.append('t')
            else:
                ListeLettres.append('e')
        if Caractere in AccentI:
            ListeLettres.append('i')
        if Caractere in AccentU:
            ListeLettres.append('u')
        if Caractere in AccentC:
            ListeLettres.append('c')
        if Caractere in AccentY:
            ListeLettres.append('y')
        if Caractere in AccentN:
            ListeLettres.append('n')
    print("Le texte à traduire: ",ListeLettres)


    for o in range (0,len(ListeLettres)):
        Lettre=ListeLettres[o]
        for p in range (0,len(ListeConnexionAvant)):
            Connexion=ListeConnexionAvant[p]
            if Lettre==Connexion[0]:
                Lettre=Connexion[1]
            elif Lettre==Connexion[1]:
                Lettre=Connexion[0]
        Num=Alphabet.index(Lettre)+1
        for q in range (0,3):
            Rotor=ListeRotor[q]
            for r in range (0,len(Rotor)):
                LettreRotor=Rotor[r]
                if Num==LettreRotor[0]:
                    Num=LettreRotor[1]
                    break
            Lettre=Alphabet[Num-1]
        for s in range (0,len(ListeConnexionRetour)):
            Connexion=ListeConnexionRetour[s]
            if Lettre==Connexion[0]:
                Lettre=Connexion[1]
            elif Lettre==Connexion[1]:
                Lettre=Connexion[0]
        Num=Alphabet.index(Lettre)+1
        for t in range (0,3):
            Rotor=ListeRotor[2-t]
            for u in range (0,len(Rotor)):
                LettreRotor=Rotor[u]
                if Num==LettreRotor[1]:
                    Num=LettreRotor[0]
                    break
            Lettre=Alphabet[Num-1]     
        for v in range (0,len(ListeConnexionAvant)):
            Connexion=ListeConnexionAvant[v]
            if Lettre==Connexion[0]:
                Lettre=Connexion[1]
            elif Lettre==Connexion[1]:
                Lettre=Connexion[0]
        ListeLettreFinal.append(Lettre)

        ListeRotor[0]=fRotationRotor(ListeRotor[0])
        if ListeOrdreRotor[0]==26:
            ListeRotor[1]=fRotationRotor(ListeRotor[1])
            if ListeOrdreRotor[1]==26:
                ListeRotor[2]=fRotationRotor(ListeRotor[2])
                if ListeOrdreRotor[2]==26:
                    ListeOrdreRotor=[1,1,1]
                else:
                    ListeOrdreRotor[2]+=1
            else:
                ListeOrdreRotor[1]+=1
        else:
            ListeOrdreRotor[0]+=1
            
            
    print("Le texte sorti est: ",ListeLettreFinal)
    LettreFinal = ''.join(str(elem) for elem in ListeLettreFinal) 
    print("Le texte finalement traduit est: ",LettreFinal)
    print("\n------------------------\n")

    print(ListeRotor,ListeOrdreRotor)
    Choix=int(input("Continuer avec la config des rotors finales (1) ou remettre comment avant (2) ou stoper (3): "))
    if Choix==2:
        ListeOrdreRotor=fCopyRotor(ListeExOrdreRotor)
        ListeRotor=fCopyRotor(ListeExRotor)
    elif Choix==3:
        break
    print(ListeRotor,ListeOrdreRotor,len(ListeLettres))
        
    ListeLettres=[]
    ListeTraduction=[]
 