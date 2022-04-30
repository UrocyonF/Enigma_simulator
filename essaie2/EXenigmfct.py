
#ça ça marche pr des listes pas des tuples comme les nouveaux rotors
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


def fTupleToList(Tuple):
    rtnListe=[]
    rtnListe=list(Tuple)
    for i in range (0,len(Tuple)):
        if type(Tuple[i])==tuple:
            rtnListe[i]=list(Tuple[i])
            for j in range (0,len(Tuple[i])):
                if type(Tuple[i][j])==tuple:
                    rtnListe[i][j]=list(Tuple[i][j])
    return(rtnListe)                


#Pourquoi c'est là ça ???
#print(fTupleToList(((1, 14), (2, 26), (3, 10), (4, 8), (5, 7), (6, 18), (7, 3), (8, 24), (9, 13), (10, 25), (11, 19), (12, 23), (13, 2), (14, 15), (15, 21), (16, 6), (17, 1), (18, 9), (19, 22), (20, 12), (21, 16), (22, 5), (23, 11), (24, 17), (25, 4), (26, 20))))
