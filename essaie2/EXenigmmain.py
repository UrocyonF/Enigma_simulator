#regarder les rotors tourne pas toujours à la même lettre (z) mais on peut choisir à quelle moment ils vont tourner (regarder vid yt)

import EXenigminput, EXenigmfct


Alphabet=('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')

AccentA=('á','à','â','ã','å','@','æ')
AccentO=('ó','ò','ô','õ','ö','ø','œ')
AccentE=('é','è','ê','ë','&')
AccentI=('í','ì','î','ï')
AccentU=('ú','ù','û','ü')
AccentC=('ç')
AccentY=('ý')
AccentN=('ñ')

Stop=0
ListeExOrdreRotor=[]
ListeExRotor=[]

ListeLettres=[]


ListeConnexionAvant=EXenigminput.InputConnextAvant()

ListeRotor=EXenigminput.InputRotor()

ListeConnexionRetour=EXenigminput.InputReflecteur()

ListeOrdreRotor=EXenigminput.InputDecalageRotor()


for m in range (0,3):
    Rotor=ListeRotor[m]
    print(Rotor)
    for n in range (0,ListeOrdreRotor[m]-1):
        Rotor=EXenigmfct.fRotationRotor(Rotor)
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
    ListeExOrdreRotor=EXenigmfct.fCopyRotor(ListeOrdreRotor)
    ListeExRotor=EXenigmfct.fCopyRotor(ListeRotor)
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

        ListeRotor[0]=EXenigmfct.fRotationRotor(ListeRotor[0])
        if ListeOrdreRotor[0]==26:
            ListeRotor[1]=EXenigmfct.fRotationRotor(ListeRotor[1])
            if ListeOrdreRotor[1]==26:
                ListeRotor[2]=EXenigmfct.fRotationRotor(ListeRotor[2])
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
        ListeOrdreRotor=EXenigmfct.fCopyRotor(ListeExOrdreRotor)
        ListeRotor=EXenigmfct.fCopyRotor(ListeExRotor)
    elif Choix==3:
        break
    print(ListeRotor,ListeOrdreRotor,len(ListeLettres))


    ListeLettres=[]
    ListeTraduction=[]
    