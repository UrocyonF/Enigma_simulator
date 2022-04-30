import matplotlib as plt


figure, axes = plt.subplots()
axes.set_aspect(1)

plt.xlim(-1, 1)
plt.ylim(-1, 1)
    
axes.xaxis.set_visible(False)
axes.yaxis.set_visible(False)


def TraceCroix(CooCentre,Largeur):
    if CooCentre[0]!=CooCentre[1]:
        plt.hlines(CooCentre[0],CooCentre[1]+(Largeur/2),CooCentre[1]-(Largeur/2),color="black")
        plt.vlines(CooCentre[1],CooCentre[0]+(Largeur/2),CooCentre[0]-(Largeur/2),color="black")
    else:
        plt.hlines(CooCentre[1],CooCentre[1]+(Largeur/2),CooCentre[1]-(Largeur/2),color="black")
        plt.vlines(CooCentre[0],CooCentre[0]+(Largeur/2),CooCentre[0]-(Largeur/2),color="black")

def TraceDecoupe(CooDepart,Largeur,NbrX,NbrY):
    for x in range (0,NbrX):
        for y in range (0,NbrY):
            TraceCroix((CooDepart[1]-(y/(1/Largeur)),CooDepart[0]+(x/(1/Largeur))),Largeur)


TraceCroix((0,0),2)
TraceDecoupe((-0.5,0.5),1,2,2)

#TraceCroix((0.5,0.5),1)

#TraceDecoupe((-0.25,0.25),0.5,2,2)
#TraceDecoupe((-0.875,0.875),0.25,6,3)


plt.show()